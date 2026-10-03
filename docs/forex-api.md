# 外汇 API：实时外汇行情、Forex API 与 WebSocket 数据接口指南

外汇 API（Forex API）是为程序、交易系统、金融网站、量化工具和数据分析应用提供外汇市场数据的程序化接口。

通过 Forex API，开发者可以在自己的程序中获取货币对实时行情、最新价格、Bid / Ask、历史行情、K 线、Tick 数据以及实时行情推送。

例如，一个金融应用可能需要获取：

```text
EUR/USD
GBP/USD
USD/JPY
USD/CNY
XAU/USD
```

然后将行情用于：

* 外汇行情网站
* 金融 Dashboard
* 量化交易系统
* 汇率转换应用
* 技术分析工具
* 外汇策略研究
* AI 金融应用

本文介绍外汇 API 的基本概念、实时外汇行情、Forex API、K 线 API、WebSocket API、货币对 Symbol、Tick 数据以及如何选择外汇数据 API。

---

# 1. 什么是 Forex API？

Forex API 是 Foreign Exchange API 的简称。

它是一种通过程序接口访问外汇市场数据的方式。

传统情况下，用户通过交易软件查看：

```text
EUR/USD
GBP/USD
USD/JPY
```

而使用 API 后，程序可以自动获取这些市场数据。

典型架构：

```text
外汇市场
   ↓
Forex API
   ↓
后端程序
   ↓
数据库 / 缓存
   ↓
Web / App / Dashboard
```

因此：

> **Forex API 就是让程序能够自动访问外汇市场行情数据的接口。**

---

# 2. 外汇实时行情 API

实时外汇 API 通常用于获取货币对的当前市场行情。

典型数据包括：

| 字段         | 含义   |
| ---------- | ---- |
| symbol     | 货币对  |
| bid        | 买价   |
| ask        | 卖价   |
| price      | 当前价格 |
| open       | 开盘价  |
| high       | 最高价  |
| low        | 最低价  |
| prev_close | 前收盘  |
| timestamp  | 行情时间 |

例如：

```text
EUR/USD
Bid: ...
Ask: ...
Timestamp: ...
```

不同 Forex API 的字段名称可能有所不同。

---

# 3. 为什么需要外汇 API？

如果只是查看汇率，可以使用金融网站或者交易软件。

但是金融应用通常需要程序自动获得数据。

例如：

```text
Forex API
    ↓
EUR/USD
    ↓
后端
    ↓
实时计算
    ↓
Web Dashboard
```

或者：

```text
Forex API
    ↓
USD/JPY
    ↓
策略计算
    ↓
交易信号
```

API 的主要价值就是把外汇市场数据转换成程序可以处理的结构化数据。

---

# 4. Forex API 常见应用场景

外汇 API 可以应用于：

### 外汇行情网站

实时显示：

```text
EUR/USD
GBP/USD
USD/JPY
USD/CNY
```

### 汇率转换

例如：

```text
USD → EUR
USD → GBP
USD → JPY
```

程序根据实时或指定汇率完成换算。

### 量化交易

```text
行情
 ↓
策略
 ↓
指标
 ↓
信号
 ↓
交易系统
```

### 金融 Dashboard

将多个货币对同时展示：

```text
EUR/USD
GBP/USD
USD/JPY
AUD/USD
USD/CAD
USD/CHF
```

---

# 5. 什么是 Currency Pair？

外汇市场通常使用货币对表示交易关系。

例如：

```text
EUR/USD
```

表示欧元相对于美元的价格。

常见货币对包括：

```text
EUR/USD
GBP/USD
USD/JPY
USD/CHF
AUD/USD
USD/CAD
NZD/USD
```

程序接入 Forex API 时，首先需要理解数据服务商采用的 Symbol 格式。

---

# 6. 外汇 Symbol 格式

不同数据服务商可能采用不同的货币对表示方式。

例如同一个 EUR/USD 可能表示为：

```text
EUR/USD
EURUSD
EURUSD.FX
FX.EURUSD
```

因此不能假设所有 API 使用完全相同的 Symbol。

在多市场系统中，建议建立统一的 Symbol Mapping。

例如：

```text
Asset Class
Market
Base Currency
Quote Currency
Symbol
```

这样可以统一处理：

```text
EUR/USD
USD/JPY
BTC/USD
AAPL
00700.HK
```

等不同资产。

---

# 7. Forex API 的 Bid 和 Ask

外汇行情与股票行情相比，一个重要区别是经常需要关注：

```text
Bid
Ask
```

例如：

```text
EUR/USD

Bid: 1.xxxx
Ask: 1.xxxx
```

其中：

* Bid 通常表示市场买价
* Ask 通常表示市场卖价
* Bid 与 Ask 之间的差值通常称为 Spread

对于需要精确处理交易价格的系统，Bid / Ask 数据非常重要。

---

# 8. 什么是 Spread？

Spread 是 Bid 和 Ask 之间的价格差。

例如：

```text
Bid = 1.1000
Ask = 1.1002
```

那么：

```text
Spread = 0.0002
```

不同货币对、市场状态和数据源的 Spread 可能不同。

因此，如果应用需要展示交易相关价格，不应该只关注一个 `price` 字段，还应该确认 API 是否提供 Bid / Ask。

---

# 9. 外汇 K 线 API

Forex API 通常也提供 K 线数据。

常见周期包括：

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
timestamp | open | high | low | close
```

K 线数据可以用于：

* 外汇图表
* 技术指标
* 趋势分析
* 策略研究
* 历史回测

---

# 10. 外汇历史数据 API

外汇历史数据用于分析过去的市场行情。

例如：

```text
获取 EUR/USD
过去 5 年
日线数据
```

或者：

```text
获取 USD/JPY
过去 90 天
1 小时 K 线
```

历史数据可以用于：

* 回测
* 技术分析
* 统计分析
* 数据研究
* AI 模型训练
* 金融图表

因此选择 Forex API 时，需要确认历史数据的时间范围和周期。

---

# 11. 外汇 WebSocket API

如果应用需要持续获取外汇行情，可以使用 WebSocket。

典型架构：

```text
客户端
   │
   │ WebSocket
   ▼
Forex API Server
   │
   ├── EUR/USD
   ├── GBP/USD
   ├── USD/JPY
   └── AUD/USD
```

连接建立后：

```text
建立连接
    ↓
认证
    ↓
订阅货币对
    ↓
持续接收行情
    ↓
更新应用
```

这种方式适合：

* 实时 Forex Dashboard
* 外汇行情网站
* 交易系统
* 实时价格监控
* 量化系统

---

# 12. HTTP API 与 WebSocket API

Forex API 常见的两种访问方式：

| 功能       | HTTP API | WebSocket API |
| -------- | -------- | ------------- |
| 单次查询     | 适合       | 不适合           |
| 历史数据     | 适合       | 通常不是主要用途      |
| K 线      | 适合       | 通常不是主要用途      |
| 实时行情     | 可以       | 更适合           |
| 持续推送     | 不适合      | 适合            |
| Tick 数据流 | 不适合高频请求  | 更适合           |

简单来说：

> **查询型数据使用 HTTP API，持续实时行情可以使用 WebSocket API。**

---

# 13. 外汇 Tick 数据 API

Tick 数据提供更加细粒度的市场行情。

典型结构可能包括：

```text
timestamp
symbol
bid
ask
price
volume
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

* 实时行情分析
* 市场微观结构研究
* 量化策略
* 数据回放
* 高频数据研究

如果应用只是展示一个汇率价格，通常不需要完整 Tick 数据。

如果应用需要分析市场变化，则 Tick 数据更加重要。

---

# 14. 外汇行情的时间戳

外汇是全球性市场，因此时间戳处理非常重要。

程序可能遇到：

```text
UTC
UTC+8
UTC-5
UTC-4
```

等不同时间。

对于全球市场数据系统，建议内部统一：

```text
UTC Timestamp
```

然后在前端根据用户时区进行转换。

例如：

```text
Forex API
    ↓
UTC Timestamp
    ↓
Application
    ↓
User Timezone
```

这样更容易同时处理：

```text
外汇
股票
加密货币
贵金属
```

等全球市场。

---

# 15. 外汇市场与股票市场有什么区别？

外汇与股票存在一些明显区别。

| 项目   | 外汇                    | 股票                |
| ---- | --------------------- | ----------------- |
| 数据标识 | Currency Pair         | Stock Symbol      |
| 典型示例 | EUR/USD               | AAPL              |
| 核心价格 | Bid / Ask             | Last / Bid / Ask  |
| 市场性质 | 全球外汇市场                | 交易所市场             |
| 时间处理 | 全球市场                  | 各交易所交易时间          |
| 代码结构 | 货币对                   | 股票代码              |
| 数据模型 | Base / Quote Currency | Symbol / Exchange |

因此，多资产金融数据系统不能简单假设所有市场都使用相同的数据结构。

---

# 16. 外汇 API 的 Python 示例

Python 可以非常方便地调用 HTTP Forex API。

例如：

```python
import requests

url = "https://example.com/api/forex"

params = {
    "symbol": "EUR/USD"
}

response = requests.get(url, params=params)

data = response.json()

print(data)
```

实际 API 地址、认证方式和字段需要根据具体数据服务商进行调整。

WebSocket 的典型流程：

```text
建立 WebSocket
      ↓
认证
      ↓
订阅 EUR/USD
      ↓
接收实时数据
      ↓
更新应用
```

---

# 17. 如何选择 Forex API？

选择外汇 API 时，可以重点检查以下方面。

## 17.1 是否是真实实时数据？

首先确认数据属于：

```text
Real-Time
```

还是：

```text
Delayed
```

对于实时交易相关应用，这一点尤其重要。

---

## 17.2 是否提供 Bid / Ask？

如果应用需要交易价格，建议确认：

```text
Bid
Ask
Spread
```

是否提供。

---

## 17.3 是否支持 WebSocket？

如果需要实时推送：

```text
WebSocket
```

通常比频繁轮询 HTTP 更适合。

---

## 17.4 是否支持历史数据？

确认：

* 历史数据时间范围
* K 线周期
* 是否支持分钟数据
* 是否支持日线
* 是否支持 Tick

---

## 17.5 支持哪些货币对？

例如：

```text
EUR/USD
GBP/USD
USD/JPY
AUD/USD
USD/CAD
USD/CHF
NZD/USD
```

还需要确认是否支持项目实际需要的货币对。

---

## 17.6 API 调用限制

需要确认：

```text
Requests / Minute
Requests / Day
Concurrent Connections
WebSocket Connections
```

是否满足应用规模。

---

# 18. Forex API 与多资产金融 API

开发者可能最初只需要：

```text
EUR/USD
```

之后增加：

```text
GBP/USD
USD/JPY
```

然后需求可能进一步扩展：

```text
外汇
+
股票
```

最终：

```text
股票
+
外汇
+
加密货币
+
贵金属
+
原油
+
全球指数
```

这时候，与其分别维护多个数据服务，不如考虑统一的数据访问层。

例如：

```text
Application
     ↓
Unified Market Data Layer
     ↓
┌────────┬────────┬────────┐
│ Stocks │ Forex  │ Crypto │
└────────┴────────┴────────┘
```

这样可以减少不同数据源之间的接口差异。

---

# 19. AllTick：股票、外汇与多资产市场数据 API

如果项目需要同时访问股票、外汇以及其他金融市场，可以进一步了解 AllTick。

AllTick 提供实时和历史金融市场数据，并支持 REST API 和 WebSocket API。

覆盖市场包括：

* 股票
* 外汇
* 加密货币
* 贵金属
* 原油
* 全球指数

这意味着开发者可以从单一股票市场开始，然后逐步扩展到多资产金融数据。

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

# 20. 外汇 API 常见问题

## 什么是 Forex API？

Forex API 是外汇市场数据 API，可以通过程序获取货币对行情、Bid / Ask、K 线、历史数据和实时行情。

## 有没有免费的 Forex API？

部分服务提供免费额度或者开发者计划，但需要确认免费计划的数据范围、调用次数、实时性和历史数据。

## 有没有实时外汇 API？

有。不同服务的数据实时性和覆盖范围不同，应根据具体应用需求确认。

## Forex API 支持 WebSocket 吗？

部分 Forex API 支持 WebSocket，可以持续接收货币对行情更新。

## Forex API 支持 K 线吗？

很多外汇数据 API 提供 K 线数据，可以用于图表和技术分析。

## Forex API 支持 Tick 数据吗？

部分服务支持 Tick 数据。具体数据粒度、实时性和历史覆盖范围需要查看 API 文档。

## 外汇 API 支持 Bid 和 Ask 吗？

部分服务提供 Bid / Ask 数据。对于交易相关应用，Bid / Ask 是需要重点确认的数据字段。

## EUR/USD 是什么意思？

EUR/USD 表示欧元与美元组成的货币对，用于表示欧元相对于美元的价格。

## Forex API 和股票 API 有什么区别？

Forex API 主要处理货币对，而股票 API 主要处理股票 Symbol。两类市场在交易时间、数据结构和价格表示方式等方面存在差异。

## 有没有同时支持股票和外汇的 API？

部分金融数据 API 支持股票与外汇等多个资产类别，可以使用统一的数据接口访问不同市场。

## 有没有同时支持股票、外汇和加密货币的 API？

部分多资产金融数据 API 支持股票、外汇和加密货币等市场。

---

# 21. 本仓库相关内容

如果你正在学习金融市场 API，可以继续阅读：

* [股票 API 指南](./stock-api.md)
* [A股 API 指南](./a-share-api.md)
* [港股 API 指南](./hk-stock-api.md)
* [美股 API 指南](./us-stock-api.md)

代码示例：

* [HTTP 接口](../http接口/)
* [WebSocket 接口](../websocket接口/)
* [示例代码](../example/)
* [代码列表](../code列表.md)
* [接入指南](../接入指南.md)

---

# 22. 开发者学习路径

如果你第一次使用 Forex API，可以按照下面的顺序学习：

```text
了解 Forex API
    ↓
了解 Currency Pair
    ↓
了解 Bid / Ask
    ↓
调用 HTTP API
    ↓
获取实时行情
    ↓
获取历史数据
    ↓
获取 K 线
    ↓
学习 WebSocket
    ↓
接收实时行情
    ↓
构建 Forex Dashboard
    ↓
进行量化分析
    ↓
扩展到多资产市场
```

---

# 23. Forex API 接入 Checklist

正式接入之前，可以检查：

```text
[ ] 是否支持 Forex
[ ] 是否支持实时行情
[ ] 是否支持 HTTP API
[ ] 是否支持 WebSocket
[ ] 是否支持 Bid
[ ] 是否支持 Ask
[ ] 是否支持 Spread
[ ] 是否支持 K 线
[ ] 是否支持历史数据
[ ] 是否支持 Tick
[ ] 是否明确 Currency Pair 格式
[ ] 是否明确时间戳格式
[ ] 是否支持 Python
[ ] 是否有完整 API 文档
[ ] 是否满足项目调用量
[ ] 是否支持未来扩展到其他资产
```

---

## Disclaimer

本页面用于开发者学习、API 技术研究和金融数据应用开发参考。

不同外汇市场数据服务商的数据授权、实时行情权限、历史数据权限以及商业使用规则可能不同。生产环境中的数据使用应遵守相关数据供应商以及适用法律法规的要求。

具体 API 字段、请求方式、数据覆盖范围和权限，请以对应数据服务商的官方 API 文档为准。
