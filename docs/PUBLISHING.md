# 发布核对清单（维护者）

目标版本：`v5.1.2-beta.1.codex.1`。

## 先准备源码

XPI 内的 `content/scripts/aiButler.js` 是打包后的 JavaScript，虽然包含部分源文件路径注释，但**不能代替用于修改和重新构建的完整对应源代码**。请在本地开发目录找到本次 Codex 修改版的原始工程（含 `src/`、构建配置、依赖清单和锁文件），并核实其与准备发布的 XPI 对应。

同时查找 `zotero-codex-bridge` 本地服务的 `server.mjs`、依赖清单、构建/启动说明及必要源码。若桥接服务来源许可不同，应分别审查、保留其许可证。

不能将上游未经修改的源码假称为该 Codex 版本完整源码。

## 打包与秘密排查

- 排除 `node_modules/`、`.git/`、构建缓存、系统私有文件及非必要生成文件。
- 必须排除 `.env`、`auth.json`、`codex-bridge-pairing.txt`、OAuth 令牌、API Key、会话信息、个人论文、Zotero 数据目录、日志中的敏感内容。
- `.env.example` 仅在确认不含真实凭证后可保留。
- 将修改版插件源码及本地桥接源码分别保留为可重建的源码包，或提交到仓库中适当目录。
- 在发布说明中标记非官方修改、版权信息、AGPL-3.0 要求和构建步骤。

## 修正自动更新

当前 XPI 的 `manifest.json` 有以下上游更新入口：

```text
https://github.com/steven-jianhao-li/zotero-AI-Butler/releases/download/release/update.json
```

已准备 [构建后处理脚本](../scripts/strip_upstream_update.py) 从现有 XPI 中移除这个上游地址，候选文件名为 `zotero-ai-butler-codex-5.1.2-beta.1.codex.1-no-upstream-update.xpi`，SHA-256 为 `dc4377ca4c5babeb168ff4959187b65832184a2a8d4e1c18a92b3c274c94a0a5`。仍应核对修改版源码和该脚本能够重现候选 XPI，并在 Zotero 实测安装、更新行为。

## GitHub 发布

1. 确认已发布完整对应源代码、构建说明和所有相关许可证。
2. 打开 [Create a new release](../releases/new)。
3. 选择 `Choose a tag`，新建 `v5.1.2-beta.1.codex.1`，目标 `main`。
4. Title 填 `Zotero AI Butler Codex 适配版 v5.1.2-beta.1.codex.1`。
5. 将 `RELEASE_NOTES.md` 的内容复制到发布正文，并更新已完成事项。
6. 上传经校验、且通过安装测试的 `-no-upstream-update.xpi`、修改版插件完整源码归档（如未随仓库提交），以及可依法分发的桥接服务源码归档（若桥接服务不在仓库中）。
7. 勾选 `Set as a pre-release`，再选择 `Publish release`。
8. 打开公开的 Release 页面，实际下载安装并检查 SHA-256、插件能否运行、桥接服务及文档链接是否可用。

**在完整源码未核查、候选 XPI 未经实际安装测试之前，不建议公开发布。**
