from api.baseapi import BaseApi
from api.util import Util
import yaml

class WeWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../test_data/wework.yaml", encoding="utf-8") as f:
            self.data = yaml.load(f)
            print(self.data)

    def test_create(self, userid, name, moblie, department=None):
        """
        创建成员
        :return:
        URL：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        """
        if department == None:
            department = '1'

        # request_body = {
        #     "userid": userid,
        #     "name": name,
        #     "department": department,
        #     "mobile": moblie}
        # print(json.dumps(request_body))

        self.params['userid'] = userid
        self.params['name'] = name
        self.params['mobile'] = moblie
        self.params['department'] = department
        # res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}', json=request_body
        return self.send(self.data["test_create"])


    def test_get_member(self, userid):
        """
        获取成员信息
        :return:
        url:https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        """
        # ACCESS_TOKEN = self.get_token()
        self.params['userid'] = userid
        # res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}')
        return self.send(self.data['test_get'])


    def test_update_member(self, userid, name):
        """
        更新成员信息
        :return:
        url:https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        """
        # ACCESS_TOKEN = self.get_token()

        # request_data = {
        #     "userid": userid,
        #     "name": name
        # }
        self.params['userid'] = userid
        self.params['name'] = name

        # res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}', json=request_data)
        return self.send(self.data['test_update'])

    def test_delete_member(self, userid):
        """
        删除成员
        :return:
        url:https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        """
        # ACCESS_TOKEN = self.get_token()
        self.params['userid'] = userid
        # res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}')
        return self.send(self.data['test_delete'])