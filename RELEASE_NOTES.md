# Zotero AI Butler Codex 适配版 v5.1.2-beta.1.codex.1

**发布状态：** [GitHub Pre-release 已公开发布](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/tag/v5.1.2-beta.1.codex.1)（Beta 测试版）。

这是基于 [Zotero AI Butler](https://github.com/steven-jianhao-li/zotero-AI-Butler) 的非官方 Codex 适配版本。

## 功能与说明

- 通过本机桥接服务连接 ChatGPT/Codex，提供 Codex 登录状态检查、模型列表获取和纯文本连接测试等功能。
- 保留上游 Zotero AI Butler 的文献阅读与辅助分析功能。
- 本版 XPI 移除了原项目的自动更新地址，以降低被上游版本覆盖的风险；尚未完成实际更新行为测试。
- 本 XPI **不包含本地桥接服务**，使用 Codex 功能须单独安装并运行。

## 发布附件

| 文件 | 用途 |
| --- | --- |
| [AI-Butler-Codex-fixed.xpi](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/AI-Butler-Codex-fixed.xpi) | 插件安装包 |
| [zotero-ai-butler-codex-source-v5.1.2-beta.1.codex.1.zip](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/zotero-ai-butler-codex-source-v5.1.2-beta.1.codex.1.zip) | 修改版插件源码归档 |
| [zotero-codex-bridge-source.zip](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/zotero-codex-bridge-source.zip) | 配套桥接服务源码归档 |

## 安装和兼容性

从 Release 下载 XPI，在 Zotero「工具」→「插件」中安装。按 [安装指南](docs/INSTALLATION.md) 获取并启动可信的桥接服务、完成登录与连接测试。

安装包清单声明适配 Zotero 7.0.0–10.x；尚未完成跨设备、跨版本验证。使用前建议备份 Zotero 数据。

## SHA-256

```text
AI-Butler-Codex-fixed.xpi
dc4377ca4c5babeb168ff4959187b65832184a2a8d4e1c18a92b3c274c94a0a5

zotero-ai-butler-codex-source-v5.1.2-beta.1.codex.1.zip
665360447c1997746efc7f52b797f01729f68338fd6c935fb29c8b9f140b2666

zotero-codex-bridge-source.zip
ac47d8506d82feda83643023b53260c4758a9622e0a7af01de1788d73f661d09
```

## 已知待核查事项

- 完整检查两个源码归档内的文件、凭证及第三方依赖；核实与 XPI 的源码对应关系以及可复现构建。
- 在干净的 Zotero 安装环境中测试 XPI、桥接服务、模型连接、更新行为。
- 以上文件已在 GitHub 提供下载，不等于已通过代码安全审计。

## 开源与免责声明

本修改版本应遵循上游项目 [AGPL-3.0](LICENSE) 及桥接服务可能涉及的其他许可证要求。请勿向公共仓库提交 API Key、OAuth 凭证或配对令牌。非官方修改版，上游作者不承担本修改版的维护责任。
