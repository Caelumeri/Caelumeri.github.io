# 曹博文 · 学术主页（部署版）

- 线上：https://caelumeri.github.io/
- 仓库：https://github.com/Caelumeri/Caelumeri.github.io
- 当前版本：2026-11-12，源自 `C:\Users\Arubav\Downloads\index.html`（134752 bytes）

## 版本历史

- **2026-11-12**：换用新版页面（TF3 分子板、Marginalia 版块、研究实践、双语），补齐 canonical / OG / Twitter / JSON-LD / favicon，`description` 去掉「设计原型」。
- **2026-11-03**：首版上线；撤除全部邮箱与 vCard；首屏改为士的宁结构（新版已替换）。

## 本版要点

1. 单文件 HTML，6 个 section：`top` / `research` / `papers` / `journey` / `marginalia` / `contact`。
2. 首屏右侧是 **Theaflavin 3,3′-digallate（茶黄素-3,3′-双没食子酸酯，CHEBI:136608）** 的分子板，文字与色块呈现，不是结构式。
3. 邮箱不公开。页面内置 Cloudflare Turnstile + Worker 取邮箱的方案，`SECURE_EMAIL.siteKey` 与 `endpoint` 均留空，联系区按钮默认 `hidden`，不会发请求。
4. 论文 4 篇的题录与出版社元数据一致。
5. 无明文邮箱、无 Cloudflare 埋点、无外部字体或 CDN 依赖（Turnstile 只在配置了 siteKey 后动态加载）。

## 本地预览

直接双击 `index.html`。语言切换、暗色、论文筛选、复制 DOI 都可用。

或：

```bash
python -m http.server 8080
# http://localhost:8080/
```

## 部署

仓库名必须是 `Caelumeri.github.io`，Pages 从 `main` / `(root)` 发布。

```bash
git add -A
git commit -m "update: 说明"
git push
```

推送后 Pages 会重建，通常 30–60 秒；浏览器有缓存时用 `Ctrl+F5`。

## 以后改内容

- 论文：改 `papers` 区块，4 篇的 DOI 链接保持 `https://doi.org/...`。
- 双语：所有可见文本走 `data-i18n`，改中文时同步 `en` 字典。
- 主题：`data-theme="light|dark"`，配色在 `:root` 与 `html[data-theme="dark"]`。

## 隐私处理

- 2026-11-03 决定：页面不公开任何邮箱地址。
- 如要恢复邮箱展示，走 Turnstile 方案（填 `siteKey` / `endpoint`），不要写明文 `mailto:`。

## 已弃用

- `tools/make_structure.py`：旧版首屏士的宁结构的生成脚本，当前版本不再使用，保留备查。
## 2026-11-24 新增：机器可读档案

站点根目录新增四个文件，给「别的 AI 来读」用，不是给人浏览的页面：

| 文件 | 内容 |
|---|---|
| `llms.txt` | 入口：一句话介绍 + 三个页面的链接 + 「怎么跟他说话」+ 边界 |
| `research.md` | 研究方向陈述（三项兴趣、研究方式、三层体系、近期目标） |
| `philosophy.md` | 哲学概念与命题：六个起点命题、附条件推论、四道推理边界、开放问题、署名分层 |
| `taste.md` | 审美与日常偏好摘要：材质、比例、颜色、气味、器物、空间 |

**`.nojekyll` 是必需品**：GitHub Pages 默认用 Jekyll 构建，会把 `.md` 编译成 `.html`，导致 `/research.md` 404。加了空文件 `.nojekyll` 后，`.md` 原样输出，Content-Type 为 `text/markdown`。

`taste.md` 只保留判断标准；肤况、体型、预算、室友、购物清单一律不进公开版。`philosophy.md` 只留概念，45 轮原始对话与情绪记录不外流。

**入口**：首页页脚有「给 AI 的公开资料 →」一行指向 `llms.txt`；`<head>` 里另有 `<link rel="alternate" type="text/plain" href="/llms.txt">`，供能解析该标签的工具发现。
