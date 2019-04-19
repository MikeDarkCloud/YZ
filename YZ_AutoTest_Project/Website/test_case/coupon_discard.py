from LoginPage import *
from HomePage import *
from CouponPage import *
from myunit import *
from Log import *
class CouponTestPage(StartEnd):
    # @unittest.skip('skip this case')
    def test_coupon(self):
        '''废弃指定学员优惠券'''
        log=Log()
        log.info("废弃指定学员优惠券开始！")
        po1 =LoginPage(self.driver)
        log = Log()
        log.info("输入账号密码！")
        po1.Login_action('蓝明勇', 'Yz123456')
        po2=ListPage(self.driver)
        po2.type_paymanage(3)
        po3=CouponTest(self.driver)
        # po3.type_coupon_test(0)
        for i in range(0,260):
            try:
                log.info(i)
                po3.type_coupon_test_1(i)
            except Exception as e:
                log.info("第%s错了！" %i)



if __name__ == '__main__':
    unittest.main()