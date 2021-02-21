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
    def test_wework(self, userid, name, moblie):
        # 添加
        print(WeWork().test_create(userid, name, moblie))
        # assert 'created' == WeWork().test_create(userid, name, moblie)['errmsg']
        # 查询
        print(WeWork().test_get_member(userid))
        # assert name == WeWork().test_get_member(userid)['name']
        # 更新
        print(WeWork().test_update_member(userid,"测试修改"))
        # assert 'updated' == WeWork().test_update_member(userid,"测试修改")['errmsg']

        # 查询修改后
        print(WeWork().test_get_member(userid))
        # assert "测试修改" == WeWork().test_get_member(userid)['name']

        # 删除
        print(WeWork().test_delete_member(userid))
        # assert 'deleted' == WeWork().test_delete_member(userid)['errmsg']


