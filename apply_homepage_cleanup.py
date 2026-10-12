#!/usr/bin/env python3
"""Apply the one-homepage navigation cleanup for Fang Peng's al-folio site.

Run once from the website repository root after copying the package files into place:
    python3 apply_homepage_cleanup.py

The script preserves removed pages under _homepage_cleanup_backup/<timestamp>/,
keeps only 首页 and 学术成果 in the top navbar, disables other page navigation,
and corrects Jekyll Scholar's first/last-name order for author highlighting.
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
import shutil
import sys

ROOT = Path.cwd()
PAGES = ROOT / "_pages"
HOME = PAGES / "about.md"
PUBLICATIONS = PAGES / "publications.md"
CONFIG = ROOT / "_config.yml"
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
BACKUP = ROOT / "_homepage_cleanup_backup" / STAMP
PAGE_EXTENSIONS = {".md", ".markdown", ".html"}


def read_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, flags=re.S)
    if not match:
        return text, None, None
    return text, match, match.group(1)


def yaml_value(front: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}\s*:\s*(.*?)\s*$", front)
    if not match:
        return ""
    return match.group(1).split(" #", 1)[0].strip().strip("\"'")


def set_front_matter(path: Path, updates: dict[str, str]) -> bool:
    text, match, front = read_front_matter(path)
    if match is None:
        return False
    original = front
    for key, value in updates.items():
        line_re = re.compile(rf"(?m)^{re.escape(key)}\s*:.*$")
        replacement = f"{key}: {value}"
        if line_re.search(front):
            front = line_re.sub(replacement, front, count=1)
        else:
            front = front.rstrip() + "\n" + replacement
    if front == original:
        return False
    updated = "---\n" + front.rstrip() + "\n---\n" + text[match.end():]
    path.write_text(updated, encoding="utf-8")
    return True


def page_should_be_removed(path: Path, front: str) -> bool:
    if path in (HOME, PUBLICATIONS):
        return False
    stem = path.stem.casefold().replace("-", "_")
    title = yaml_value(front, "title").casefold()
    permalink_value = yaml_value(front, "permalink")
    is_root_permalink = permalink_value == "/"
    title_norm = re.sub(r"[\s_\-]+", "", title)

    # Remove obsolete research/projects pages and the explicitly unwanted People page.
    if stem.startswith(("research", "project", "科研")) or "科研" in title_norm or "research" in title_norm:
        return True
    if stem.startswith(("people", "team", "member")) or any(token in title_norm for token in ("people", "team", "members", "团队成员", "团队", "成员")):
        return True

    # Remove separate CV/education pages now integrated into the homepage.
    if stem.startswith(("cv", "education", "educational", "resume")):
        return True
    if "教育" in title_norm or title_norm in {"个人简历", "简历", "cv", "resume", "education"}:
        return True

    # Preserve about.md as canonical; move duplicate pages that create extra 首页/主页 tabs or root URLs.
    if title_norm in {"首页", "主页", "home", "homepage", "mainpage"} or is_root_permalink:
        return True
    return False


def update_scholar_name_order():
    if not CONFIG.exists():
        print("提示：未找到 _config.yml，跳过 Scholar 作者姓名配置修正。")
        return False
    text = CONFIG.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    in_scholar = False
    scholar_indent = 0
    changed = False
    for i, line in enumerate(lines):
        if re.match(r"^scholar\s*:\s*(?:#.*)?$", line.rstrip("\r\n")):
            in_scholar = True
            scholar_indent = len(line) - len(line.lstrip())
            continue
        if in_scholar:
            if line.strip() and not line.lstrip().startswith("#"):
                indent = len(line) - len(line.lstrip())
                if indent <= scholar_indent and ":" in line:
                    break
            if re.match(r"^\s+last_name\s*:\s*\[Fang\]\s*(?:#.*)?$", line.rstrip("\r\n")):
                ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
                lines[i] = re.sub(r"last_name\s*:\s*\[Fang\]", "last_name: [Peng]", line.rstrip("\r\n")) + ending
                changed = True
            elif re.match(r"^\s+first_name\s*:\s*\[Peng\]\s*(?:#.*)?$", line.rstrip("\r\n")):
                ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
                lines[i] = re.sub(r"first_name\s*:\s*\[Peng\]", "first_name: [Fang]", line.rstrip("\r\n")) + ending
                changed = True
    if changed:
        CONFIG.write_text("".join(lines), encoding="utf-8")
    return changed


def main() -> int:
    if not PAGES.is_dir():
        print("错误：请在网站仓库根目录运行本脚本（需要存在 _pages/）。", file=sys.stderr)
        return 2
    if not HOME.is_file() or not PUBLICATIONS.is_file():
        print("错误：请先把压缩包中的 _pages/about.md 和 _pages/publications.md 覆盖到仓库。", file=sys.stderr)
        return 2

    # Normalize the only two navigation-visible pages.
    set_front_matter(HOME, {"title": "首页", "permalink": "/", "nav": "true", "nav_order": "1"})
    set_front_matter(PUBLICATIONS, {"title": "学术成果", "permalink": "/publications/", "nav": "true", "nav_order": "2"})

    moved, hidden, changed = [], [], []
    candidates = sorted(p for p in PAGES.iterdir() if p.is_file() and p.suffix.lower() in PAGE_EXTENSIONS)
    for path in candidates:
        if path in (HOME, PUBLICATIONS):
            continue
        _, match, front = read_front_matter(path)
        if match is None:
            continue
        if page_should_be_removed(path, front):
            destination = BACKUP / path.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(destination))
            moved.append(f"{path.relative_to(ROOT)} -> {destination.relative_to(ROOT)}")
            continue
        if set_front_matter(path, {"nav": "false"}):
            hidden.append(str(path.relative_to(ROOT)))

    scholar_changed = update_scholar_name_order()
    print("单页主页清理完成。")
    print("导航中保留：")
    print("  - _pages/about.md（首页）")
    print("  - _pages/publications.md（学术成果）")
    print(f"移入备份的旧页面：{len(moved)}")
    for item in moved:
        print("  -", item)
    print(f"关闭导航的其他页面：{len(hidden)}")
    for item in hidden:
        print("  -", item)
    print("Scholar 姓名高亮配置：" + ("已修正" if scholar_changed else "无需修改/未发现旧配置"))
    if moved:
        print(f"备份目录：{BACKUP.relative_to(ROOT)}")
    print("请运行 git diff 检查变更，再提交到 GitHub。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
