# Binance K线图表工具 - 专业增强版

## 📌 声明 / Disclaimer

本项目基于 [lichuan/binance-copytrading](https://github.com/lichuan/binance-copytrading) 原始项目进行改进和增强。在原作者的基础上，我们添加了更多专业交易功能和现代化界面设计。

This project is an enhanced version based on the original [lichuan/binance-copytrading](https://github.com/lichuan/binance-copytrading) project. We have added more professional trading features and modern UI design on top of the original work.

## 🎯 改进内容 / Improvements

相比原始版本，本增强版进行了以下重大改进：

### 🆕 新增功能
- **MA均线系统** - 添加MA5/MA10/MA30三条移动平均线
- **成交量指标** - 底部Volume柱状图显示
- **十字光标定位** - 精确显示价格和时间坐标
- **深色/浅色主题** - 支持一键切换主题
- **鼠标拖动** - 支持拖动查看历史K线数据
- **滚轮缩放** - 鼠标滚轮放大缩小图表
- **更多快捷键** - R重置、G网格、M均线、V成交量等

### 🔧 技术优化
- **全新UI设计** - 采用现代化的专业交易界面
- **Canvas性能优化** - 更流畅的图表渲染
- **代码重构** - 模块化设计，更易维护和扩展
- **响应式布局** - 自适应不同屏幕尺寸
- **CSS变量** - 支持主题定制

### 🐛 问题修复
- 修复了原版K线无法正常显示的问题
- 修复了数据格式不兼容问题
- 优化了服务器代理逻辑
- 改进了错误处理机制

## 🚀 项目简介 / Project Introduction

专业的加密货币K线图表分析工具，基于币安交易所实时数据，提供类似TradingView的专业交易界面。支持多币种、多周期、技术指标分析，为加密货币交易员提供强大的行情分析工具。

A professional cryptocurrency candlestick chart analysis tool based on Binance exchange real-time data, providing a TradingView-like professional trading interface.

## ✨ 核心功能 / Core Features

### 📊 专业图表
- 实时K线图 - 基于Canvas的高性能渲染
- 成交量指标 - 直观展示市场活跃度
- MA均线系统 - 自动计算并实时更新
- 十字光标 - OHLCV数据实时显示

### 🎛 交互功能
- 鼠标拖动查看历史数据
- 滚轮缩放图表
- 键盘快捷键操作
- 触摸屏支持（移动端）

### 🎨 界面特性
- 深色/浅色主题切换
- 专业网格背景
- 实时信息面板
- 状态栏显示

### 📈 数据支持
- 多时间周期：1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w
- 多交易对：BTC, ETH, SOL, BNB, XRP, DOGE等
- 实时数据更新（10秒自动刷新）

## 📦 快速开始 / Quick Start

### 环境要求
- Python 3.6+
- 现代浏览器（Chrome/Firefox/Safari最新版本）

### 安装运行

1. **克隆项目**
```bash
git clone [your-repo-url]
cd binance-copytrading
```

2. **启动服务器**
```bash
python3 server.py
```

或使用快速启动脚本：
```bash
chmod +x start.sh
./start.sh
```

3. **访问应用**
```
http://localhost:8080
```

## 🎮 使用指南 / User Guide

### 键盘快捷键
| 快捷键 | 功能说明 |
|--------|----------|
| **D** | 放大K线 |
| **F** | 缩小K线 |
| **←/→** | 左右移动 |
| **↑/↓** | 缩放Y轴 |
| **R** | 重置视图 |
| **G** | 网格开关 |
| **M** | MA均线开关 |
| **V** | 成交量开关 |
| **H** | 帮助面板 |

### 鼠标操作
- **左键拖动** - 查看历史K线
- **滚轮** - 缩放图表
- **悬停** - 显示十字光标和价格

## 🛠 技术架构 / Technical Stack

### 前端
- 原生JavaScript（无框架依赖）
- HTML5 Canvas
- CSS3 (支持CSS变量)

### 后端
- Python3 HTTP Server
- Binance REST API代理

## 📋 项目结构 / Project Structure

```
binance-copytrading/
├── index.html        # 主页面（专业版）
├── server.py         # Python代理服务器
├── start.sh          # 快速启动脚本
├── README.md         # 项目文档
└── *.gif            # 演示图片
```

## 🔧 配置说明 / Configuration

### 添加新交易对
编辑 `index.html` 中的币种选项：
```html
<option value="SYMBOL:价格精度:数量精度">显示名称</option>
```

### 自定义主题颜色
修改CSS变量：
```css
:root {
  --up-color: #26a69a;
  --down-color: #ef5350;
  --ma5-color: #FF9800;
  --ma10-color: #2196F3;
  --ma30-color: #9C27B0;
}
```

## 🚧 开发计划 / Roadmap

- [ ] WebSocket实时数据推送
- [ ] 更多技术指标（MACD, RSI, 布林带）
- [ ] 画线工具
- [ ] 自定义指标参数
- [ ] 本地存储用户配置
- [ ] 多窗口同步
- [ ] 移动端优化

## 🤝 贡献指南 / Contributing

欢迎提交Issue和Pull Request！

提交前请确保：
1. 代码风格保持一致
2. 添加必要的注释
3. 测试功能正常
4. 更新相关文档

## 📄 开源协议 / License

MIT License

## 🙏 致谢 / Acknowledgments

- 感谢 [lichuan](https://github.com/lichuan) 的原始项目
- 感谢币安交易所提供的公开API
- 感谢所有贡献者的支持

---

**如果这个项目对您有帮助，请给个 Star ⭐ 支持一下！**

**If this project helps you, please give it a Star ⭐!**