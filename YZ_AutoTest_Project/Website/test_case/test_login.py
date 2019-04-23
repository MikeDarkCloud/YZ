from Website.test_case.page_object.LoginPage import *
from time import sleep
from myunit import *
from Log import *

class LoginTest(StartEnd):
    @unittest.skip('skip this case')
    def test_register1_normal_1(self):
        '''登陆测试'''
        try:
            Log().info("开始执行教务系统登录测试！")
            LoginPage(self.driver).open()
            Log().info("输入用户名！")
            LoginPage(self.driver).type_username("蓝明勇")
            Log().info("输入密码！")
            LoginPage(self.driver).type_password('Yz123456')
            sleep(2)
            LoginPage(self.driver).type_submit()
            sleep(5)
            self.assertTrue(LoginPage(self.driver).type_loginPass_hint(), msg=None)
        except Exception as e:
            self.assertTrue(LoginPage(self.driver).type_loginPass_hint(), msg=None)
            Log().info("执行登录过程失败！！！！！！！！！！！！！！！！")



if __name__ == '__main__':
    unittest.main()






