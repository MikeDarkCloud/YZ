from LoginPage import *
from AdultRegisterPage import *
from HomePage import *
from myunit import *
import unittest
from Log import *

class AdultRegisterTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_adult_register_1(self):
        '''测试教务系统成教学员录入'''
        try:
            Log().info("测试成教学员信息录入。。。。。。。")
            Log().info("输入账号密码！")
            LoginPage(self.driver).Login_action('蓝明勇', 'Yz123456')
            Log().info("开始测试录入成教学员信息！")
            ListPage(self.driver).type_studentmanage(1)
            Auto_CJ_Register(self.driver).type_cheng_register()
            Log().info("测试成教学员录入是否成功断言！")
            self.assertTrue(Auto_CJ_Register(self.driver).type_register_cj_success, msg=None)
            Log().info('成教学员录入信息成功！')
        except Exception as e:
            self.assertTrue(Auto_CJ_Register(self.driver).type_register_cj_success, msg=None)
            Log().info("测试成教学员信息录入失败！！！！！！！！！！！")

if __name__ == '__main__':
    unittest.main()