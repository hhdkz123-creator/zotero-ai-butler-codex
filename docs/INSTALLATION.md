# 安装与配置指南（Beta 预发布版）

> 当前版本 [v5.1.2-beta.1.codex.1](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/tag/v5.1.2-beta.1.codex.1) **已公开发布**，但尚未完成跨设备完整安装测试。请先备份 Zotero 数据，核查下载的源码与软件安全性。本项目为非官方修改版。

## 下载文件

| 文件 | 作用 | 下载 |
| --- | --- | --- |
| `AI-Butler-Codex-fixed.xpi` | Zotero 插件 | [下载 XPI](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/AI-Butler-Codex-fixed.xpi) |
| `zotero-codex-bridge-source.zip` | 运行 Codex 功能所需本地桥接服务的源码 | [下载桥接源码](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/zotero-codex-bridge-source.zip) |
| `zotero-ai-butler-codex-source-v5.1.2-beta.1.codex.1.zip` | 修改版插件源码归档，不用于日常安装 | [下载插件源码](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/download/v5.1.2-beta.1.codex.1/zotero-ai-butler-codex-source-v5.1.2-beta.1.codex.1.zip) |

> GitHub 自动生成的 `Source code (zip)`、`Source code (tar.gz)` 仅包含仓库当前标签的文件，不是上表中单独上传的完整插件源码归档。XPI 本身也**不包含**桥接服务。

## 运行环境

- Zotero：插件清单声明支持 7.0.0–10.x，但未对所有版本进行验证。
- 操作系统：文档以下以 macOS 为例；其他平台需要分别测试。
- Node.js：本地桥接服务需要 Node.js，具体所需版本和依赖以桥接源码内的说明或 `package.json` 为准。
- ChatGPT/Codex 账号：需自行具备可用权限和额度，本项目不提供订阅及 API 额度。

## 安装 Zotero 插件

1. 先备份 Zotero 数据及配置。
2. 下载 `AI-Butler-Codex-fixed.xpi`。不要将其误认为 ZIP 源码包。
3. 打开 Zotero，进入「工具」→「插件」，把 XPI 文件拖进插件窗口并确认安装；如有提示则重启。
4. 插件显示正常后，再配置本地 Codex 桥接服务。

## 检查并启动本地桥接服务（macOS）

1. 下载 `zotero-codex-bridge-source.zip`，解压至自己选择的目录。
2. **运行前检查**解压内容和可能包含的依赖安装脚本。不要执行不明来源的命令，也不要分享个人密钥或令牌。
3. 在终端进入实际包含 `server.mjs` 的目录；如果解压后有多层文件夹，需要进入相应内层目录。
4. 查看源码提供的运行要求；如果 `server.mjs` 可直接运行，可执行：

```bash
node server.mjs
```

是否需要先运行 `npm install`、是否需要特定环境变量，以**实际源码的依赖清单和说明**为准；当前归档尚未经独立复核，不应假定无需其他配置。

此前适配版使用的默认本地地址为 `http://127.0.0.1:23119`。可用以下命令检查 macOS 上是否有服务监听该端口：

```bash
lsof -nP -iTCP:23119 -sTCP:LISTEN
```

如果服务使用了其他端口，应在 Zotero 插件设置里同步修改。桥接服务应限制在本机环回地址，切勿向公网暴露授权服务。

## 配对与 Codex 登录

1. 打开 Zotero AI Butler 设置，选择 Codex 供应商。
2. 将服务地址设置为 `http://127.0.0.1:23119`，或实际监听的本机地址和端口。
3. 按桥接服务的本地说明获取当前实例的配对令牌，在插件中填写；**令牌只保留在本地**。
4. 检查登录状态，并仅在可信的官方 ChatGPT/OpenAI 授权页面完成账号授权。
5. 获取模型列表，选择可用模型后执行纯文本连接测试，确认服务正常后再处理实际文献。

## 常见问题

- **无法连接**：先检查桥接服务是否仍在运行，确认地址、端口和防火墙设置一致。
- **提示配对失败**：核对插件中输入的配对令牌是否对应当前桥接实例；不要在 Issue 或截图中展示真实令牌。
- **登录状态异常 / 模型列表为空**：确认账号权限、官方授权状态、可用额度和本地服务日志；分享日志前先删除私人信息。
- **安装后功能未显示**：重启 Zotero，核对插件版本；如需排错，请只提供经过脱敏的错误信息。
- **自动更新**：当前发布的 XPI 已移除上游的 `update_url`，见 [处理脚本](../scripts/strip_upstream_update.py)。但尚未完成 Zotero 内的自动更新行为实测。

## 校验与风险说明

发布 XPI 的 SHA-256：

```text
dc4377ca4c5babeb168ff4959187b65832184a2a8d4e1c18a92b3c274c94a0a5
```

在 macOS 中可运行 `shasum -a 256 文件路径` 对下载文件计算哈希。哈希匹配只能确认文件与该 Release 附件一致，**不能证明软件安全**。

本仓库已提供两个源码 ZIP，但尚未对其内容、依赖、敏感信息以及与本版 XPI 的可复现关系完成审核。详见 [维护者发布核对清单](PUBLISHING.md)。
