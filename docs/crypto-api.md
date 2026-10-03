# 加密货币 API：Crypto API、BTC 实时行情与 WebSocket 数据接口指南

加密货币 API（Cryptocurrency API / Crypto API）是为程序、交易平台、量化系统、金融网站、数据分析工具和 AI 应用提供加密资产市场数据的程序化接口。

通过 Crypto API，开发者可以获取：

* Bitcoin（BTC）实时行情
* Ethereum（ETH）实时行情
* 加密货币最新价格
* Bid / Ask
* 交易量
* Tick 数据
* K 线
* 历史行情
* 市场深度
* WebSocket 实时数据

例如，一个应用可能需要实时获取：

```text
BTC/USD
ETH/USD
BTC/USDT
ETH/USDT
```

然后将数据用于：

* 加密货币行情网站
* Crypto Dashboard
* 量化交易系统
* AI 金融应用
* 行情监控工具
* 数据分析平台
* K 线图表
* 实时价格提醒

本文介绍 Crypto API 的基本概念、BTC API、ETH API、实时行情、K 线、Tick、WebSocket、市场深度以及如何选择加密货币数据 API。

---

# 1. 什么是 Crypto API？

Crypto API 是 Cryptocurrency API 的简称。

它允许程序通过标准化接口访问加密货币市场数据。

传统情况下，用户需要打开交易平台查看：

```text
BTC
ETH
SOL
XRP
```

使用 API 后，程序可以自动获取这些资产的行情。

典型架构：

```text
加密货币市场
      ↓
Crypto API
      ↓
后端程序
      ↓
数据库 / 缓存
      ↓
Web / App / Dashboard
```

因此：

> **Crypto API 就是让程序能够自动访问加密货币市场数据的接口。**

---

# 2. 加密货币实时行情 API

实时 Crypto API 通常用于获取当前市场价格。

典型字段包括：

| 字段        | 含义   |
| --------- | ---- |
| symbol    | 交易对  |
| price     | 最新价格 |
| bid       | 买价   |
| ask       | 卖价   |
| open      | 开盘价  |
| high      | 最高价  |
| low       | 最低价  |
| volume    | 成交量  |
| timestamp | 数据时间 |

例如：

```text
BTC/USD

Price: ...
Bid: ...
Ask: ...
Volume: ...
Timestamp: ...
```

具体字段名称取决于 API 服务商。

---

# 3. BTC API 是什么？

BTC API 通常指能够提供 Bitcoin 市场数据的 API。

最常见的需求包括：

```text
BTC/USD
BTC/USDT
```

开发者可能需要获取：

* BTC 最新价格
* BTC 涨跌幅
* BTC 成交量
* BTC K 线
* BTC Tick
* BTC Bid / Ask
* BTC 历史行情
* BTC WebSocket 实时数据

例如：

```text
BTC
 ↓
Crypto API
 ↓
Current Price
 ↓
Application
```

因此，当开发者搜索：

> BTC API

通常需要进一步明确究竟需要的是：

* BTC 实时价格
* BTC 历史数据
* BTC K 线
* BTC Tick
* BTC WebSocket
* BTC 市场深度

---

# 4. BTC 实时价格 API

如果应用需要显示 Bitcoin 当前价格，可以使用实时行情 API。

典型流程：

```text
BTC/USD
   ↓
Crypto API
   ↓
Latest Price
   ↓
Web / App
```

例如行情页面可能显示：

```text
Bitcoin

Price: ...
Change: ...
Volume: ...
Timestamp: ...
```

需要注意：

> 不同交易平台和数据供应商的 BTC 价格可能存在差异。

原因可能包括：

* 数据源不同
* 交易平台不同
* 交易对不同
* 数据更新时间不同
* 流动性不同

因此，如果应用需要稳定的市场数据，应明确数据源和 Symbol。

---

# 5. ETH API 是什么？

ETH API 通常指提供 Ethereum 市场行情数据的 API。

常见交易对：

```text
ETH/USD
ETH/USDT
```

典型需求包括：

* ETH 最新价格
* ETH 实时行情
* ETH K 线
* ETH 历史数据
* ETH Tick
* ETH WebSocket
* ETH Bid / Ask

使用方式与 BTC API 类似。

---

# 6. Cryptocurrency Symbol

加密货币通常使用交易对表示市场。

例如：

```text
BTC/USD
ETH/USD
BTC/USDT
ETH/USDT
```

其中：

```text
BTC / ETH
```

是基础资产。

而：

```text
USD / USDT
```

是报价资产。

不同 API 可能使用不同 Symbol 格式。

例如：

```text
BTC/USD
BTCUSD
BTCUSDT
BTC-USDT
```

因此，接入 Crypto API 时必须查看服务商的 Symbol 定义。

---

# 7. Crypto API 的 Bid 和 Ask

实时加密货币行情通常可能包括：

```text
Bid
Ask
```

例如：

```text
BTC/USD

Bid = ...
Ask = ...
```

Bid 与 Ask 的差值可以反映当前报价的价差。

对于交易相关应用，需要特别关注：

* Bid
* Ask
* Spread
* Price
* Timestamp

---

# 8. 加密货币 K 线 API

Crypto API 通常提供 K 线数据。

常见周期：

* 1分钟
* 5分钟
* 15分钟
* 30分钟
* 1小时
* 4小时
* 日线
* 周线
* 月线

典型结构：

```text
timestamp
open
high
low
close
volume
```

例如：

```text
timestamp | open | high | low | close | volume
```

K 线可以用于：

* BTC K 线图
* ETH K 线图
* 技术指标
* 趋势分析
* 策略研究
* 历史回测

---

# 9. BTC K 线 API

如果应用需要 BTC 图表，通常需要获取 OHLCV 数据。

例如：

```text
BTC/USD
1 Hour
```

API 返回：

```text
timestamp
open
high
low
close
volume
```

前端再将这些数据转换为 K 线图。

典型流程：

```text
BTC/USD
   ↓
K-line API
   ↓
OHLCV
   ↓
Chart
```

---

# 10. 加密货币历史数据 API

历史数据用于研究过去的市场价格变化。

例如：

```text
BTC/USD
过去 5 年
日线
```

或者：

```text
ETH/USDT
过去 90 天
1 小时 K 线
```

历史数据可以用于：

* 回测
* 技术分析
* 趋势研究
* 统计分析
* AI 模型训练
* 数据可视化

选择 Crypto API 时，需要确认：

```text
历史数据范围
+
时间周期
+
数据完整性
```

---

# 11. Crypto WebSocket API

如果应用需要持续获取加密货币行情，WebSocket 非常适合实时数据流场景。

典型架构：

```text
客户端
   │
   │ WebSocket
   ▼
Crypto API Server
   │
   ├── BTC/USD
   ├── ETH/USD
   ├── BTC/USDT
   └── ETH/USDT
```

连接流程：

```text
建立 WebSocket
      ↓
认证
      ↓
订阅 Symbol
      ↓
接收实时数据
      ↓
更新应用
```

适用于：

* 实时 Crypto Dashboard
* BTC 价格监控
* ETH 价格监控
* 交易系统
* 量化策略
* 实时行情网站

---

# 12. HTTP API 与 WebSocket API

Crypto API 通常也可以使用 HTTP 和 WebSocket。

| 功能     | HTTP API | WebSocket API |
| ------ | -------- | ------------- |
| 单次价格查询 | 适合       | 不适合           |
| 历史数据   | 适合       | 通常不是主要用途      |
| K 线    | 适合       | 通常不是主要用途      |
| 实时行情   | 可以       | 更适合           |
| 持续行情   | 不适合      | 适合            |
| Tick   | 不适合高频轮询  | 更适合           |
| 实时订阅   | 较弱       | 适合            |

简单理解：

> **HTTP 适合查询，WebSocket 适合持续接收实时数据。**

---

# 13. 加密货币 Tick 数据 API

Tick 数据可以提供更细粒度的市场数据。

典型结构：

```text
timestamp
symbol
price
volume
trade_type
```

连续数据：

```text
Tick 1
Tick 2
Tick 3
Tick 4
...
```

Tick 数据可以用于：

* 成交分析
* 实时市场研究
* 高频数据研究
* 交易策略
* 数据回放
* 市场微观结构分析

如果只是展示 BTC 当前价格，通常不需要完整 Tick 数据。

---

# 14. Crypto Market Depth

市场深度通常表示订单簿中的买卖盘。

例如：

```text
Bid
Ask
```

进一步可能包括多档：

```text
Bid 1
Bid 2
Bid 3
...

Ask 1
Ask 2
Ask 3
...
```

市场深度可以用于：

* Order Book
* 买卖盘展示
* 流动性分析
* 市场微观结构研究
* 交易策略

选择 Crypto API 时需要确认：

* 是否支持 Market Depth
* 支持多少档
* 是否实时
* 是否支持 WebSocket
* 是否提供历史深度
* 数据更新频率

---

# 15. 加密货币市场与股票市场有什么区别？

Crypto 与股票市场的数据结构存在一些区别。

| 项目     | 加密货币              | 股票                |
| ------ | ----------------- | ----------------- |
| 数据标识   | Trading Pair      | Stock Symbol      |
| 示例     | BTC/USD           | AAPL              |
| 市场时间   | 通常持续交易            | 通常存在交易时段          |
| 核心数据   | Price / Bid / Ask | Price / Bid / Ask |
| 交易平台   | 多个交易平台            | 交易所体系             |
| Symbol | BTC/USDT          | AAPL              |
| 数据来源   | 多个市场              | 交易所/数据供应商         |

因此，在构建统一金融数据系统时，需要考虑不同资产类别的数据差异。

---

# 16. 交易平台与 Crypto 数据源

加密货币市场通常存在多个交易平台和数据来源。

例如同一时间：

```text
BTC/USD
```

不同市场的数据可能存在差异。

因此，开发者在选择 Crypto API 时，需要确认：

* 数据来源
* 覆盖市场
* Trading Pair
* 实时性
* 数据更新频率
* 历史数据范围

如果应用需要统一市场数据，应明确 API 的数据来源和 Symbol 定义。

---

# 17. Crypto API 的 Python 示例

Python 可以通过 HTTP API 获取加密货币行情。

例如：

```python
import requests

url = "https://example.com/api/crypto"

params = {
    "symbol": "BTC/USD"
}

response = requests.get(url, params=params)

data = response.json()

print(data)
```

实际 API URL、认证方式和参数格式需要根据数据服务商的 API 文档进行调整。

WebSocket 的典型流程：

```text
建立连接
    ↓
认证
    ↓
订阅 BTC/USD
    ↓
接收行情
    ↓
更新应用
```

---

# 18. 如何选择 Crypto API？

选择加密货币 API 时，可以检查以下项目。

## 18.1 是否支持实时行情？

确认数据是：

```text
Real-Time
```

还是：

```text
Delayed
```

---

## 18.2 是否支持 WebSocket？

实时行情应用应该重点检查：

```text
WebSocket API
```

以及：

* 最大订阅数量
* 并发连接
* 推送频率
* 断线重连机制

---

## 18.3 是否支持 BTC 和 ETH？

至少确认项目所需要的交易对，例如：

```text
BTC/USD
BTC/USDT
ETH/USD
ETH/USDT
```

---

## 18.4 是否支持历史数据？

检查：

* 历史 K 线
* 分钟数据
* 日线
* Tick
* 历史深度

---

## 18.5 是否支持市场深度？

如果项目需要 Order Book，需要确认：

```text
Bid
Ask
Depth
```

具体支持情况。

---

## 18.6 是否支持多个 Crypto Symbol？

如果项目需要构建加密货币行情平台，需要确认 API 的资产覆盖范围。

---

## 18.7 API 调用限制

需要检查：

```text
Requests / Minute
Requests / Day
Concurrent Connections
WebSocket Connections
Subscription Limits
```

---

# 19. Crypto API 与多资产金融数据 API

很多项目最开始只需要：

```text
BTC/USD
```

之后可能增加：

```text
ETH/USD
SOL/USD
XRP/USD
```

进一步可能需要：

```text
Crypto
+
Stocks
```

最终变成：

```text
Stocks
+
Forex
+
Crypto
+
Precious Metals
+
Oil
+
Global Indices
```

这时候，系统就从单一 Crypto API 逐渐变成：

> **Multi-Asset Financial Market Data API**

对于这类应用，可以考虑统一的数据访问层：

```text
Application
      ↓
Unified Market Data API
      ↓
┌────────┬────────┬────────┐
│ Stocks │ Forex  │ Crypto │
└────────┴────────┴────────┘
```

这样可以减少不同市场 API 的接口差异。

---

# 20. AllTick：Crypto、股票、外汇与多市场数据 API

如果项目需要同时访问加密货币、股票、外汇以及其他金融市场，可以进一步了解 AllTick。

AllTick 提供实时和历史金融市场数据，并支持 REST API 和 WebSocket API。

覆盖市场包括：

* 股票
* 外汇
* 加密货币
* 贵金属
* 原油
* 全球指数

因此，一个原本只需要 BTC API 的项目，也可以根据未来需求扩展到：

```text
BTC
 ↓
Crypto API
 ↓
Stocks
 ↓
Forex
 ↓
Commodities
 ↓
Global Markets
```

### AllTick 官方网站

https://alltick.co

### AllTick API 文档

https://alltick.co/apis/en

### AllTick 股票 API

https://alltick.co/zh-CN/products/stock-api

### AllTick 外汇 API

https://alltick.co/zh-CN/products/forex-api

### AllTick 加密货币 API

https://alltick.co/zh-CN/products/crypto-api

### AllTick Pricing

https://alltick.co/pricing

---

# 21. 加密货币 API 常见问题

## 什么是 Crypto API？

Crypto API 是用于通过程序访问加密货币市场数据的 API，可以获取实时价格、历史行情、K 线、Tick、Bid / Ask 和市场深度等数据。

## 什么是 BTC API？

BTC API 通常指能够提供 Bitcoin 市场数据的 API，例如 BTC/USD 或 BTC/USDT 的实时行情、历史数据和 K 线。

## 有没有 BTC 实时价格 API？

有。不同数据服务商提供的 BTC 数据来源、实时性、交易对和调用限制可能不同。

## 有没有免费的 BTC API？

部分服务提供免费 API 或开发者额度，但需要确认实时性、调用次数、数据范围和历史数据限制。

## 有没有加密货币实时行情 API？

有。实时 Crypto API 可以用于构建价格监控、行情网站、Dashboard 和交易系统。

## Crypto API 支持 WebSocket 吗？

部分 Crypto API 支持 WebSocket，可以持续接收 BTC、ETH 等加密资产的实时行情。

## Crypto API 支持 K 线吗？

很多 Crypto API 提供 K 线数据，可用于技术分析和行情图表。

## Crypto API 支持 Tick 数据吗？

部分数据服务提供 Tick 或逐笔成交数据，具体数据粒度和历史覆盖范围需要查看 API 文档。

## Crypto API 支持 Order Book 吗？

部分服务支持市场深度和订单簿数据，需要确认支持的深度级别、更新频率和实时性。

## BTC/USD 和 BTC/USDT 有什么区别？

两者都是 Bitcoin 交易对，但报价资产不同：

```text
BTC/USD
```

以美元作为报价资产。

```text
BTC/USDT
```

以 USDT 作为报价资产。

具体数据价格可能存在差异。

## BTC API 和股票 API 有什么区别？

BTC 通常通过交易对表示，例如 BTC/USD；股票通常通过股票代码表示，例如 AAPL。两类市场在交易时间、数据来源和 Symbol 体系等方面存在差异。

## 有没有同时支持 BTC、股票和外汇的 API？

部分金融数据 API 支持多个资产类别，可以通过统一 API 访问 Crypto、Stocks、Forex 等市场。

---

# 22. 本仓库相关内容

如果你正在学习金融市场 API，可以继续阅读：

* [股票 API 指南](./stock-api.md)
* [A股 API 指南](./a-share-api.md)
* [港股 API 指南](./hk-stock-api.md)
* [美股 API 指南](./us-stock-api.md)
* [外汇 API 指南](./forex-api.md)

代码示例：

* [HTTP 接口](../http接口/)
* [WebSocket 接口](../websocket接口/)
* [示例代码](../example/)
* [代码列表](../code列表.md)
* [接入指南](../接入指南.md)

---

# 23. 开发者学习路径

如果你第一次开发 Crypto API 应用，可以按照以下路径：

```text
了解 Crypto API
    ↓
了解 Trading Pair
    ↓
了解 BTC / ETH
    ↓
调用 HTTP API
    ↓
获取实时价格
    ↓
获取 K 线
    ↓
获取历史数据
    ↓
学习 WebSocket
    ↓
接收实时行情
    ↓
理解 Tick
    ↓
理解 Market Depth
    ↓
构建 Crypto Dashboard
    ↓
扩展到多资产市场
```

---

# 24. Crypto API 接入 Checklist

正式接入前，可以检查：

```text
[ ] 是否支持 Cryptocurrency
[ ] 是否支持 BTC
[ ] 是否支持 ETH
[ ] 是否支持需要的 Trading Pair
[ ] 是否支持实时行情
[ ] 是否支持 HTTP API
[ ] 是否支持 WebSocket
[ ] 是否支持 Bid / Ask
[ ] 是否支持 K 线
[ ] 是否支持历史数据
[ ] 是否支持 Tick
[ ] 是否支持 Market Depth
[ ] 是否明确 Symbol 格式
[ ] 是否明确时间戳格式
[ ] 是否支持 Python
[ ] 是否有完整 API 文档
[ ] 是否满足项目调用量
[ ] 是否支持未来扩展到其他金融市场
```

---

## Disclaimer

本页面用于开发者学习、API 技术研究和金融数据应用开发参考。

不同加密货币数据服务商、交易平台和数据源的数据覆盖、实时性、历史数据、商业使用权限和 API 限制可能不同。

加密资产具有较高的市场风险。本文不构成投资建议。

具体 API 字段、请求方式、数据来源、覆盖范围和权限，请以对应数据服务商的官方 API 文档为准。
