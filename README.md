# 🚀 皎月连自动签到

> [!TIP]
> 如果你打算长期使用皎月连，建议订阅以支持原作者。

> [!WARNING]
> 本项目仅供娱乐。使用本项目带来的风险和后果由使用者自行承担。

本仓库 Fork 自 [doubletree6/Jiaoyuelian-autocheckin](https://github.com/doubletree6/Jiaoyuelian-autocheckin)，用于通过 GitHub Actions 自动完成 [natpierce.cn](https://www.natpierce.cn/) 签到，并通过 NotifyX 推送签到结果。

## 🔧 本 Fork 的改动

- 每日签到时间调整为北京时间 **12:16**。
- 将 `actions/checkout`、`actions/setup-node` 和 `actions/setup-python` 升级到 `v7`。
- 将签到结果推送服务从 PushPlus 切换为 NotifyX（码达），使用 NotifyX API 密钥和默认公众号渠道。

## ✨ 功能特性

- 🤖 全自动签到，无需手动操作
- 🔐 账号密码通过 GitHub Secrets 安全存储
- 🧩 自动识别并解决滑块验证码
- 📱 微信推送签到结果（通过 NotifyX 默认公众号渠道）
- ⏰ 每天计划于北京时间 12:16 自动触发

## 📋 准备工作

### 1. 准备 NotifyX API 密钥（用于微信推送）

1. 登录 [NotifyX（码达）](https://www.notifyx.cn/)
2. 确认默认推送渠道为公众号，并在平台生成或复制 API 密钥


### 2. Fork 本仓库

点击右上角 **Fork** 按钮，将仓库复制到你自己的账号下

## ⚙️ 配置步骤

### Step 1: 进入 Secrets 设置页面

1. 打开你 Fork 的仓库
2. 点击 **Settings**（设置）
3. 左侧菜单找到 **Secrets and variables** → **Actions**
4. 点击 **New repository secret** 按钮

### Step 2: 添加以下 3 个 Secrets

| 名称 | 值 | 说明 |
|------|-----|------|
| `NATPIERCE_USERNAME` | 你的手机号或邮箱 | 皎月连登录账号 |
| `NATPIERCE_PASSWORD` | 你的密码 |  |
| `NOTIFYX_API_KEY` | 你的 API 密钥 | 从 NotifyX 平台获取 |

**添加示例：**

```
Name: NATPIERCE_USERNAME
Secret: your_email@example.com

Name: NATPIERCE_PASSWORD  
Secret: YourPassword123.

Name: NOTIFYX_API_KEY
Secret: abc123def456ghi789
```

> [!NOTE]
> 如果你之前配置过 `PUSHPLUS_TOKEN`，请新增 `NOTIFYX_API_KEY`，并在仓库 **Settings → Secrets and variables → Actions** 中删除旧的 `PUSHPLUS_TOKEN`。

### Step 3: 启用 GitHub Actions

1. 进入仓库的 **Actions** 选项卡
2. 如果看到提示，点击 **I understand my workflows, go ahead and enable them**
3. 确认工作流已启用

## ▶️ 运行方式

### 方式一：手动触发

1. 进入 **Actions** 选项卡
2. 左侧选择 **Daily NatPierce Check-in**
3. 点击右侧 **Run workflow** → **Run workflow**
4. 等待运行完成，查看日志确认结果

### 方式二：定时自动运行

工作流计划在每天 **UTC 04:16**（北京时间 **12:16**）触发。

> [!NOTE]
> `schedule` 设定的是计划触发时间，GitHub Actions 不保证准点启动。负载较高时（例如整点），工作流可能明显延迟，延迟时长不固定；极端情况下，排队中的任务也可能被丢弃。详见 [GitHub 关于定时工作流延迟的说明](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows#scheduled-workflows-running-at-unexpected-times)。

如果需要修改时间，编辑 `.github/workflows/daily-checkin.yml` 中的 cron 表达式：

```yaml
schedule:
  - cron: '16 4 * * *'  # UTC 时间，北京时间需要 +8 小时
```

**常用时间对照表：**

| 北京时间 | cron 表达式 |
|---------|-------------|
| 08:00 | `0 0 * * *` |
| 10:00 | `0 2 * * *` |
| 12:16 | `16 4 * * *` |
| 20:00 | `0 12 * * *` |

## 📱 推送效果

签到完成后，你会在微信收到推送通知：

```
皎月连签到：签到成功！
下次可签到时间: 2026-03-17 10:00:00
```

## 🔧 常见问题

### Q: 签到失败怎么办？

1. 检查 Secrets 中的账号密码是否正确
2. 进入 Actions 查看运行日志，了解具体错误
3. 确认皎月连服务未到期

### Q: 没有收到微信推送？

1. 确认 NotifyX 默认推送渠道已配置为公众号
2. 检查仓库 Secret `NOTIFYX_API_KEY` 是否存在且填写正确
3. 查看 GitHub Actions 运行日志中的推送接口响应

### Q: 如何关闭自动签到？

进入 Actions → Daily NatPierce Check-in → 右侧 **⋯** → **Disable workflow**

或者直接删除仓库

### Q: 账号密码安全吗？

- 账号密码存储在 GitHub Secrets 中
- 代码中不会硬编码任何敏感信息
- 建议定期更换密码

## 📄 项目结构

```
.
├── .github/workflows/
│   └── daily-checkin.yml   # 每日签到工作流
├── checkin.js              # 签到主脚本
├── solve_slider.py         # 滑块验证码求解器
├── push_notification.py    # NotifyX 推送脚本
└── README.md
```

## 📜 开源协议

MIT License

---

⭐ 如果这个项目对你有帮助，欢迎 Star！
