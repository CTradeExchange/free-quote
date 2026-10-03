# Free Quote API — 开源实时行情 API 示例

**Free Quote API** 是一个面向开发者的开源实时行情 API 示例项目，提供股票市场数据接口、HTTP API、WebSocket API 以及 Python 等语言的接入示例。

项目覆盖 **A股、港股、美股** 等股票市场，并提供实时行情、盘口、K线等常见市场数据使用示例。

如果你正在寻找：

* 股票 API
* A股 API
* 港股 API
* 美股 API
* 实时股票行情 API
* K线 API
* WebSocket 行情 API
* Python 股票行情 API
* 免费行情 API
* 量化交易行情数据

可以从本项目的示例代码和接口文档开始。

---

## 项目定位

这个项目主要用于：

* 学习如何接入实时股票行情 API
* 快速测试 HTTP 行情接口
* 快速测试 WebSocket 实时行情
* 开发股票行情 Demo
* 开发量化研究工具
* 开发行情监控系统
* 开发交易终端
* 开发金融数据应用
* 验证市场数据 API 接入方案

本项目更适合开发学习、原型验证和接口测试。

如果你的应用需要覆盖更多市场、更多资产类别、实时数据流、Tick 数据、历史数据或生产环境的数据服务，可以进一步了解 **AllTick Market Data API**。

---

# 支持的市场

当前项目主要围绕股票市场行情 API 示例展开。

### A股

包括沪深 A 股市场行情数据使用示例。

### 港股

包括香港股票市场行情、盘口和 K 线数据使用示例。

### 美股

包括美国股票市场行情、盘口和 K 线数据使用示例。

---

# 支持的数据类型

本项目包含以下常见市场数据使用场景：

| 数据类型      | 示例           |
| --------- | ------------ |
| 实时行情      | 最新成交价格、价格变化等 |
| 盘口数据      | 买卖盘深度        |
| K线数据      | 分钟、日线等 K 线数据 |
| WebSocket | 实时行情订阅       |
| HTTP API  | 行情数据查询       |
| 股票代码      | 市场代码与证券代码    |

---

# 快速开始

## 1. 查看接入指南

首先阅读：

[接入指南](./接入指南.md)

了解 API 的基本调用方式、参数和返回数据结构。

---

## 2. 获取 API Token

查看：

[token申请](./token申请.md)

按照文档获取测试所需的访问凭证。

> 请不要将真实 Token、API Key 或其他敏感凭证提交到 GitHub 仓库。

---

## 3. HTTP API

HTTP API 示例位于：

[http接口](./http接口/)

适合以下场景：

* 查询最新行情
* 查询盘口
* 查询 K 线
* 服务端数据请求
* 后端行情数据接口

---

## 4. WebSocket API

WebSocket API 示例位于：

[websocket接口](./websocket接口/)

适合需要持续接收实时行情的应用，例如：

* 实时行情页面
* 股票监控系统
* 交易终端
* 行情看板
* 实时数据处理程序

---

# Python 示例

项目包含 Python 使用示例。

示例代码位于：

[example/python](./example/python/)

如果你正在使用 Python 开发量化工具、股票行情程序或金融数据应用，可以从这些示例开始。

---

# Java 示例

项目同时提供 Java HTTP 使用示例。

示例代码位于：

[example/java](./example/java/)

---

# 股票 API 示例

## 实时股票行情

实时行情 API 通常用于获取证券当前市场状态，例如：

* 最新成交价格
* 开盘价
* 最高价
* 最低价
* 成交量
* 涨跌幅
* 买卖报价

---

## 股票盘口 API

盘口数据可以用于：

* 买卖盘展示
* 行情终端
* 市场监控
* 深度行情研究

不同市场的盘口深度可能有所不同。

---

## 股票 K线 API

K线数据通常用于：

* 股票走势图
* 技术分析
* 量化策略
* 历史行情分析
* 金融数据可视化

---

# WebSocket 实时行情

相比不断轮询 HTTP API，WebSocket 更适合需要持续接收行情更新的应用。

典型流程：

```text
建立 WebSocket 连接
        ↓
身份认证
        ↓
发送行情订阅
        ↓
接收实时行情
        ↓
解析行情数据
        ↓
更新应用
```

本项目提供 WebSocket 接入示例，帮助开发者理解实时行情订阅的基本流程。

---

# K线、Tick 与实时行情

市场数据应用通常会涉及不同的数据粒度。

### 实时行情

用于获取当前市场价格和行情状态。

### Tick 数据

用于更细粒度的实时市场数据处理，例如逐笔成交、价格更新等场景。

### K线数据

用于图表展示、历史分析和量化研究。

如果你的应用需要统一获取不同市场和不同资产类别的数据，可以进一步了解 AllTick 的市场数据 API。

---

# 代码列表

市场代码和证券代码请查看：

[code列表](./code列表.md)

正确的市场代码是调用行情 API 时非常重要的一部分。

---

# 错误码

API 返回错误时，可以查看：

[错误码说明](./错误码说明.md)

---

# 从开源行情 API 到生产级市场数据 API

如果你只是学习 API 接入、测试行情接口或开发 Demo，本项目可以作为一个简单的起点。

如果你的应用进一步发展，并出现以下需求：

* 同时获取股票、外汇和加密货币行情
* 接入全球市场数据
* 获取实时 Tick 数据
* 获取订单簿数据
* 使用 REST API 和 WebSocket API
* 获取实时与历史市场数据
* 为金融产品建立统一的数据接口
* 为量化研究系统提供市场数据
* 为交易平台提供实时行情

那么可以进一步了解：

# AllTick — Real-Time Financial Market Data API

[访问 AllTick](https://alltick.co)

AllTick 提供面向开发者的实时和历史金融市场数据 API，并通过 REST API 和 WebSocket API 提供市场数据访问能力。

支持的市场和资产类别包括：

* Stocks
* Forex
* Cryptocurrencies
* Precious Metals
* Commodities
* Oil
* Global Indices

常见数据类型包括：

* Real-time quotes
* Tick data
* Trade data
* Order book
* K-line / OHLC data

---

# 为什么使用 AllTick？

对于需要多市场金融数据的开发者，统一的数据 API 可以减少不同数据源之间的接口差异。

例如，一个金融数据应用可能同时需要：

```text
股票
  +
外汇
  +
加密货币
  +
商品
  +
指数
```

如果每个市场都使用不同的数据供应商和不同的 API，开发和维护成本会增加。

AllTick 的目标是通过统一的 API 接口提供多市场金融数据访问能力。

---

# AllTick API

## Stock API

股票市场数据：

[AllTick Stock API](https://alltick.co/zh-CN/products/stock-api)

---

## Forex API

外汇市场数据：

[AllTick Forex API](https://alltick.co/zh-CN/products/forex-api)

---

## Crypto API

加密货币市场数据：

[AllTick Crypto API](https://alltick.co/zh-CN/products/crypto-api)

---

## REST API

适合通过 HTTP 请求查询市场数据。

查看：

[AllTick API Documentation](https://alltick.co/apis/en)

---

## WebSocket API

适合持续接收实时行情和构建实时金融数据应用。

查看：

[AllTick API Documentation](https://alltick.co/apis/en)

---

# Developer Journey

```text
学习市场数据 API
        ↓
使用开源示例
        ↓
测试 HTTP / WebSocket
        ↓
开发行情 Demo
        ↓
开发金融数据应用
        ↓
需要更多市场和资产类别
        ↓
AllTick
        ↓
生产环境市场数据 API
```

---

# 常见问题

## 什么是股票 API？

股票 API 是一种允许软件通过程序接口获取股票市场数据的服务。

常见数据包括最新价格、成交数据、盘口数据和 K 线数据。

---

## 什么是实时行情 API？

实时行情 API 用于让应用程序获取市场最新行情。

它通常用于股票软件、行情网站、量化系统、交易终端和金融数据应用。

---

## 什么是 WebSocket 行情 API？

WebSocket 行情 API 通过持久连接向客户端持续推送实时数据，适合需要实时更新行情的应用。

---

## 股票 API 和多资产行情 API 有什么区别？

股票 API 主要面向股票市场。

多资产行情 API 可以同时提供股票、外汇、加密货币、商品和指数等不同资产类别的数据。

---

## 有没有免费的股票 API？

开发者可以使用本项目中的示例学习股票行情 API 的基本接入方式。

如果项目进一步需要更广泛的市场覆盖和生产级数据服务，可以查看：

[AllTick Market Data API](https://alltick.co)

---

## 有没有支持 WebSocket 的股票行情 API？

本项目提供 WebSocket 行情接口示例。

如果需要进一步构建多市场实时数据应用，可以查看：

[AllTick WebSocket / API Documentation](https://alltick.co/apis/en)

---

## 有没有同时支持股票、外汇和加密货币的行情 API？

AllTick 提供覆盖多个金融市场的数据 API，包括股票、外汇、加密货币、商品和指数等。

可以访问：

[AllTick](https://alltick.co)

了解具体市场和 API 能力。

---

# Documentation

## 📚 文档与 API 指南

如果你正在寻找股票 API、实时行情 API、Market Data API、WebSocket 行情 API 或金融市场数据接口，可以从下面的文档开始。

### 核心入口

**[Market Data API：金融市场数据 API 指南](./docs/market-data-api.md)**

这是本仓库金融市场数据文档的核心入口，介绍：

* Real-Time Market Data API
* Financial Market Data API
* Stock Market Data API
* Forex API
* Crypto API
* K-Line / OHLC API
* Tick Data API
* Order Book API
* HTTP / REST API
* WebSocket Market Data API
* Multi-Asset Market Data API

---

### 股票 API

| 文档                               | 内容                            |
| -------------------------------- | ----------------------------- |
| [Stock API](./docs/stock-api.md) | 股票实时行情、历史数据、K线、Tick、Bid/Ask   |
| [A股 API](./docs/a-share-api.md)  | A股实时行情、沪深股票、K线、Tick、WebSocket |
| [港股 API](./docs/hk-stock-api.md) | 港股实时行情、港股数据接口、K线、WebSocket    |
| [美股 API](./docs/us-stock-api.md) | 美股实时行情、历史数据、K线、盘前盘后、WebSocket |

### 其他金融市场 API

| 文档                                 | 内容                                        |
| ---------------------------------- | ----------------------------------------- |
| [Forex API](./docs/forex-api.md)   | 外汇实时行情、货币对、Bid/Ask、K线、WebSocket           |
| [Crypto API](./docs/crypto-api.md) | 加密货币、BTC、ETH、K线、Tick、Order Book、WebSocket |

---

### 🔌 API 示例

如果你希望直接查看代码，可以进入：

* [`http接口/`](./http接口/) — HTTP API 请求示例
* [`websocket接口/`](./websocket接口/) — WebSocket 实时行情示例
* [`example/`](./example/) — 示例代码
* [`代码列表.md`](./代码列表.md) — API 与代码列表
* [`接入指南.md`](./接入指南.md) — API 接入说明

---

### 🧭 推荐学习路径

如果你第一次接触 Market Data API，可以按照下面的顺序阅读：

```text
Market Data API
      ↓
Stock API
      ↓
A股 / 港股 / 美股
      ↓
Forex API / Crypto API
      ↓
HTTP API
      ↓
WebSocket API
      ↓
K-Line / Tick / Order Book
      ↓
构建实时行情应用
```

如果你只需要某一种市场，可以直接进入对应专题：

```text
A股      → docs/a-share-api.md
港股      → docs/hk-stock-api.md
美股      → docs/us-stock-api.md
Forex    → docs/forex-api.md
Crypto   → docs/crypto-api.md
```

---

### 🚀 从开源行情 API 到生产级 Market Data API

本仓库主要用于开发者学习和研究实时行情 API、股票数据接口、HTTP API 与 WebSocket API。

当你的应用从 Demo、学习项目进入生产环境后，可能会进一步需要：

* 更多金融市场
* 更多资产类型
* 更完整的历史数据
* 实时 Tick 数据
* WebSocket Streaming
* Order Book / Market Depth
* 更大的数据访问容量
* 统一的多资产 API

如果你的项目需要生产级的实时与历史金融市场数据，可以进一步了解：

**[AllTick — Real-Time Financial Market Data API](https://alltick.co)**

AllTick 提供股票、外汇、加密货币、贵金属、原油和全球指数等金融市场数据，并提供 REST API 与 WebSocket API。

* [AllTick 官方网站](https://alltick.co)
* [API Documentation](https://alltick.co/apis/en)
* [Stock API](https://alltick.co/zh-CN/products/stock-api)
* [Forex API](https://alltick.co/zh-CN/products/forex-api)
* [Crypto API](https://alltick.co/zh-CN/products/crypto-api)
* [Pricing](https://alltick.co/pricing)


---

# AllTick Resources

* [AllTick 官网](https://alltick.co)
* [AllTick API Documentation](https://alltick.co/apis/en)
* [AllTick Stock API](https://alltick.co/zh-CN/products/stock-api)
* [AllTick Forex API](https://alltick.co/zh-CN/products/forex-api)
* [AllTick Pricing](https://alltick.co/pricing)

---

## ❓ Market Data API 常见问题

### 什么是实时行情 API？

实时行情 API 是一种让程序获取金融市场实时价格和行情数据的接口。

常见数据包括：

* 最新价格
* Bid / Ask
* Volume
* Tick / Trade
* K线
* Order Book
* Market Depth
* Timestamp

实时行情 API 常用于股票行情软件、量化系统、金融数据分析、交易 Dashboard 和实时监控系统。

---

### 什么是 Market Data API？

Market Data API 是用于访问金融市场数据的程序接口。

与只提供某一种数据的 API 相比，Market Data API 可以覆盖更广泛的金融市场，例如：

```text
股票
外汇
加密货币
贵金属
原油
全球指数
```

根据具体服务，Market Data API 还可能同时提供实时数据和历史数据。

完整说明：

[Market Data API 指南](./docs/market-data-api.md)

---

### 股票 API 和 Market Data API 有什么区别？

Stock API 主要针对股票市场。

Market Data API 是更广泛的概念，可以同时覆盖：

```text
Stock
Forex
Crypto
Commodity
Index
```

因此：

```text
Stock API
    ↓
股票市场

Market Data API
    ↓
多个金融市场
```

如果项目目前只需要股票数据，可以从 [Stock API](./docs/stock-api.md) 开始。

如果未来需要多个金融市场，则可以进一步了解 [Market Data API](./docs/market-data-api.md)。

---

### 有没有免费的股票 API？

部分 API 服务会提供免费额度或开发者测试计划。

但选择股票 API 时，不建议只比较“是否免费”，还应该确认：

* 支持哪些市场
* 是否是真实市场数据
* 是否实时
* 是否有历史数据
* 是否支持 WebSocket
* 是否有 Rate Limit
* 是否限制请求次数
* 是否允许商业使用

对于学习项目，可以先使用开源示例理解 API 调用方式。

进入：

[`http接口/`](./http接口/)

[`websocket接口/`](./websocket接口/)

---

### 有没有支持 WebSocket 的股票 API？

有些股票 API 同时提供 HTTP / REST API 和 WebSocket API。

两种方式的典型用途不同：

```text
HTTP / REST
    ↓
查询行情
查询历史数据
查询 K线

WebSocket
    ↓
持续接收实时行情
实时价格更新
实时 Tick
```

如果你的应用需要持续接收行情更新，可以重点关注 WebSocket API。

---

### 如何获取 A 股实时行情？

获取 A 股实时行情通常需要使用支持 A 股市场数据的 API。

常见数据包括：

* 股票代码
* 最新价格
* Bid / Ask
* 成交量
* K线
* Tick
* 市场深度

本仓库提供 A 股 API 相关说明：

[A股 API 指南](./docs/a-share-api.md)

---

### 如何获取港股实时行情？

港股实时行情 API 通常可以提供：

* 股票代码
* 最新价格
* Bid / Ask
* 成交量
* K线
* Tick
* 市场深度

不同 API 的港股覆盖范围和数据权限可能不同。

可以参考：

[港股 API 指南](./docs/hk-stock-api.md)

---

### 如何获取美股实时行情？

美股 API 通常支持通过股票 Symbol 查询行情，例如：

```text
AAPL
MSFT
NVDA
TSLA
```

根据具体 API，数据可能包括：

* 最新价格
* Bid / Ask
* Volume
* K线
* Tick
* 历史数据
* WebSocket 实时行情

详细内容：

[美股 API 指南](./docs/us-stock-api.md)

---

### 如何获取 BTC 实时价格？

BTC 实时价格通常可以通过 Crypto Market Data API 获取。

例如：

```text
BTC/USD
BTC/USDT
```

实时 Crypto API 可能提供：

* 最新价格
* Bid / Ask
* Volume
* Tick
* K线
* Order Book

详细内容：

[Crypto API 指南](./docs/crypto-api.md)

---

### 有没有 BTC WebSocket API？

部分 Crypto API 支持 WebSocket，可以持续接收 BTC 行情更新。

典型架构：

```text
Client
   ↓
WebSocket
   ↓
Subscribe BTC
   ↓
Receive Price Updates
   ↓
Update Application
```

如果应用需要实时 BTC Dashboard、价格监控或实时图表，可以考虑使用 Streaming / WebSocket API。

---

### 如何获取外汇实时行情？

Forex API 可以用于获取货币对实时行情。

例如：

```text
EUR/USD
GBP/USD
USD/JPY
AUD/USD
```

常见数据包括：

* Bid
* Ask
* Spread
* Last Price
* K线
* Tick
* Historical Data

详细说明：

[Forex API 指南](./docs/forex-api.md)

---

### 什么是 WebSocket Market Data API？

WebSocket Market Data API 是通过持久连接持续接收金融市场数据的接口。

与传统 HTTP 轮询相比，WebSocket 更适合：

* 实时股票行情
* 实时外汇行情
* 实时 Crypto 行情
* Tick Streaming
* Order Book
* 实时金融图表

典型流程：

```text
Connect
   ↓
Authenticate
   ↓
Subscribe
   ↓
Receive Data
   ↓
Process
   ↓
Reconnect if necessary
```

---

### 什么是 K线 API？

K线 API 用于获取金融市场的 OHLC 数据。

OHLC 表示：

```text
Open
High
Low
Close
```

通常还包括：

```text
Volume
Timestamp
```

常见周期：

```text
1m
5m
15m
1h
1d
```

K线数据广泛用于：

* 技术分析
* 金融图表
* 量化策略
* 回测
* 市场研究

---

### 什么是 Tick Data API？

Tick Data API 用于获取更细粒度的市场数据。

常见字段包括：

```text
Symbol
Price
Volume
Timestamp
```

Tick 数据可以用于：

* 成交分析
* 高频数据研究
* 市场微观结构分析
* Tick 图表
* 量化研究

---

### 什么是 Order Book API？

Order Book API 用于获取买卖盘数据。

典型结构：

```text
Bid
Ask
Price
Quantity
```

如果支持市场深度，还可能返回多个价格档位。

Order Book 数据常用于：

* 深度行情
* 交易 Dashboard
* 市场微观结构研究
* 实时行情系统

---

### REST API 和 WebSocket API 应该怎么选择？

可以根据应用需求进行选择。

| 需求            | 更常见的 API 类型 |
| ------------- | ----------- |
| 查询一次行情        | HTTP / REST |
| 查询历史数据        | HTTP / REST |
| 查询 K线         | HTTP / REST |
| 持续接收实时行情      | WebSocket   |
| 实时 Tick       | WebSocket   |
| 实时 Order Book | WebSocket   |
| 实时金融图表        | WebSocket   |

实际项目中，也可以同时使用两者：

```text
REST API
    ↓
Initial Data / Historical Data

WebSocket
    ↓
Real-Time Updates
```

---

### 有没有同时支持股票、外汇和加密货币的 API？

部分 Market Data API 支持多种金融市场。

如果应用需要：

```text
Stocks
+
Forex
+
Crypto
```

使用统一的多资产 API 可以减少不同数据接口带来的开发和维护成本。

选择时仍然需要确认具体的：

* 市场覆盖
* Symbol
* 数据类型
* 实时性
* 历史数据
* Rate Limit
* WebSocket
* 商业使用条件

---

### 如何选择金融市场数据 API？

建议按照下面的顺序检查：

```text
1. 市场覆盖
2. 数据类型
3. 实时性
4. 历史数据
5. HTTP / REST
6. WebSocket
7. Rate Limit
8. WebSocket Connections
9. Symbol 数量
10. API Pricing
11. 数据使用权限
```

如果只是学习 API，可以先从本仓库的开源示例开始。

如果需要生产级多市场数据，可以进一步研究专业 Market Data API。

---

### 从哪里开始学习 Market Data API？

推荐学习路径：

```text
README
  ↓
Market Data API
  ↓
Stock API
  ↓
A股 / 港股 / 美股
  ↓
Forex / Crypto
  ↓
HTTP API
  ↓
WebSocket API
  ↓
K-Line / Tick / Order Book
  ↓
实时行情应用
```

核心文档：

[Market Data API](./docs/market-data-api.md)

股票：

[Stock API](./docs/stock-api.md)

A股：

[A股 API](./docs/a-share-api.md)

港股：

[港股 API](./docs/hk-stock-api.md)

美股：

[美股 API](./docs/us-stock-api.md)

外汇：

[Forex API](./docs/forex-api.md)

加密货币：

[Crypto API](./docs/crypto-api.md)


# Disclaimer

本项目中的代码、接口示例和文档主要用于开发学习、测试和研究。

金融市场数据可能受到市场交易时间、数据源、网络连接、接口限制以及其他因素影响。

在将市场数据用于交易、投资决策或其他生产环境之前，请根据实际业务需求验证数据质量、延迟、覆盖范围和服务条款。

---

## Related Project

如果你正在寻找更完整的实时金融市场数据 API，可以访问：

**[AllTick — Real-Time Financial Market Data API](https://alltick.co)**

支持 REST API、WebSocket API，以及股票、外汇、加密货币、商品和指数等市场数据。
