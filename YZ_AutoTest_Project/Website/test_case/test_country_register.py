from CountryRegisterPage import *
from LoginPage import *
from PayPage import *
from SearchPage import *
from PayCheckPage import *
from HomePage import *
from AdultEntrance import *
from myunit import *

class CountryRegisterTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_country_register(self):
        '''测试教务系统国开学员录入缴费'''
        log = Log()
        po1=LoginPage(self.driver)
        log.info("输入账号密码！")
        po1.Login_action('autotester1', 'Yz123456')
        log.info("开始测试录入国开学员信息！")
        po2 = AutoGkRegister(self.driver)
        po3 = ListPage(self.driver)
        po3.type_studentmanage(1)
        iphone = po2.type_gk_register()
        self.assertTrue(po2.type_register_gk_success, msg=None)
        po3.type_paymanage(1)
        po5 = Search(self.driver)
        po5.pay_search(iphone, 1)
        po4 = Pay(self.driver)
        po4.type_pay()
        po3.type_paymanage(2)
        po5.pay_check_search(iphone)
        po6 = PayCheck(self.driver)
        po6.type_pay_check()
        self.assertTrue(po2.type_register_gk_success, msg=None)
        #循环时使用
        # for i in range(0, 10):
        #     po2.type_cheng_register()
        #     log.info("断言！")
        #     self.assertIsNotNone(po2.type_register_gk_success, msg=None)



if __name__ == '__main__':
    unittest.main()






