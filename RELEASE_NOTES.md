# v5.1.2-beta.1.codex.1 — 预发布说明（草稿）

**此文件是发布说明草稿，仓库尚未发布可下载的 GitHub Release。**

Zotero AI Butler 的非官方 Codex 适配版。

## 主要信息

- 插件清单版本：`5.1.2-beta.1.codex.1`
- 包含 Codex 接口及登录相关逻辑，依赖本地 Codex 适配服务；插件安装包本身**不包含**适配服务。
- 本地服务默认地址：`http://127.0.0.1:23119`
- 清单声明支持 Zotero 7.0.0 至 10.x，尚未完成跨设备验证。
- 清单保留原项目的自动更新地址，可能造成后续更新覆盖本修改版，公开发布前应解决。

## 安装方式（正式发布后）

从本仓库 Releases 下载 `zotero-ai-butler-codex-5.1.2-beta.1.codex.1.xpi`，使用 Zotero「工具」→「插件」安装。使用 Codex 功能前需安装可信的兼容本地适配服务并完成授权。

## 安装包 SHA-256

```text
8a46fdf676aa7d4c573fd1a0baded4811074718a229081ccc2267a90c8f90cdb
```

## 版权与源码

本项目基于 [steven-jianhao-li/zotero-AI-Butler](https://github.com/steven-jianhao-li/zotero-AI-Butler) 修改，原项目依据 AGPL-3.0 许可。**公开分发修改版安装包前，请先提供该修改版的完整对应源代码、构建所需文件、原版权许可声明及修改说明。**

请勿提交私有 API Key、OAuth 凭证、个人授权记录。非官方发布，不代表原作者认可或维护。
