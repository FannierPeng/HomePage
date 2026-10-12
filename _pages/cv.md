---
layout: page
title: 教育与经历
permalink: /cv/
description: 教育背景、工作经历与研究方向。
nav: true
nav_order: 4
---

<style>
main { font-size: 16px; line-height: 1.8; }
main h1 { font-size: clamp(1.8rem, 3vw, 2.25rem); line-height: 1.3; font-weight: 760; letter-spacing: -0.02em; }
main h2 { margin-top: 2.35rem; margin-bottom: 1rem; padding-bottom: 0.55rem; border-bottom: 1px solid var(--global-divider-color, #e5e7eb); font-size: clamp(1.3rem, 2.1vw, 1.55rem); font-weight: 740; }
.fang-cv { --cv-accent: var(--global-theme-color, #7952b3); --cv-border: var(--global-divider-color, #e5e7eb); font-size: 1rem; line-height: 1.8; }
.fang-cv .cv-timeline { position: relative; margin: 0.45rem 0 1rem 0.45rem; padding-left: 1.55rem; border-left: 2px solid var(--cv-border); }
.fang-cv .cv-item { position: relative; margin: 0 0 1.15rem; animation: cv-fade-up 600ms cubic-bezier(.2,.7,.2,1) both; animation-delay: var(--cv-delay, 0ms); }
.fang-cv .cv-item:last-child { margin-bottom: 0.2rem; }
.fang-cv .cv-item::before { content: ""; position: absolute; left: calc(-1.55rem - 6px); top: 0.95rem; width: 10px; height: 10px; border: 3px solid var(--global-bg-color, #fff); border-radius: 50%; background: var(--cv-accent); box-shadow: 0 0 0 2px color-mix(in srgb, var(--cv-accent) 28%, transparent); transition: transform 200ms ease; }
.fang-cv .cv-item:hover::before { transform: scale(1.18); }
.fang-cv .cv-date { display: inline-block; margin: 0 0 0.52rem; padding: 0.2rem 0.65rem; border: 1px solid color-mix(in srgb, var(--cv-accent) 24%, var(--cv-border)); border-radius: 999px; background: color-mix(in srgb, var(--cv-accent) 7%, transparent); color: var(--cv-accent); font-size: 0.82rem; font-weight: 720; }
.fang-cv .cv-card { padding: 1rem 1.1rem; border: 1px solid var(--cv-border); border-radius: 13px; background: color-mix(in srgb, var(--global-bg-color, #fff) 97%, var(--cv-accent) 3%); transition: transform 200ms ease, box-shadow 200ms ease, border-color 200ms ease; }
.fang-cv .cv-card:hover { transform: translateY(-2px); border-color: color-mix(in srgb, var(--cv-accent) 42%, var(--cv-border)); box-shadow: 0 8px 20px color-mix(in srgb, var(--cv-accent) 9%, transparent); }
.fang-cv .cv-title { display: flex; align-items: center; flex-wrap: wrap; gap: 0.4rem 0.65rem; font-size: 1.06rem; line-height: 1.55; }
.fang-cv .cv-tag { display: inline-block; padding: 0.1rem 0.5rem; border-radius: 6px; background: color-mix(in srgb, var(--cv-accent) 10%, transparent); color: var(--cv-accent); font-size: 0.78rem; font-weight: 700; }
.fang-cv .cv-meta { margin: 0.3rem 0 0; color: var(--global-text-color-light, #6b7280); font-size: 0.92rem; }
.fang-cv .cv-links { display: flex; flex-wrap: wrap; gap: 0.65rem; margin-top: 1rem; }
.fang-cv .cv-link { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.48rem 0.8rem; border: 1px solid color-mix(in srgb, var(--cv-accent) 32%, var(--cv-border)); border-radius: 8px; color: var(--cv-accent); font-size: 0.9rem; font-weight: 650; text-decoration: none; }
.fang-cv .cv-link:hover { background: color-mix(in srgb, var(--cv-accent) 8%, transparent); text-decoration: none; }
@keyframes cv-fade-up { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
@media (max-width: 640px) { main { font-size: 15.5px; } .fang-cv .cv-card { padding: 0.9rem; } }
@media (prefers-reduced-motion: reduce) { .fang-cv .cv-item { animation: none; } .fang-cv .cv-card, .fang-cv .cv-item::before { transition: none; } }
</style>

<div class="fang-cv">
<p>以下为教育背景与工作经历。首页展示简要时间轴，本页提供更完整的经历信息。</p>

<h2>教育背景</h2>
<div class="cv-timeline">
  <article class="cv-item" style="--cv-delay: 0ms">
    <div class="cv-date">2022.09 — 2026.06</div>
    <div class="cv-card">
      <div class="cv-title"><strong>中山大学 · 计算机学院</strong><span class="cv-tag">博士</span></div>
      <p class="cv-meta">导师：王昌栋教授</p>
    </div>
  </article>
  <article class="cv-item" style="--cv-delay: 100ms">
    <div class="cv-date">2018.09 — 2021.06</div>
    <div class="cv-card">
      <div class="cv-title"><strong>中山大学 · 计算机学院</strong><span class="cv-tag">硕士</span></div>
      <p class="cv-meta">导师：王昌栋教授</p>
    </div>
  </article>
  <article class="cv-item" style="--cv-delay: 200ms">
    <div class="cv-date">2014.09 — 2018.06</div>
    <div class="cv-card">
      <div class="cv-title"><strong>华南农业大学 · 数学与信息学院软件学院</strong><span class="cv-tag">学士</span></div>
      <p class="cv-meta">导师：黄栋教授</p>
    </div>
  </article>
</div>

<h2>工作经历</h2>
<div class="cv-timeline">
  <article class="cv-item" style="--cv-delay: 0ms">
    <div class="cv-date">2026.07 — 至今</div>
    <div class="cv-card">
      <div class="cv-title"><strong>华南农业大学</strong><span class="cv-tag">副教授</span></div>
      <p class="cv-meta">数学与信息学院软件学院</p>
      <p>从事计算机与人工智能相关教学和科研工作。</p>
    </div>
  </article>
</div>

<h2>研究方向</h2>
<ul>
  <li><strong>多模态大模型视觉理解与判别增强：</strong>探索细粒度视觉识别、视觉信息选择以及多模态大语言模型内在视觉能力激发。</li>
  <li><strong>视觉语言预训练模型的小样本适配与迁移：</strong>研究通用预训练知识与任务特定视觉信息的高效融合。</li>
  <li><strong>实例级时序语义建模与小样本视频理解：</strong>面向少样本动作识别，学习细粒度实例语义和动态时序信息。</li>
</ul>

<h2>代表性论文</h2>
<p>代表性论文及其 DOI、代码链接请见学术成果页面。</p>
<div class="cv-links">
  <a class="cv-link" href="{{ '/publications/' | relative_url }}"><i class="fa-solid fa-book-open" aria-hidden="true"></i> 查看学术成果</a>
  <a class="cv-link" href="mailto:pengfang_cau@qq.com"><i class="fa-solid fa-envelope" aria-hidden="true"></i> 联系我</a>
</div>
</div>
