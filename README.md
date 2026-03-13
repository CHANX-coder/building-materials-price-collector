# 建筑材料价格自动收集系统

每天早上9点自动收集中国建筑材料的最新价格，整理后发送到你的邮箱。

## 功能特点

- **自动定时收集**：每天早上9点自动运行
- **多数据源**：整合我的钢铁网、1688等平台数据
- **分类整理**：钢材、板材、辅料分类展示
- **精美报告**：HTML格式邮件，支持手机/电脑查看
- **数据存档**：自动保存JSON和Excel格式数据
- **免费部署**：使用GitHub Actions，无需服务器

## 收集的材料类型

### 钢材类
- 螺纹钢 (HRB400/HRB500)
- 盘螺、高线
- 角钢、槽钢、工字钢
- H型钢

### 板材类
- 热轧板卷
- 冷轧板卷
- 中厚板
- 镀锌板
- 彩涂板

### 辅料类
- 电焊条、焊丝
- 防锈漆、防火涂料
- 膨胀螺栓、钻尾螺丝
- 结构胶、玻璃胶

## 配置说明

### 必需的GitHub Secrets

在仓库的 **Settings → Secrets and variables → Actions** 中添加：

| Secret名称 | 说明 |
|-----------|------|
| `EMAIL_USERNAME` | 发件邮箱（如QQ邮箱） |
| `EMAIL_PASSWORD` | 邮箱SMTP授权码 |
| `RECIPIENT_EMAIL` | 收件邮箱（如234497541@qq.com） |

### 获取QQ邮箱授权码

1. 登录QQ邮箱网页版
2. 点击「设置」→「账户」
3. 找到「POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务」
4. 开启「SMTP服务」，获取授权码

## 手动运行

在GitHub仓库页面：
1. 点击 **Actions** 标签
2. 选择 **每日建筑材料价格收集**
3. 点击 **Run workflow** 手动运行

## 自动运行

配置完成后，系统会每天早上9点（北京时间）自动运行，并将报告发送到指定邮箱。

## 项目结构

```
.
├── .github/workflows/          # GitHub Actions配置
│   └── daily_price_collection.yml
├── scraper/                    # 爬虫模块
│   ├── __init__.py
│   ├── mysteel_scraper.py     # 我的钢铁网爬虫
│   └── alibaba_scraper.py     # 1688爬虫
├── main.py                     # 主程序入口
├── data_processor.py           # 数据处理模块
├── email_sender.py             # 邮件发送模块
├── requirements.txt            # Python依赖
└── README.md                   # 项目说明
```

## 技术栈

- Python 3.11
- Requests + BeautifulSoup4 (网页抓取)
- Pandas + OpenPyXL (数据处理)
- GitHub Actions (定时任务)
- SMTP (邮件发送)
