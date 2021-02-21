from api.wework import WeWork
import pytest

def test_wework_data():
    # 用列表生成器生成数据
    # userid,name,mobile
    data = [('user_' + str(x),
             'test_' + str(x),
             '138%08d'%x) for x in range(3)]
    print(data)
    return data


class TestWework:
    @pytest.mark.parametrize("userid, name, moblie", test_wework_data())
    def test_create(self,userid, name, moblie):
        WeWork().test_create(userid, name, moblie)