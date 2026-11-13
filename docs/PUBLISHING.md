# 维护者发布与安全核对清单

目标版本：[v5.1.2-beta.1.codex.1](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/tag/v5.1.2-beta.1.codex.1)。

## 当前发布事实

- [x] GitHub 仓库已公开。
- [x] 已以 **Pre-release** 形式发布 `v5.1.2-beta.1.codex.1`。
- [x] 已上传 `AI-Butler-Codex-fixed.xpi` 安装包。
- [x] 已上传修改版插件源码 ZIP 和桥接服务源码 ZIP；**上传完成不代表内容审核完成**。
- [x] GitHub 已提供三个附件的 SHA-256 校验值。
- [x] 已从发布的 XPI 清单中移除原项目自动更新 URL。
- [ ] 逐文件审核两个源码 ZIP，排查密钥、配对令牌、个人数据和不需要的依赖/缓存。
- [ ] 核查修改版插件源码确实是本版 XPI 的完整对应源码，包含可用构建配置、依赖清单与必要许可证。
- [ ] 核查桥接服务源码、启动依赖、许可证及公开分发所需说明。
- [ ] 在干净环境重建 XPI，复现或解释与发布包的差异。
- [ ] 在 Zotero 中验证修正版安装、Codex 连接、授权流程、模型列表以及自动更新行为。
- [ ] 检查安装说明能否在新 macOS 环境独立走通，并补充已证实的 Node.js 版本和依赖安装步骤。

## 发布附件与校验值

| 文件 | SHA-256 |
| --- | --- |
| `AI-Butler-Codex-fixed.xpi` | `dc4377ca4c5babeb168ff4959187b65832184a2a8d4e1c18a92b3c274c94a0a5` |
| `zotero-ai-butler-codex-source-v5.1.2-beta.1.codex.1.zip` | `665360447c1997746efc7f52b797f01729f68338fd6c935fb29c8b9f140b2666` |
| `zotero-codex-bridge-source.zip` | `ac47d8506d82feda83643023b53260c4758a9622e0a7af01de1788d73f661d09` |

下载位置：[Release 页面](https://github.com/hhdkz123-creator/zotero-ai-butler-codex/releases/tag/v5.1.2-beta.1.codex.1)。

## 源码与敏感信息审查

XPI 内的 `content/scripts/aiButler.js` 是打包后的脚本，不能替代修改版本应提供的完整对应源码。应核验单独上传的插件源码 ZIP 是否包含可复现版本的 `src/`、构建脚本、依赖清单和锁文件，并核实具体改动与上游的关系。对于桥接服务，检查 `server.mjs` 及其所有运行依赖和必要源文件。

对两个压缩包逐项检查，排除以下不应公开的内容：

- `.env`、`auth.json`、`codex-bridge-pairing.txt`、账号缓存与 OAuth token；
- API Key、Cookie、会话凭证、个人论文、Zotero 数据、错误日志中的敏感数据；
- 不必要的 `node_modules/`、`.git/`、临时文件和构建缓存；
- 无法确认许可或来源的第三方内容。

macOS 可用以下命令列出压缩包文件清单，或计算 SHA-256。请先更换成实际本地文件路径：

```bash
unzip -l /path/to/source.zip
shasum -a 256 /path/to/source.zip
```

**重要：** 文件清单检查和哈希校验都不能替代敏感信息扫描、人工代码审查与许可证核查。当前两个 ZIP 的内部内容尚未完成独立审核。

## 自动更新处理

原始测试版 XPI 指向的上游更新地址是：

```text
https://github.com/steven-jianhao-li/zotero-AI-Butler/releases/download/release/update.json
```

已使用 [strip_upstream_update.py](../scripts/strip_upstream_update.py) 移除此 URL；当前 GitHub 附件 `AI-Butler-Codex-fixed.xpi` 的 SHA-256 为 `dc4377ca4c5babeb168ff4959187b65832184a2a8d4e1c18a92b3c274c94a0a5`。

该处理**并未建立自己的自动更新机制**，也尚未在 Zotero 中验证更新行为。后续正式发布应从源工程和打包配置层面固定更新策略，并编写可复现构建说明。

## 许可证与下一版本

上游 Zotero AI Butler 采用 [GNU AGPL-3.0](../LICENSE)。需保留原始版权及许可声明，明确修改内容，并依法向接收者提供完整对应源码、构建文件和必要说明。桥接服务还应独立核查其许可证及第三方依赖。

本版已经发布为 Beta，以上未完成事项应在后续修订版中优先处理。若发现公开文件中含有任何真实凭证，应及时撤销或轮换凭证；**仅删除 GitHub 文件不足以消除已经公开的密钥风险**。
