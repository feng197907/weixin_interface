import requests

class Util:
    def get_token(self):
        request_params = {
            "corpid": 'wwf4a25d59655a5e0b',
            "corpsecret": '3FeUoe8bU4AK_xu4hGKNFZmTApxOcsZz4icR0nPHui8'
        }

        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=request_params)

        # print(res.json()['access_token'])
        return res.json()['access_token']