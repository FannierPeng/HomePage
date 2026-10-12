---
layout: about
title: 首页
permalink: /
nav: true
nav_order: 1
subtitle: 副教授 · 多模态大模型与视觉语言学习
profile:
  align: left
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p><a href="mailto:pengfang_cau@qq.com"><i class="fa-solid fa-envelope" aria-hidden="true"></i> pengfang_cau@qq.com</a></p>
    <p><i class="fa-solid fa-flask" aria-hidden="true"></i> 多模态大模型 · 视觉语言学习 · 小样本迁移</p>
social: true
announcements:
  enabled: false
latest_posts:
  enabled: false
---

<style>
/* 首页专属样式：不修改 al-folio 核心布局，保留其主题与深色模式。 */
body {
  font-family: Inter, -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}
main { font-size: 16px; line-height: 1.78; }
main h1 {
  font-size: clamp(1.9rem, 3.4vw, 2.45rem);
  line-height: 1.28;
  font-weight: 760;
  letter-spacing: -0.025em;
}
main h2 {
  position: relative;
  margin: 2.7rem 0 1.15rem;
  padding-bottom: 0.62rem;
  border-bottom: 1px solid var(--global-divider-color, #e5e7eb);
  font-size: clamp(1.42rem, 2.2vw, 1.7rem);
  line-height: 1.4;
  font-weight: 760;
  letter-spacing: -0.018em;
}
main h2::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -1px;
  width: 3.2rem;
  height: 3px;
  border-radius: 8px;
  background: var(--global-theme-color, #7952b3);
}
main h3 { margin: 0 0 0.55rem; font-size: 1.12rem; line-height: 1.5; font-weight: 730; }
main p { font-size: 1rem; line-height: 1.85; }
.profile .more-info, .profile .more-info p { font-size: 0.9rem; line-height: 1.7; }
.profile .more-info p { margin: 0.45rem 0; }
.fang-homepage {
  --fp-accent: var(--global-theme-color, #7952b3);
  --fp-border: var(--global-divider-color, #e5e7eb);
  --fp-text: var(--global-text-color, #252832);
  color: var(--fp-text);
  font-size: 1rem;
  line-height: 1.82;
}
.fang-homepage p { font-size: 1rem; line-height: 1.85; }
.fang-homepage .fp-intro { font-size: 1.04rem; line-height: 1.95; margin: 0.1rem 0 0.85rem; }
.fang-homepage .fp-muted { color: var(--global-text-color-light, #6b7280); font-size: 0.91rem; }
.fang-homepage .fp-timeline {
  position: relative;
  margin: 0.55rem 0 0.25rem 0.45rem;
  padding-left: 1.55rem;
  border-left: 2px solid var(--fp-border);
}
.fang-homepage .fp-timeline-item {
  position: relative;
  padding: 0 0 1.2rem;
  animation: fp-rise-in 620ms cubic-bezier(.2,.7,.2,1) both;
  animation-delay: var(--fp-delay, 0ms);
}
.fang-homepage .fp-timeline-item:last-child { padding-bottom: 0.15rem; }
.fang-homepage .fp-timeline-item::before {
  content: "";
  position: absolute;
  left: calc(-1.55rem - 6px);
  top: 0.94rem;
  width: 10px;
  height: 10px;
  border: 3px solid var(--global-bg-color, #fff);
  border-radius: 50%;
  background: var(--fp-accent);
  box-shadow: 0 0 0 2px color-mix(in srgb, var(--fp-accent) 28%, transparent);
  transition: transform 220ms ease, box-shadow 220ms ease;
}
.fang-homepage .fp-timeline-item:hover::before {
  transform: scale(1.18);
  box-shadow: 0 0 0 5px color-mix(in srgb, var(--fp-accent) 13%, transparent);
}
.fang-homepage .fp-date {
  display: inline-flex;
  align-items: center;
  margin: 0 0 0.55rem;
  padding: 0.22rem 0.68rem;
  border: 1px solid color-mix(in srgb, var(--fp-accent) 24%, var(--fp-border));
  border-radius: 999px;
  background: color-mix(in srgb, var(--fp-accent) 7%, transparent);
  color: var(--fp-accent);
  font-size: 0.82rem;
  font-weight: 720;
  letter-spacing: 0.01em;
}
.fang-homepage .fp-card {
  border: 1px solid var(--fp-border);
  border-radius: 14px;
  background: color-mix(in srgb, var(--global-bg-color, #fff) 97%, var(--fp-accent) 3%);
  padding: 1rem 1.1rem;
  transition: transform 220ms ease, border-color 220ms ease, box-shadow 220ms ease;
}
.fang-homepage .fp-card:hover {
  transform: translateY(-3px);
  border-color: color-mix(in srgb, var(--fp-accent) 45%, var(--fp-border));
  box-shadow: 0 8px 22px color-mix(in srgb, var(--fp-accent) 10%, transparent);
}
.fang-homepage .fp-card-title {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.4rem 0.65rem;
  margin: 0 0 0.2rem;
  font-size: 1.08rem;
  line-height: 1.55;
}
.fang-homepage .fp-tag {
  display: inline-block;
  padding: 0.1rem 0.52rem;
  border-radius: 6px;
  background: color-mix(in srgb, var(--fp-accent) 10%, transparent);
  color: var(--fp-accent);
  font-size: 0.77rem;
  font-weight: 730;
}
.fang-homepage .fp-meta, .fang-homepage .fp-mentor {
  margin: 0.28rem 0 0;
  font-size: 0.92rem;
  line-height: 1.7;
}
.fang-homepage .fp-meta { color: var(--global-text-color-light, #6b7280); }
.fang-homepage .fp-mentor { opacity: 0.93; }
.fang-homepage .fp-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.9rem; margin-top: 0.8rem; }
.fang-homepage .fp-research-card { height: 100%; padding: 1.08rem 1.1rem; animation: fp-rise-in 620ms cubic-bezier(.2,.7,.2,1) both; animation-delay: var(--fp-delay, 0ms); }
.fang-homepage .fp-research-heading { display: flex; align-items: center; gap: 0.65rem; margin-bottom: 0.45rem; font-size: 1.03rem; font-weight: 740; line-height: 1.5; }
.fang-homepage .fp-icon { display: inline-flex; align-items: center; justify-content: center; flex: 0 0 2.05rem; width: 2.05rem; height: 2.05rem; border-radius: 10px; background: color-mix(in srgb, var(--fp-accent) 11%, transparent); color: var(--fp-accent); }
.fang-homepage .fp-research-card p { font-size: 0.94rem; line-height: 1.8; margin: 0.3rem 0 0; }
.fang-homepage .fp-paper-card { margin: 0.85rem 0; }
.fang-homepage .fp-paper-card .fp-research-heading { align-items: flex-start; font-size: 1.04rem; }
.fang-homepage .fp-paper-meta { margin-top: 0.6rem !important; font-size: 0.88rem !important; color: var(--global-text-color-light, #6b7280); }
.fang-homepage a.fp-button {
  display: inline-flex; align-items: center; gap: 0.45rem; margin-top: 0.65rem; padding: 0.48rem 0.85rem;
  border: 1px solid color-mix(in srgb, var(--fp-accent) 36%, var(--fp-border)); border-radius: 9px;
  color: var(--fp-accent); font-size: 0.9rem; font-weight: 680; text-decoration: none;
  transition: background 180ms ease, transform 180ms ease;
}
.fang-homepage a.fp-button:hover { background: color-mix(in srgb, var(--fp-accent) 9%, transparent); text-decoration: none; transform: translateY(-1px); }
@keyframes fp-rise-in { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
@media (max-width: 640px) {
  main { font-size: 15.5px; }
  main h2 { margin-top: 2.2rem; }
  .fang-homepage .fp-grid { grid-template-columns: minmax(0, 1fr); }
  .fang-homepage .fp-card { padding: 0.9rem; }
}
@media (prefers-reduced-motion: reduce) {
  .fang-homepage .fp-timeline-item, .fang-homepage .fp-research-card { animation: none; }
  .fang-homepage .fp-card, .fang-homepage .fp-timeline-item::before, .fang-homepage a.fp-button { transition: none; }
}
</style>

<div class="fang-homepage">

<h2>关于我</h2>
<p class="fp-intro">彭芳，现任华南农业大学数学与信息学院软件学院副教授，博士毕业于中山大学计算机学院。研究方向包括<strong>多模态大模型、视觉语言预训练、小样本迁移学习与视觉理解</strong>。研究工作聚焦于视觉语言预训练模型的小样本适配、视频动作识别中的实例级语义建模，以及多模态大语言模型的视觉判别能力增强。</p>

<h2>教育背景</h2>
<div class="fp-timeline">
  <article class="fp-timeline-item" style="--fp-delay: 0ms">
    <div class="fp-date">2022.09 — 2026.06</div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>中山大学</strong><span class="fp-tag">博士</span></div>
      <p class="fp-meta">计算机学院</p>
      <p class="fp-mentor">导师：王昌栋教授</p>
    </div>
  </article>
  <article class="fp-timeline-item" style="--fp-delay: 100ms">
    <div class="fp-date">2018.09 — 2021.06</div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>中山大学</strong><span class="fp-tag">硕士</span></div>
      <p class="fp-meta">计算机学院</p>
      <p class="fp-mentor">导师：王昌栋教授</p>
    </div>
  </article>
  <article class="fp-timeline-item" style="--fp-delay: 200ms">
    <div class="fp-date">2014.09 — 2018.06</div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>华南农业大学</strong><span class="fp-tag">学士</span></div>
      <p class="fp-meta">数学与信息学院软件学院</p>
      <p class="fp-mentor">导师：黄栋教授</p>
    </div>
  </article>
</div>

<h2>工作经历</h2>
<div class="fp-timeline">
  <article class="fp-timeline-item" style="--fp-delay: 0ms">
    <div class="fp-date">2026.07 — 至今</div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>华南农业大学</strong><span class="fp-tag">副教授</span></div>
      <p class="fp-meta">数学与信息学院软件学院</p>
      <p class="fp-mentor">从事计算机与人工智能相关教学和科研工作。</p>
    </div>
  </article>
</div>

<h2>研究方向</h2>
<div class="fp-grid">
  <article class="fp-card fp-research-card" style="--fp-delay: 0ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-eye" aria-hidden="true"></i></span>多模态大模型视觉理解</div>
    <p>研究生成式多模态模型的视觉识别与细粒度判别能力，探索在不依赖额外外部知识的情况下激发模型内在视觉能力。</p>
  </article>
  <article class="fp-card fp-research-card" style="--fp-delay: 80ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-diagram-project" aria-hidden="true"></i></span>视觉语言模型小样本迁移</div>
    <p>研究通用预训练知识与任务特定视觉信息的高效融合，提升少样本场景下的适配效果并尽可能保持模型泛化能力。</p>
  </article>
  <article class="fp-card fp-research-card" style="--fp-delay: 160ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-film" aria-hidden="true"></i></span>小样本视频理解</div>
    <p>面向少样本动作识别，探索实例级代理语义建模与动态时序信息学习。</p>
  </article>
  <article class="fp-card fp-research-card" style="--fp-delay: 240ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-water" aria-hidden="true"></i></span>视觉理解应用</div>
    <p>关注细粒度图像分类、水下图像目标检测等视觉任务。</p>
  </article>
</div>

<h2>代表性研究</h2>
<div class="fp-card fp-paper-card">
  <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-brain" aria-hidden="true"></i></span>GROVE：多模态大语言模型的视觉判别增强</div>
  <p>针对多模态大语言模型在视觉识别任务中的判别能力不足问题，提出组相对视觉判别增强方法 GROVE，通过轻量视觉路由插件与组相对奖惩机制激发模型内在视觉判别潜力。</p>
  <p class="fp-paper-meta"><strong>IEEE Transactions on Circuits and Systems for Video Technology</strong>, 2026。</p>
  <a class="fp-button" href="https://github.com/FannierPeng/GROVE" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-github" aria-hidden="true"></i> 查看代码</a>
  <a class="fp-button" href="https://doi.org/10.1109/TCSVT.2026.3652189" target="_blank" rel="noopener noreferrer"><i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i> 查看论文</a>
</div>
<div class="fp-card fp-paper-card">
  <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-video" aria-hidden="true"></i></span>ProLIPS：面向小样本动作识别的实例级代理语义学习</div>
  <p>提出渐进式实例级代理语义学习方法 ProLIPS，通过代理语义扩散模块与预训练知识引导机制，建模少样本视频中的动态时序语义。</p>
  <p class="fp-paper-meta"><strong>IEEE Transactions on Multimedia</strong>, 2026。</p>
  <a class="fp-button" href="https://doi.org/10.1109/TMM.2025.3632652" target="_blank" rel="noopener noreferrer"><i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i> 查看论文</a>
</div>
<div class="fp-card fp-paper-card">
  <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-layer-group" aria-hidden="true"></i></span>SgVA-CLIP：语义引导的视觉语言模型小样本适配</div>
  <p>通过隐式知识蒸馏将跨模态原型中的细粒度相对语义迁移至视觉特征空间，实现预训练知识与任务特定视觉知识的高效融合。</p>
  <p class="fp-paper-meta"><strong>IEEE Transactions on Multimedia</strong>, 2024。</p>
  <a class="fp-button" href="https://doi.org/10.1109/TMM.2023.3311646" target="_blank" rel="noopener noreferrer"><i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i> 查看论文</a>
</div>

<p><a class="fp-button" href="{{ '/publications/' | relative_url }}"><i class="fa-solid fa-book-open" aria-hidden="true"></i> 查看全部学术成果</a>　<a class="fp-button" href="{{ '/cv/' | relative_url }}"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i> 教育与经历</a></p>

</div>
