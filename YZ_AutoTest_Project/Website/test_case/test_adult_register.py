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
        print("test_cj_register_normal is start test..")
        po1=LoginPage(self.driver)
        log = Log()
        log.info("输入账号密码！")
        po1.Login_action('autotester1', 'Yz123456')
        log.info("开始测试录入成教学员信息！")
        po2 = Auto_CJ_Register(self.driver)
        po3 = ListPage(self.driver)
        po3.type_studentmanage(1)
        po2.type_cheng_register()
        log.info("测试成教学员录入是否成功断言！")
        self.assertTrue(po2.type_register_cj_success, msg=None)
        log.info('成教学员录入信息成功！')

if __name__ == '__main__':
    unittest.main()