import json
import websocket    # pip install websocket-client

class Feed(object):

    def __init__(self):
<<<<<<< HEAD:example/websocket_request.py
        self.url = 'wss://quote.aatest.online/quote-b-ws-api?token=3662a972-1a5d-4bb1-88b4-66ca0c402a03-1688712831841'
        #self.url = 'wss://quote.aatest.online/quote-b-ws-api?token=a9037628-30ae-4ffa-bd3c-9f7beaf1d44d-1688712831666'      # 这里输入websocket的url
=======
        self.url = 'wss://quote.aatest.online/quote-stock-b-ws-api?token=e945d7d9-9e6e-4721-922a-7251a9d311d0-1678159756806'  # 这里输入websocket的url
>>>>>>> cb01ae1482e0c2f5637228f2aebd652618f56ae7:example/python/websocket_python_example.py
        self.ws = None

    def on_open(self, ws):
        """
        Callback object which is called at opening websocket.
        1 argument:
        @ ws: the WebSocketApp object
        """
        print('A new WebSocketApp is opened!')

        # 开始订阅（举个例子）
        sub_param = {
            "cmd_id": 22002, 
            "seq_id": 123,
            "trace":"3baaa938-f92c-4a74-a228-fd49d5e2f8bc-1678419657806",
            "data":{
                "symbol_list":[
                    {
<<<<<<< HEAD:example/websocket_request.py
                        "code": "ETHUSDT",
                        "depth_level": 5,
                    },
                    {
                        "code": "GBPJPY",
=======
                        "code": "700.HK",
                        "depth_level": 5,
                    },
                    {
                        "code": "UNH.US",
>>>>>>> cb01ae1482e0c2f5637228f2aebd652618f56ae7:example/python/websocket_python_example.py
                        "depth_level": 5,
                    }
                ]
            }
        }
        
        #如果希望长时间运行，除了需要发送订阅之外，还需要修改代码，定时发送心跳，避免连接断开，具体查看接口文档
        sub_str = json.dumps(sub_param)
        ws.send(sub_str)
        print("depth quote are subscribed!")

    def on_data(self, ws, string, type, continue_flag):
        """
        4 argument.
        The 1st argument is this class object.
        The 2nd argument is utf-8 string which we get from the server.
        The 3rd argument is data type. ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY will be came.
        The 4th argument is continue flag. If 0, the data continue
        """

    def on_message(self, ws, message):
        """
        Callback object which is called when received data.
        2 arguments:
        @ ws: the WebSocketApp object
        @ message: utf-8 data received from the server
        """
        # 对收到的message进行解析
        result = eval(message)
        print(result)

    def on_error(self, ws, error):
        """
        Callback object which is called when got an error.
        2 arguments:
        @ ws: the WebSocketApp object
        @ error: exception object
        """
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        """
        Callback object which is called when the connection is closed.
        2 arguments:
        @ ws: the WebSocketApp object
        @ close_status_code
        @ close_msg
        """
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    feed = Feed()
    feed.start()
