## GET K线查询

GET /quote-stock-api/kline

> Body 请求参数

```json
{
  "trace": "culpa cillum ea reprehenderit occaecat",
  "data": {
    "code": "857.HK",
    "kline_type": 1,
    "kline_timestamp_end": 0,
    "query_kline_num": 2
  }
}
```

### 请求参数

| 名称                   | 位置  | 类型    | 必选 | 说明                                                         |
| ---------------------- | ----- | ------- | ---- | ------------------------------------------------------------ |
| token                  | query | string  | 否   |                                                          |
| body                   | body  | object  | 否   |                                                          |
| » trace                | body  | string  | 是   | 跟踪号                                                       |
| » data                 | body  | object  | 是   |                                                          |
| »» code                | body  | string  | 是   | 代码                                                         |
| »» kline_type          | body  | integer | 是   | k线类型，1分钟K，2为5分钟K，3为15分钟K，4为30分钟K，5为小时K，6为2小时K，7为4小时K，8为日K，9为周K，10为月K |
| »» kline_timestamp_end | body  | integer | 是   | K线结束时间戳，单位秒                                        |
| »» query_kline_num     | body  | integer | 是   | 查询K线数量，最大查询1000根                                  |

> 返回示例

> OK

```json
{
  "ret": 200,
  "msg": "ok",
  "trace": "asdfsdfa",
  "data": {
    "code": "857.HK",
    "kline_type": 1,
    "kline_list": [
      {
        "timestamp": "1677829200",
        "open_price": "136.421",
        "close_price": "136.412",
        "high_price": "136.422",
        "low_price": "136.407",
        "volume": "0",
        "turnover": "0"
      },
      {
        "timestamp": "1677829260",
        "open_price": "136.412",
        "close_price": "136.401",
        "high_price": "136.415",
        "low_price": "136.397",
        "volume": "0",
        "turnover": "0"
      }
    ]
  }
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | OK   | Inline   |

### 返回数据结构

状态码 **200**

| 名称            | 类型     | 必选 | 约束 | 中文名 | 说明                                                         |
| --------------- | -------- | ---- | ---- | ------ | ------------------------------------------------------------ |
| » ret           | integer  | true |  |        |                                                          |
| » msg           | string   | true |  |        |                                                          |
| » trace         | string   | true |  |        |                                                          |
| » data          | object   | true |  |        |                                                          |
| »» code         | string   | true |  |        | 代码                                                         |
| »» kline_type   | integer  | true |  |        | k线类型，1分钟K，2为5分钟K，3为15分钟K，4为30分钟K，5为小时K，6为2小时K，7为4小时K，8为日K，9为周K，10为月K |
| »» kline_list   | [object] | true |  |        |                                                          |
| »»» timestamp   | string   | true |  |        | 该K线时间戳                                                  |
| »»» open_price  | string   | true |  |        | 该K线开盘价                                                  |
| »»» close_price | string   | true |  |        | 该K线收盘价                                                  |
| »»» high_price  | string   | true |  |        | 该K线最高价                                                  |
| »»» low_price   | string   | true |  |        | 该K线最低价                                                  |
| »»» volume      | string   | true |  |        | 该K线成交数量                                                |
| »»» turnover    | string   | true |  |        | 该K线成交金额                                                |
