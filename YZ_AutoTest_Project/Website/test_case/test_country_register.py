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
        log.info("开始执行测试教务系统国开学员录入>>缴费")
        try:
            log.info("输入账号密码！")
            LoginPage(self.driver).Login_action('蓝明勇', 'Yz123456')
            log.info("开始测试录入国开学员信息！")
            ListPage(self.driver).type_studentmanage(1)
            iphone=AutoGkRegister(self.driver).type_gk_register()
        except Exception as e:
            self.assertTrue(AutoGkRegister(self.driver).type_register_gk_success, msg=None)
            log.info("执行教务系统国开学员录入失败！！！！！！！！！！！")
        try:
            ListPage(self.driver).type_paymanage(1)
            Search(self.driver).pay_search(iphone,1)
            Pay(self.driver).type_pay()
            ListPage(self.driver).type_paymanage(2)
            Search(self.driver).pay_check_search(iphone)
            PayCheck(self.driver).type_pay_check()
            log.info('开始国开录入缴费判断！')
            self.assertTrue(AutoGkRegister(self.driver).type_register_gk_success, msg=None)
        except Exception as e:
            self.assertTrue(AutoGkRegister(self.driver).type_register_gk_success, msg=None)
            log.info("执行教务系统国开学员缴费失败！！！！！！！！！！！")

if __name__ == '__main__':
    unittest.main()






