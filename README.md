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