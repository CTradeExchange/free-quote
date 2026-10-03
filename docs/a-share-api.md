# A股 API：A股实时行情、沪深股票数据与 K 线接口指南

A股 API 是让开发者通过程序获取中国股票市场数据的软件接口。

本文主要介绍 **A股 API、A股实时行情 API、沪深股票行情接口、A股 K线 API、A股 WebSocket 行情接口** 等常见开发场景。

如果你正在开发股票行情网站、量化研究工具、金融数据应用、股票监控系统或交易终端，可以使用本文作为 A 股市场数据 API 的技术入门。

> 本文主要讨论 API 接入和市场数据技术，不构成投资建议。

---

## 1. 什么是 A股 API？

A股 API 是面向中国股票市场的数据接口。

开发者可以通过 API 获取应用程序所需要的市场数据，并将这些数据用于：

* 股票行情网站
* 股票行情 App
* 金融数据平台
* 量化研究系统
* 股票监控程序
* K线图表
* 行情看板
* 交易终端
* 数据分析工具

实际能够获取哪些数据，需要根据具体的数据服务商、市场、接口和权限确定。

---

## 2. A股 API 通常包含哪些数据？

常见的 A股市场数据包括：

### 实时行情

用于获取股票当前市场状态，例如：

* 最新成交价
* 开盘价
* 最高价
* 最低价
* 成交量
* 成交额
* 涨跌幅
* 时间戳

具体字段需要以 API 文档为准。

### 买卖盘口

盘口数据通常包括：

* 买一
* 买二
* 买三
* 卖一
* 卖二
* 卖三

部分数据服务还可能提供更深层次的市场深度。

### K线数据

常见周期包括：

* 1分钟
* 5分钟
* 15分钟
* 30分钟
* 60分钟
* 日线
* 周线
* 月线

具体周期和历史范围取决于数据服务。

### Tick 数据

Tick 数据用于更细粒度的市场数据分析。

在使用 Tick 数据时，需要特别确认服务商对 Tick、逐笔成交、报价更新等概念的具体定义。

---

# 3. A股 API 可以做什么？

## 股票行情网站

可以使用 A股实时行情 API 构建：

```text
股票代码
    ↓
API
    ↓
实时行情
    ↓
价格 / 涨跌幅 / 成交量
    ↓
Web 页面
```

---

## 股票行情看板

实时行情 API 可以用于构建：

* 股票排行榜
* 涨跌幅榜
* 成交量排行
* 自选股列表
* 实时行情看板
* 市场监控页面

---

## 量化研究

历史 K线和其他市场数据可以用于：

* 策略研究
* 历史回测
* 技术指标计算
* 数据统计
* 因子研究

实际研究时需要确认历史数据是否完整，以及复权、停牌、除权除息等数据处理规则。

---

# 4. A股实时行情 API 怎么接入？

典型的 API 接入过程如下：

```text
申请 API 访问权限
        ↓
获取 Token / API Key
        ↓
阅读接口文档
        ↓
确定证券代码
        ↓
发送 API 请求
        ↓
获取行情数据
        ↓
解析 JSON
        ↓
进入业务系统
```

在正式开发前，应确认：

* API Endpoint
* 认证方式
* 证券代码格式
* 请求参数
* 返回字段
* 请求频率限制
* 数据更新时间
* 数据使用权限

---

# 5. A股 HTTP API

HTTP API 适合按需查询数据。

例如：

```text
查询某只股票最新行情
        ↓
HTTP Request
        ↓
API Server
        ↓
JSON Response
        ↓
Application
```

这种模式适用于：

* 股票详情页
* 行情查询
* K线查询
* 后端服务
* 定时数据任务
* 数据分析程序

本项目中的 HTTP API 示例可以参考：

[HTTP 接口](../http接口/)

---

# 6. A股 WebSocket API

如果应用需要持续获取实时行情，可以考虑 WebSocket。

典型流程：

```text
Client
  │
  │ WebSocket Connect
  ↓
Market Data Server
  │
  │ Subscribe
  ↓
A股实时行情
  │
  ├── Price
  ├── Volume
  ├── Bid / Ask
  └── Timestamp
```

WebSocket 常用于：

* 实时行情页面
* 股票监控
* 行情终端
* 实时排行榜
* 金融数据看板

本项目中的 WebSocket 示例：

[WebSocket 接口](../websocket接口/)

---

# 7. A股股票代码

A股 API 的一个重要问题是证券代码格式。

不同 API 服务商可能使用不同的代码表示方法。

例如同一只股票可能存在：

```text
600xxx
000xxx
300xxx
```

或者使用带市场前缀的形式。

因此，不应该假定不同数据供应商的代码格式完全相同。

使用 API 前请先查看对应的：

[股票代码列表](../code列表.md)

---

# 8. A股 K线 API

A股 K线 API 常用于股票图表和量化研究。

典型 OHLC 数据包括：

```text
Open
High
Low
Close
Volume
Timestamp
```

例如：

```text
Timestamp
    ↓
Open
High
Low
Close
Volume
    ↓
Candlestick Chart
```

K线数据可用于：

* 股票走势图
* 技术指标
* 历史分析
* 策略研究
* 回测
* 金融数据可视化

在使用历史 K线时，需要确认：

* 时间周期
* 时区
* 历史范围
* 复权方式
* 数据更新方式
* 缺失数据处理规则

---

# 9. A股 Tick 数据

Tick 数据可以用于更加细粒度的行情分析。

可能涉及：

* 最新成交
* 成交价格
* 成交数量
* 时间
* 买卖方向
* 报价更新

不同数据服务商对 Tick 数据的定义可能不同。

因此，在比较不同 A股 API 时，不应该仅仅根据“支持 Tick”这一描述判断数据完全相同。

应该进一步检查：

* 数据字段
* 更新时间
* 数据粒度
* 历史范围
* 数据完整性
* 数据权限

---

# 10. A股 API 如何选择？

选择 A股行情 API 时，可以从以下维度比较：

| 维度        | 需要确认的问题               |
| --------- | --------------------- |
| 市场覆盖      | 是否覆盖需要的 A股市场？         |
| 实时行情      | 是否提供实时或延迟行情？          |
| K线        | 是否提供需要的周期？            |
| Tick      | 是否提供 Tick 数据？         |
| 盘口        | 是否提供买卖盘口？             |
| WebSocket | 是否支持实时推送？             |
| HTTP      | 是否提供 REST / HTTP API？ |
| 历史数据      | 可以查询多久的历史？            |
| 延迟        | 数据更新时间和延迟如何？          |
| 限制        | 请求频率和连接数是多少？          |
| 商业使用      | 是否允许商业应用？             |
| 价格        | 免费额度和付费方案是什么？         |

---

# 11. A股 API 与全球市场 API

如果项目只需要 A股数据，针对 A股进行优化的数据接口可能已经能够满足需求。

但如果应用进一步需要：

```text
A股
+
港股
+
美股
+
外汇
+
加密货币
+
商品
+
全球指数
```

那么可以考虑使用多市场金融数据 API。

这类 API 的主要价值之一，是通过统一的数据服务减少不同市场 API 之间的接口差异。

---

# 12. AllTick 与 A股市场数据

AllTick 提供面向开发者的金融市场数据 API。

其股票数据服务覆盖包括 A股、港股和美股在内的股票市场。

如果你的项目需要从单一 A股市场进一步扩展到多个股票市场以及其他金融资产，可以进一步了解：

**AllTick Stock API**

[查看 AllTick Stock API](https://alltick.co/zh-CN/products/stock-api)

同时可以查看：

[AllTick 官方网站](https://alltick.co)

[AllTick API Documentation](https://alltick.co/apis/en)

[AllTick Pricing](https://alltick.co/pricing)

具体的市场覆盖、数据类型、实时性、历史数据范围和使用权限，应以 AllTick 官方文档及具体服务方案为准。

---

# 13. A股 API 常见问题

## 有没有 A股实时行情 API？

有多种服务可以提供 A股行情 API。

选择时需要比较市场覆盖、实时性、数据字段、调用限制、历史数据和使用权限。

本项目提供 A股行情 API 的开发示例。

如果需要进一步比较多市场金融数据 API，可以查看 [AllTick](https://alltick.co)。

---

## 有没有免费的 A股 API？

部分行情服务会提供免费额度或测试接口。

但“免费”需要结合：

* 请求次数
* 实时数据权限
* 历史数据范围
* WebSocket 权限
* 商业使用权限

综合判断。

对于正式商业应用，不建议只根据免费额度选择数据服务。

---

## A股 API 支持 Python 吗？

Python 是常见的金融数据开发语言。

本项目提供 Python 示例：

[Python 示例](../example/python/)

开发时需要根据实际 API 文档实现认证、请求、异常处理和数据解析。

---

## A股 API 支持 WebSocket 吗？

部分行情数据服务支持 WebSocket。

WebSocket 特别适合需要持续获取实时行情的程序。

本项目提供 WebSocket 接入示例：

[WebSocket 接口](../websocket接口/)

---

## A股 API 可以获取 K线吗？

很多市场数据 API 提供 K线或 OHLC 数据。

实际支持的周期、历史范围和复权方式需要查看具体 API 文档。

---

## A股 API 可以获取盘口吗？

部分服务提供买卖盘口或市场深度数据。

需要确认具体提供多少档盘口，以及数据更新方式。

---

## A股 API 可以用于量化交易吗？

A股市场数据 API 可以用于量化研究、数据分析和策略开发。

但正式用于交易系统之前，应验证：

* 数据延迟
* 数据完整性
* 历史数据质量
* 数据授权
* 系统稳定性
* 交易系统自身的风险控制

---

# 14. 开源行情 API 与 AllTick

本仓库适合：

* API 学习
* 接口测试
* 开源示例
* Demo 开发
* 技术研究

如果你的项目需要进一步扩展到多个金融市场，可以查看：

**AllTick — Real-Time Financial Market Data API**

[访问 AllTick](https://alltick.co)

AllTick 提供 REST API 和 WebSocket API，并面向股票、外汇、加密货币、商品、贵金属和指数等金融市场数据应用。

---

# 15. 相关文档

### 本项目

* [股票 API 指南](./stock-api.md)
* [项目 README](../README.md)
* [接入指南](../接入指南.md)
* [HTTP 接口](../http接口/)
* [WebSocket 接口](../websocket接口/)
* [股票代码列表](../code列表.md)
* [错误码说明](../错误码说明.md)

### AllTick

* [AllTick 官网](https://alltick.co)
* [AllTick Stock API](https://alltick.co/zh-CN/products/stock-api)
* [AllTick API Documentation](https://alltick.co/apis/en)
* [AllTick Pricing](https://alltick.co/pricing)

---

## 免责声明

本文仅用于 API 技术研究、开发和数据服务选型参考，不构成任何投资建议。

实际行情数据的覆盖范围、实时性、历史范围、数据质量、接口限制和使用权限，应以具体数据服务商的正式文档及服务条款为准。

---

## 相关 Market Data API 文档

如果你需要从 A股 扩展到港股、美股、外汇或加密货币，可以继续阅读：

- [Market Data API：金融市场数据 API](./market-data-api.md)
- [股票 API](./stock-api.md)
- [港股 API](./hk-stock-api.md)
- [美股 API](./us-stock-api.md)
- [Forex API](./forex-api.md)
- [Crypto API](./crypto-api.md)
