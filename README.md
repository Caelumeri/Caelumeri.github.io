# 曹博文 · 学术主页（部署版）

- 源文件：`C:\Users\Arubav\Downloads\曹博文_Bowen_Cao_个人主页_ORCID最终版.html`（2026-10-16 20:09）
- 本目录 = 清理过的可部署版本，2026-11-03 处理
- 首次提交：`e502b95`

## 本版改了什么

1. 删除全部邮箱与 vCard——联系区只留 ORCID 与学院页面入口（明文 `mailto:` 会被爬虫直接抓）
2. 删除 Cloudflare `email-decode` 脚本与 `cloudflareinsights` 埋点
3. 补 `og:` / `twitter:` meta、favicon（内联 SVG）、JSON-LD `Person`
4. 正文内容一字未改

## 本地预览

直接双击 `index.html` 即可。语言切换、暗色、筛选、复制 DOI 都可用。

或起本地服务：

```bash
python -m http.server 8080
# 浏览器打开 http://localhost:8080/
```

## 部署到 GitHub Pages（约 10 分钟）

1. 注册 / 登录 GitHub。
2. 新建仓库，**仓库名必须是 `<你的用户名>.github.io`**（否则会变成子路径，主页要改链接）。
3. 在本目录执行：

```bash
git remote add origin https://github.com/<用户名>/<用户名>.github.io.git
git branch -M main
git push -u origin main
```

4. 等 1–2 分钟，访问 `https://<用户名>.github.io/`。
5. 若 404：仓库 Settings → Pages，确认 Source 是 `main` / `(root)`。

## 部署后待补

- `<link rel="canonical">` 与 `og:url`：拿到最终 URL 后加到 `<head>`（现在故意没写，避免写错地址）
- `og:image`：有正式照片再加
- 自定义域名：仓库 Settings → Pages → Custom domain（域名要另买，几十元/年；国内访问要快就得备案）

## 以后更新论文

改 `index.html` 里的 publications 区块，然后：

```bash
git add -A
git commit -m "update: 论文列表"
git push
```

## 隐私处理

- 页面不公开任何邮箱地址（2026-11-03 决定）：联系方式只走 ORCID 与学院页面。
- 以后若要加回邮箱，别用明文 `mailto:`——写成 `name [at] domain` 或走表单。

## 已知可选项

- 不想被搜索引擎收录：`<head>` 加 `<meta name="robots" content="noindex">`，只把链接发给特定的人。
- 想加快国内访问：换国内云 OSS + 自有域名 + ICP 备案，不再是纯免费。

## 首屏结构图

首屏右侧是**士的宁（strychnine）**的二维骨架式，不是抽象装饰：

- 结构来自 PubChem CID 441071 的 IsomericSMILES，由 RDKit 生成（脚本 `tools/make_structure.py`），分子式 C21H22N2O2。没有手绘、拼贴或生成式图像参与。
- 它只作构图与审美示意，**不代表本人研究对象或成果**。图注写 `REFERENCE ONLY`，`aria-label` 也标了中文说明。
- 线条与原子标签用 CSS 变量 `--mol-c` / `--mol-n` / `--mol-o` 着色，深色模式自动换色；装饰圆环由 `--line` / `--muted` 驱动。
- 换分子：改 `tools/make_structure.py` 里的 `SMILES` 重跑，把输出替换进 `index.html` 的 `<g class="mol-structure">` 内。
