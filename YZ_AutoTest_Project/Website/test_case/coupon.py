from LoginPage import *
from AdultRegisterPage import *
from HomePage import *
from Domain import *
from AdultEntrance import *
from myunit import *
from Log import *
class CouponTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_coupon_1(self):
        '''清除域数据'''
        log=Log()
        log.info("test_test_add_testdata is start test..")
        po1 =LoginPage(self.driver)
        log = Log()
        log.info("输入账号密码！")
        po1.Login_action('autotester1', 'Yz123456')
        po2=ListPage(self.driver)
        po2.type_domain()
        po3=DomianTest(self.driver)
        for i in range(0,6):
            po3.type_domain_manage(i)




if __name__ == '__main__':
    unittest.main()