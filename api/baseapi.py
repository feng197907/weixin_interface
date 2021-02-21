import json

import requests

class BaseApi:
    params = {}

    def send(self, data):
        raw_data = json.dumps(data)

        for key, value in self.params.items():
            # print(key, value)
            # 测试数据调用变量
            raw_data = raw_data.replace("${"+key+"}", value)

        data = json.loads(raw_data)
        return requests.request(**data).json()