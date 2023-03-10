import requests	# pip3 install requests
import json

# Base URL being accessed
test_url = 'https://quote.tradeswitcher.com/quote-stock-api/kline?token=e945d7d9-9e6e-4721-922a-7251a9d311d0-1678159756806'

# Dictionary of query parameters (if any)
test_parms = {
	'trace' : '3baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806',
	'data' : {
		'code' : '857.HK',
		'kline_type' : 1,
		'kline_timestamp_end' : 0,
		'query_kline_num' : 2
	}
}

# Extra headers
test_headers = {
    'Content-Type' : 'application/json'
}

resp = requests.post(url=test_url, headers=test_headers, data=json.dumps(test_parms))

# Decoded text returned by the request
text = resp.text
print(text)