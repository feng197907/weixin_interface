
import re
import random

import requests
import json
import pytest
from test_data.wework_data import Wework_data


def test_wework_data():
    # 用列表生成器生成数据
    # userid,name,mobile
    data = [('user_' + str(x),
             'test_' + str(x),
             '138%08d'%x) for x in range(3)]
    print(data)
    return data


class TestWework:

    # def setup(self):
    #     test_data = Wework_data()




    @pytest.fixture(scope="session")
    def token(self):
        request_params = {
            "corpid": 'wwf4a25d59655a5e0b',
            "corpsecret": '3FeUoe8bU4AK_xu4hGKNFZmTApxOcsZz4icR0nPHui8'
        }

        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=request_params)

        # print(res.json()['access_token'])
        return res.json()['access_token']

    def get_token(self):
        """
        获取 token
        :return:
        url:https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        """
        request_params = {
            "corpid": 'wwf4a25d59655a5e0b',
            "corpsecret": '3FeUoe8bU4AK_xu4hGKNFZmTApxOcsZz4icR0nPHui8'
        }

        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=request_params)

        # print(res.json()['access_token'])
        return res.json()['access_token']

    def test_create(self, token, userid, name, moblie, department=None):
        """
        创建成员
        :return:
        URL：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        """
        if department == None:
            department = [1]

        # ACCESS_TOKEN = self.get_token()
        request_body = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": moblie}
        # print(json.dumps(request_body))
        res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}', json=request_body
                            )
        print(res.json())
        return res.json()

    def test_get_member(self, token, userid):
        """
        获取成员信息
        :return:
        url:https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        """
        ACCESS_TOKEN = self.get_token()
        res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}')

        print(res.json())
        return res.json()

    def test_update_member(self, token, userid, name):
        """
        更新成员信息
        :return:
        url:https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        """
        # ACCESS_TOKEN = self.get_token()

        request_data = {
            "userid": userid,
            "name": name
        }

        res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}', json=request_data)
        print(res.json())
        return res.json()

    def test_delete_member(self, token, userid):
        """
        删除成员
        :return:
        url:https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        """
        # ACCESS_TOKEN = self.get_token()
        res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}')
        print(res.json())
        return res.json()

    @pytest.mark.parametrize("userid,name,mobile", test_wework_data())
    def test_member_wework(self, token, userid, name, mobile):

        # 创建成员

        # try:
        #     assert 'created' == self.test_create(token, userid, name, mobile)['errmsg']
        # except AssertionError as e:
        #     # print(e)
        #     if 'mobile existed' in e.__str__():
        #         # 提取绑定已有手机号的id
        #         # re_userid = re.findall(":.*'$", e.__str__())[0]
        #         lin_str = e.__str__().split(':')[1]
        #         num = len(lin_str)-1
        #         re_userid = lin_str[:num]
        #         # print(type(re_userid))
        #         print(re_userid)
        #         # 删除 此成员
        #         self.test_delete_member(token, re_userid)
        #         assert 'created' == self.test_create(token, userid, name, mobile)['errmsg']

        # 添加成员
        assert 'created' == self.test_create(token, userid, name, mobile)["errmsg"]

        # 查询成员信息
        assert name == self.test_get_member(token, userid)["name"]

        # 更新成员信息
        assert 'updated' == self.test_update_member(token, userid, '测试修改')["errmsg"]
        assert "测试修改" == self.test_get_member(token, userid)["name"]

        # 删除成员
        assert 'deleted' == self.test_delete_member(token, userid)["errmsg"]
