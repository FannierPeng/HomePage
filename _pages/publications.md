---
layout: page
title: 学术成果
permalink: /publications/
description: 彭芳的代表性研究工作与学术论文。
nav: true
nav_order: 2
---

<style>
main { font-size: 16px; line-height: 1.78; }
main h1 { font-size: clamp(1.85rem, 3vw, 2.25rem); line-height: 1.3; font-weight: 760; letter-spacing: -.02em; }
main h2 { margin-top: 2.2rem; margin-bottom: .95rem; padding-bottom: .55rem; border-bottom: 1px solid var(--global-divider-color, #e5e7eb); font-size: clamp(1.32rem, 2.05vw, 1.58rem); line-height: 1.42; font-weight: 740; }
.fang-publications { font-size: 1rem; line-height: 1.8; }
.fang-publications .pub-intro { margin: .4rem 0 1rem; font-size: 1rem; }
.fang-publications .pub-note { padding: .8rem 1rem; margin: 1rem 0 1.4rem; border-left: 3px solid var(--global-theme-color, #7952b3); border-radius: 0 8px 8px 0; background: color-mix(in srgb, var(--global-theme-color, #7952b3) 5%, transparent); font-size: .92rem; }
.fang-publications .publications { margin-top: .7rem; }
@media (max-width: 640px) { main { font-size: 15.5px; } }
</style>

<div class="fang-publications">

<p class="pub-intro">本页汇总代表性研究工作与论文成果。核心论文条目附有研究简介；可使用条目下方的 <em>Abs</em> 查看摘要，通过 <em>DOI</em>、<em>Code</em> 等链接访问论文原文或代码仓库。</p>

<div class="pub-note">研究工作简介已整理至对应论文条目中，不再单设“科研经历”页面。论文信息以正式出版记录为准，后续可继续补充 PDF、代码和项目主页链接。</div>

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>

</div>
