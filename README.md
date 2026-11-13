# Zotero AI Butler — Codex 适配版（非官方）

这是 [Zotero AI Butler](https://github.com/steven-jianhao-li/zotero-AI-Butler) 的**非官方修改版本**，旨在通过本地适配服务接入 Codex/ChatGPT 登录能力，辅助 Zotero 文献阅读与分析。本仓库不属于原作者的官方发布渠道。

> **当前状态：准备发布。** 对应修改版完整源代码和本地适配服务尚未在本仓库提供；正式发布前需要补齐。请勿将仓库地址误认为已经提供可下载、可独立运行的完整版本。

## 文档

- [安装与 Codex 本地桥接配置](docs/INSTALLATION.md)
- [维护者发布清单：源码、敏感信息与 XPI 更新配置](docs/PUBLISHING.md)
- [预发布说明草稿](RELEASE_NOTES.md)

## 版本信息

- 插件版本：`5.1.2-beta.1.codex.1`
- 拟发布文件：`zotero-ai-butler-codex-5.1.2-beta.1.codex.1-no-upstream-update.xpi`
- 插件清单所声明的 Zotero 版本：7.0.0 至 10.x
- 默认本地适配服务地址：`http://127.0.0.1:23119`
- 原项目：[steven-jianhao-li/zotero-AI-Butler](https://github.com/steven-jianhao-li/zotero-AI-Butler)
- 原项目许可证：GNU AGPL-3.0

## 安装与使用（发布完成后）

1. 从 [Releases](../../releases) 下载 `.xpi` 安装包。
2. 在 Zotero 中打开「工具」→「插件」，将 XPI 拖入插件窗口并确认安装；如有提示，请重启 Zotero。
3. 如需使用 Codex 功能，还须**另外安装并运行与该版本匹配的本地 Codex 适配服务**。本 XPI **不包含**适配服务。
4. 依照可信适配服务的安装说明进行 ChatGPT/Codex 登录授权，再配置插件。注意不同账号/计划的功能和额度可能不同。

尚未完成跨设备兼容性验证。安装前建议备份 Zotero 数据库及配置，核查代码与适配服务来源。

## 完整性校验

计划发布文件的 SHA-256：

```text
dc4377ca4c5babeb168ff4959187b65832184a2a8d4e1c18a92b3c274c94a0a5
```

## 重要注意事项

- 原始测试 XPI 指向**原项目的自动更新地址**，可能造成覆盖。准备发布的候选安装包已移除该入口；后处理过程见 [scripts/strip_upstream_update.py](scripts/strip_upstream_update.py)。该候选包尚待安装实测，发布前应确认源码与构建过程可复现。
- 本仓库不提供 OpenAI API 额度，也不保证 ChatGPT/Codex 订阅登录能力在所有环境中持续可用。
- 不应在仓库中提交 API 密钥、OAuth 凭证、访问令牌、个人文献或本地授权配置。

## 许可证与源代码

原项目采用 [GNU AGPL-3.0](LICENSE)。分发此修改版本时须保留版权和许可声明，明确修改之处，并依据许可证提供**本修改版对应的完整源代码及构建所需文件**。仅链接到上游仓库或仅上传 XPI 安装包不构成充分的源码提供。完整修改版源码尚未就绪，暂不发布二进制文件。

## 免责声明

非官方社区修改版本，不代表原作者认可或提供维护。使用者应自行核验运行环境、网络连接和数据处理方式。
