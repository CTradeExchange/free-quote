import requests	# pip3 install requests
import json

# 将如下字段信息进行url的encode，复制到url的查询字符串的query里
"""
{
	'trace' : '3baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806',
	'data' : {
		'code' : '9988-HK',
		'kline_type' : 1,
		'kline_timestamp_end' : 0,
		'query_kline_num' : 2,
        'adjust_type': 0
	}
}

{
	'trace' : '3baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806',
	'data' : {
		'code' : 'WELL-US',
		'kline_type' : 1,
		'kline_timestamp_end' : 0,
		'query_kline_num' : 2,
        'adjust_type': 0
	}
}

{
	'trace' : '3baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806',
	'data' : {
		'code' : 'TITN-US',
		'kline_type' : 1,
		'kline_timestamp_end' : 0,
		'query_kline_num' : 2,
        'adjust_type': 0
	}
}
"""

# Base URL being accessed
#test_url = 'https://quote.aatest.online/quote-stock-b-api/kline?token=2a07d971-47f8-4c1a-93e2-fbcb2f2aa8ab-1688867929754&query=%7B%09%27trace%27%20%3A%20%273baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806%27%2C%09%27data%27%20%3A%20%7B%09%09%27code%27%20%3A%20%279988-HK%27%2C%09%09%27kline_type%27%20%3A%201%2C%09%09%27kline_timestamp_end%27%20%3A%200%2C%09%09%27query_kline_num%27%20%3A%202%2C%20%20%20%20%20%20%20%20%27adjust_type%27%3A%200%09%7D%7D'
#test_url = 'https://quote.aatest.online/quote-stock-b-api/kline?token=2a07d971-47f8-4c1a-93e2-fbcb2f2aa8ab-1688867929754&query=%7B%09%27trace%27%20%3A%20%273baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806%27%2C%09%27data%27%20%3A%20%7B%09%09%27code%27%20%3A%20%27WELL-US%27%2C%09%09%27kline_type%27%20%3A%201%2C%09%09%27kline_timestamp_end%27%20%3A%200%2C%09%09%27query_kline_num%27%20%3A%202%2C%20%20%20%20%20%20%20%20%27adjust_type%27%3A%200%09%7D%7D'
test_url = 'https://quote.aatest.online/quote-stock-b-api/kline?token=2a07d971-47f8-4c1a-93e2-fbcb2f2aa8ab-1688867929754&query=%7B%09%27trace%27%20%3A%20%273baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806%27%2C%09%27data%27%20%3A%20%7B%09%09%27code%27%20%3A%20%27NINE-US%27%2C%09%09%27kline_type%27%20%3A%201%2C%09%09%27kline_timestamp_end%27%20%3A%200%2C%09%09%27query_kline_num%27%20%3A%202%2C%20%20%20%20%20%20%20%20%27adjust_type%27%3A%200%09%7D%7D'

# Extra headers
test_headers = {
    'Content-Type' : 'application/json'
}

resp = requests.get(url=test_url, headers=test_headers)

# Decoded text returned by the request
text = resp.text
print(text)