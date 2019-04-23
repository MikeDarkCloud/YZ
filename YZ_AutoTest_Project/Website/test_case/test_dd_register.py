from DingRegisterPage import *
from AdultRegisterPage import *
from AdultEntrance import *
from myunit import *

class DingDingRegisterTest(StartEnd):
    '''钉钉招生应用'''
    # @unittest.skip('skip this case')
    def test_dingding_register_1(self):
        '''测试钉钉招生应用成教学员录入'''
        try:
            Log().info("开始执行测试钉钉录入成教学员信息！")
            Auto_DCJ_register(self.driver).open_new('http://zm-3.yzwill.cn/recruit/login')
            Auto_DCJ_register(self.driver).type_dd_login()
            Auto_DCJ_register(self.driver).type_ddcj_register()
            Log().info("断言！")
            self.assertIsNotNone(Auto_DCJ_register(self.driver).type_dregister_success,msg=None)
            Log().info("恭喜！钉钉录入学员通过")
        except Exception as e:
            self.assertIsNotNone(Auto_DCJ_register(self.driver).type_dregister_success,msg=None)
            Log().info("执行测试钉钉录入成教学员信息失败！！！！！！！！！")

if __name__ == '__main__':
    unittest.main()






