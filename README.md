# Zotero AI Butler — Codex 适配版（非官方）

基于 [Zotero AI Butler](https://github.com/steven-jianhao-li/zotero-AI-Butler) 的非官方修改版本，旨在通过本地桥接服务接入 ChatGPT/Codex 登录能力，辅助 Zotero 文献阅读与分析。本仓库不属于上游项目的官方发布渠道。

> **发布状态：已公开发布 Beta 预发布版** [v5.1.2-beta.1.codex.1](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/tag/v5.1.2-beta.1.codex.1)。本版本尚未完成跨设备安装测试、完整源码归档审查与可复现构建验证，请将其视为测试版。

## 下载

| 文件 | 用途 | 下载 |
| --- | --- | --- |
| `AI-Butler-Codex-fixed.xpi` | Zotero 插件安装包（约 4.78 MB） | [下载 XPI](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/AI-Butler-Codex-fixed.xpi) |
| `zotero-codex-bridge-source.zip` | Codex 本地桥接服务源码（约 27 KB） | [下载桥接源码](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/zotero-codex-bridge-source.zip) |
| `zotero-ai-butler-codex-source-v5.1.2-beta.1.codex.1.zip` | 修改版插件源码归档（约 113 MB） | [下载插件源码](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/zotero-ai-butler-codex-source-v5.1.2-beta.1.codex.1.zip) |

**重要：** XPI 只安装 Zotero 插件，**不包含**必须另外运行的 Codex 本地桥接服务。GitHub 自动提供的 `Source code (zip/tar.gz)` 是当前仓库的源码快照，不等同于上表单独上传的插件源码归档。

## 安装概览

1. 备份 Zotero 数据，从上述 Release 下载并安装 `AI-Butler-Codex-fixed.xpi`（Zotero「工具」→「插件」）。
2. 下载桥接服务源码，检查来源与文件内容后解压，按 [安装与配置指南](docs/INSTALLATION.md) 启动本地服务。
3. 在插件中选择 Codex，配置本机桥接地址、私有配对令牌，并按提示使用可信的账号授权流程。
4. 检查登录状态、模型列表，进行纯文本连接测试。

## 版本与兼容性

- 发布标签：`v5.1.2-beta.1.codex.1`（Pre-release）
- Zotero 兼容范围：安装包清单声明 7.0.0–10.x；**尚未逐版本验证**
- 默认桥接地址：`http://127.0.0.1:23119`；实际端口以本地服务配置为准
- 安装包已去除指向上游原版的自动更新地址；处理方法见 [脚本](scripts/strip_upstream_update.py)，**尚需实际安装及更新行为测试**

## 完整性校验（SHA-256）

| 文件 | SHA-256 |
| --- | --- |
| XPI 安装包 | `dc4377ca4c5babeb168ff4959187b65832184a2a8d4e1c18a92b3c274c94a0a5` |
| 插件源码 ZIP | `665360447c1997746efc7f52b797f01729f68338fd6c935fb29c8b9f140b2666` |
| 桥接服务源码 ZIP | `ac47d8506d82feda83643023b53260c4758a9622e0a7af01de1788d73f661d09` |

以上校验值来自本版本 GitHub Release 的附件记录；可用于核对下载文件，**不能代替代码安全审计**。

## 项目文档

- [安装与本地桥接配置](docs/INSTALLATION.md)
- [当前版本发布说明](RELEASE_NOTES.md)
- [维护者发布与安全核对清单](docs/PUBLISHING.md)

## 开源与安全

原项目采用 [GNU AGPL-3.0](LICENSE)。本仓库已随 Release 提供修改版插件源码和桥接服务源码两个归档，但**尚未独立核查其完整性、对应关系、构建可复现性及是否包含敏感信息**。分发修改版应保留相应版权、许可、修改说明和对应完整源码。

不要在 Issue、仓库文件或截图中公开 OAuth 凭证、API Key、配对令牌、ChatGPT 登录信息或私人文献。此项目不提供 ChatGPT/Codex 使用额度，也不保证全部账号或环境可用。

**非官方社区修改版，不代表上游作者认可或维护。**
