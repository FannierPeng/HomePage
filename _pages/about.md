---
layout: about
title: 首页
permalink: /
nav: true
nav_order: 1
subtitle: 首聘副教授 · 多模态大模型与视觉语言学习
profile:
  align: left
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p><a href="mailto:pengfang_cau@qq.com"><i class="fa-solid fa-envelope" aria-hidden="true"></i> pengfang_cau@qq.com</a></p>
    <p><i class="fa-solid fa-flask" aria-hidden="true"></i> 多模态大模型 · 视觉语言学习 · 小样本迁移</p>
social: true
selected_papers: false
announcements:
  enabled: false
latest_posts:
  enabled: false
---

<style>
/* 页面局部样式：兼容 al-folio v1.x 的 Tailwind 样式模式，不依赖 Bootstrap。 */
main { font-size: 16px; line-height: 1.78; }
main h1 { font-size: clamp(1.9rem, 3.1vw, 2.35rem); line-height: 1.3; font-weight: 760; letter-spacing: -.025em; }
.profile .more-info, .profile .more-info p { font-size: .9rem; line-height: 1.7; }
.profile .more-info p { margin: .42rem 0; }
.fang-homepage {
  --fp-accent: var(--global-theme-color, #7952b3);
  --fp-border: var(--global-divider-color, #e5e7eb);
  --fp-text: var(--global-text-color, #252832);
  color: var(--fp-text); font-size: 1rem; line-height: 1.82;
}
.fang-homepage h2 {
  position: relative; margin: 2.45rem 0 1rem; padding-bottom: .58rem;
  border-bottom: 1px solid var(--fp-border); font-size: clamp(1.35rem, 2.1vw, 1.62rem);
  line-height: 1.42; font-weight: 760; letter-spacing: -.015em;
}
.fang-homepage h2::after { content: ""; position: absolute; left: 0; bottom: -1px; width: 2.8rem; height: 3px; border-radius: 8px; background: var(--fp-accent); }
.fang-homepage h3 { margin: 0 0 .45rem; font-size: 1.04rem; line-height: 1.55; font-weight: 740; }
.fang-homepage p { margin: .45rem 0; font-size: 1rem; line-height: 1.82; }
.fang-homepage .fp-intro { margin: .2rem 0 .85rem; font-size: 1.02rem; line-height: 1.9; }
/* The profile image floats beside the intro in al-folio's about layout. Clear it before Education. */
.fang-homepage h2.fp-clear { clear: both; margin-top: 2.35rem; padding-top: .2rem; }
.fang-homepage .fp-muted { color: var(--global-text-color-light, #6b7280); font-size: .9rem; }
.fang-homepage .fp-timeline { position: relative; margin: .5rem 0 .25rem .42rem; padding-left: 1.45rem; border-left: 2px solid var(--fp-border); }
.fang-homepage .fp-item { position: relative; margin: 0 0 1.1rem; animation: fp-rise-in 580ms cubic-bezier(.2,.7,.2,1) both; animation-delay: var(--fp-delay, 0ms); }
.fang-homepage .fp-item:last-child { margin-bottom: .2rem; }
.fang-homepage .fp-item::before { content: ""; position: absolute; left: calc(-1.45rem - 6px); top: .32rem; width: 10px; height: 10px; border: 3px solid var(--global-bg-color, #fff); border-radius: 50%; background: var(--fp-accent); box-shadow: 0 0 0 2px color-mix(in srgb, var(--fp-accent) 22%, transparent); transition: transform 180ms ease, box-shadow 180ms ease; }
.fang-homepage .fp-item:hover::before { transform: scale(1.12); box-shadow: 0 0 0 5px color-mix(in srgb, var(--fp-accent) 10%, transparent); }
.fang-homepage .fp-date-row { display: block; margin: 0 0 .55rem; }
.fang-homepage .fp-date { display: inline-block; padding: .2rem .68rem; border: 1px solid color-mix(in srgb, var(--fp-accent) 24%, var(--fp-border)); border-radius: 999px; background: color-mix(in srgb, var(--fp-accent) 6%, transparent); color: var(--fp-accent); font-size: .82rem; line-height: 1.5; font-weight: 730; white-space: nowrap; }
.fang-homepage .fp-card { padding: .9rem 1.05rem; border: 1px solid var(--fp-border); border-radius: 12px; background: color-mix(in srgb, var(--global-bg-color, #fff) 97%, var(--fp-accent) 3%); transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease; }
.fang-homepage .fp-card:hover { transform: translateY(-2px); border-color: color-mix(in srgb, var(--fp-accent) 35%, var(--fp-border)); box-shadow: 0 6px 16px color-mix(in srgb, var(--fp-accent) 8%, transparent); }
.fang-homepage .fp-card-title { display: flex; flex-wrap: wrap; align-items: flex-start; gap: .35rem .55rem; margin: 0 0 .2rem; font-size: 1.02rem; line-height: 1.62; }
.fang-homepage .fp-tag { display: inline-block; padding: .1rem .48rem; border-radius: 6px; background: color-mix(in srgb, var(--fp-accent) 9%, transparent); color: var(--fp-accent); font-size: .77rem; line-height: 1.5; font-weight: 720; white-space: nowrap; }
.fang-homepage .fp-meta, .fang-homepage .fp-mentor { margin: .25rem 0 0; font-size: .92rem; line-height: 1.7; }
.fang-homepage .fp-meta { color: var(--global-text-color-light, #6b7280); }
.fang-homepage .fp-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .85rem; margin-top: .75rem; }
.fang-homepage .fp-research-card { height: 100%; padding: .95rem 1rem; animation: fp-rise-in 580ms cubic-bezier(.2,.7,.2,1) both; animation-delay: var(--fp-delay, 0ms); }
.fang-homepage .fp-research-heading { display: flex; align-items: flex-start; gap: .6rem; margin: 0 0 .35rem; font-size: 1rem; line-height: 1.55; font-weight: 740; }
.fang-homepage .fp-icon { display: inline-flex; align-items: center; justify-content: center; flex: 0 0 1.95rem; width: 1.95rem; height: 1.95rem; border-radius: 9px; background: color-mix(in srgb, var(--fp-accent) 10%, transparent); color: var(--fp-accent); }
.fang-homepage .fp-research-card p { margin: .25rem 0 0; font-size: .93rem; line-height: 1.72; }
.fang-homepage .fp-award-list { margin: .4rem 0 0; padding-left: 1.2rem; }
.fang-homepage .fp-award-list li { margin: .25rem 0; font-size: .92rem; line-height: 1.7; }
.fang-homepage .fp-links { display: flex; flex-wrap: wrap; gap: .55rem; margin-top: .6rem; }
.fang-homepage a.fp-button { display: inline-flex; align-items: center; gap: .4rem; padding: .4rem .72rem; border: 1px solid color-mix(in srgb, var(--fp-accent) 30%, var(--fp-border)); border-radius: 8px; color: var(--fp-accent); font-size: .87rem; font-weight: 680; text-decoration: none; transition: background 160ms ease, transform 160ms ease; }
.fang-homepage a.fp-button:hover { background: color-mix(in srgb, var(--fp-accent) 7%, transparent); text-decoration: none; transform: translateY(-1px); }
@keyframes fp-rise-in { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
@media (max-width: 640px) {
  main { font-size: 15.5px; }
  .fang-homepage h2 { margin-top: 2.05rem; }
  .fang-homepage h2.fp-clear { margin-top: 2rem; }
  .fang-homepage .fp-grid { grid-template-columns: minmax(0, 1fr); }
  .fang-homepage .fp-card { padding: .82rem .9rem; }
  .fang-homepage .fp-date { white-space: normal; }
}
@media (prefers-reduced-motion: reduce) {
  .fang-homepage .fp-item, .fang-homepage .fp-research-card { animation: none; }
  .fang-homepage .fp-card, .fang-homepage .fp-item::before, .fang-homepage a.fp-button { transition: none; }
}
</style>

<div class="fang-homepage">

<h2>关于我</h2>
<p class="fp-intro">彭芳，现任华南农业大学数学与信息学院软件学院首聘副教授，博士毕业于中国科学院自动化研究所。研究方向包括<strong>多模态大模型的后训练与推理增强、视觉语言预训练模型的小样本适配与迁移，以及空间智能与多模态场景理解</strong>。关注少样本条件下的细粒度视觉语义建模、视觉信息高效利用与多模态模型推理能力提升。</p>

<h2 class="fp-clear">教育背景</h2>
<div class="fp-timeline">
  <article class="fp-item" style="--fp-delay: 0ms">
    <div class="fp-date-row"><span class="fp-date">2021.09 — 2026.01</span></div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>中国科学院自动化研究所 · 模式识别与智能系统</strong><span class="fp-tag">博士</span></div>
      <p class="fp-mentor">导师：徐常胜研究员（国家杰青、万人计划领军人才、IEEE Fellow）</p>
    </div>
  </article>
  <article class="fp-item" style="--fp-delay: 80ms">
    <div class="fp-date-row"><span class="fp-date">2017.09 — 2020.01</span></div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>中国农业大学 · 计算机科学与技术</strong><span class="fp-tag">硕士</span></div>
      <p class="fp-mentor">导师：李振波教授</p>
    </div>
  </article>
  <article class="fp-item" style="--fp-delay: 160ms">
    <div class="fp-date-row"><span class="fp-date">2013.09 — 2017.06</span></div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>中国农业大学 · 能源与动力工程、计算机科学与技术</strong><span class="fp-tag">双学位学士</span></div>
    </div>
  </article>
</div>

<h2>工作经历</h2>
<div class="fp-timeline">
  <article class="fp-item" style="--fp-delay: 0ms">
    <div class="fp-date-row"><span class="fp-date">2026.09 — 至今</span></div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>华南农业大学</strong><span class="fp-tag">首聘副教授</span></div>
      <p class="fp-meta">数学与信息学院软件学院</p>
      <p class="fp-mentor">从事计算机与人工智能相关教学和科研工作。</p>
    </div>
  </article>
  <article class="fp-item" style="--fp-delay: 80ms">
    <div class="fp-date-row"><span class="fp-date">2020.04 — 2021.08</span></div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>鹏城国家实验室</strong><span class="fp-tag">大语言模型算法研发</span></div>
      <p class="fp-mentor">参与盘古 Alpha 大语言模型相关研发工作。</p>
    </div>
  </article>
  <article class="fp-item" style="--fp-delay: 160ms">
    <div class="fp-date-row"><span class="fp-date">2017.07 — 2017.09</span></div>
    <div class="fp-card">
      <div class="fp-card-title"><strong>小米科技</strong><span class="fp-tag">实习生</span></div>
      <p class="fp-meta">人工智能云平台</p>
    </div>
  </article>
</div>

<h2>研究方向</h2>
<div class="fp-grid">
  <article class="fp-card fp-research-card" style="--fp-delay: 0ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-brain" aria-hidden="true"></i></span>多模态大模型的后训练与推理增强</div>
    <p>探索小样本与细粒度视觉识别、视觉信息冗余精简，以及多模态大语言模型内在视觉能力的激发。</p>
  </article>
  <article class="fp-card fp-research-card" style="--fp-delay: 70ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-layer-group" aria-hidden="true"></i></span>视觉语言预训练模型的小样本适配与迁移</div>
    <p>研究通用预训练知识向下游任务与交叉任务的泛化迁移，提升少样本条件下的适配效率与泛化能力。</p>
  </article>
  <article class="fp-card fp-research-card" style="--fp-delay: 140ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-cubes" aria-hidden="true"></i></span>空间智能与多模态场景理解</div>
    <p>关注视觉空间关系、场景结构理解与多模态推理方法。</p>
  </article>
</div>

<h2>主持项目与获奖荣誉</h2>
<div class="fp-grid">
  <section class="fp-card fp-research-card" style="--fp-delay: 0ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-file-signature" aria-hidden="true"></i></span>主持项目</div>
    <p><strong>国家自然科学基金青年科学基金项目 1 项</strong></p>
    <p class="fp-muted">项目名称与批准年度可在后续取得正式信息后补充。</p>
  </section>
  <section class="fp-card fp-research-card" style="--fp-delay: 70ms">
    <div class="fp-research-heading"><span class="fp-icon"><i class="fa-solid fa-award" aria-hidden="true"></i></span>获奖荣誉</div>
    <ul class="fp-award-list">
      <li>2023｜鹏城实验室优秀博士生</li>
      <li>2024｜中国科学院大学三好学生</li>
      <li>2016｜美国大学生数学建模竞赛 H 奖</li>
      <li>2016｜全国大学生物理竞赛二等奖</li>
    </ul>
  </section>
</div>

<p class="fp-muted" style="margin-top:1.2rem">代表性论文、研究简介及 DOI / 代码链接见 <a href="{{ '/publications/' | relative_url }}">学术成果</a> 页面。</p>

</div>
