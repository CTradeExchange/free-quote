package main

import (
	"log"

	"io/ioutil"

	"net/http"
)

func http_example() {

	/*
		将如下JSON进行url的encode，复制到http的查询字符串的query字段里
		{"trace" : "go_http_test1","data" : {"code" : "700.HK","kline_type" : 1,"kline_timestamp_end" : 0,"query_kline_num" : 2,"adjust_type": 0}}
	*/
	url := "http://quote.aatest.online/quote-stock-b-api/kline?token=e945d7d9-9e6e-4721-922a-7251a9d311d0-1678159756806&query=%7B%22trace%22%20%3A%20%22go_http_test1%22%2C%22data%22%20%3A%20%7B%22code%22%20%3A%20%22700.HK%22%2C%22kline_type%22%20%3A%201%2C%22kline_timestamp_end%22%20%3A%200%2C%22query_kline_num%22%20%3A%202%2C%22adjust_type%22%3A%200%7D%7D"
	log.Println("请求内容：", url)
	resp, err := http.Get(url)

	if err != nil {

		log.Println("请求失败：", err)

		return

	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)

	if err != nil {

		log.Println("读取响应失败：", err)

		return

	}

	log.Println("响应内容：", string(body))

}
