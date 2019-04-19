from LoginPage import *
from AdultRegisterPage import *
from SearchPage import *
from HomePage import *
from PayPage import *
from PayCheckPage import *
from StudentModifyPage import *
from StudentChangePage import *
from StudentOutPage import *
from myunit import *
from Log import *
class StudentOutTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_studentout_1(self):
        '''测试退学申请'''
        log=Log()
        log.info("test_test_add_testdata is start test..")
        po1 =LoginPage(self.driver)
        log.info("输入账号密码！")
        po1.Login_action('蓝明勇', 'Yz123456')
        log.info("开始测试退学申请！")
        po2 = Auto_CJ_Register(self.driver)
        po3 = ListPage(self.driver)
        po3.type_studentmanage(1)
        iphone = po2.type_cheng_register()
        po3.type_paymanage(1)
        po5 = Search(self.driver)
        po5.pay_search(iphone,1)
        po4 = Pay(self.driver)
        po4.type_pay()
        po3.type_paymanage(2)
        po5.pay_check_search(iphone)
        po6 = PayCheck(self.driver)
        po6.type_pay_check()
        po3.type_std_change(5)
        po7 = StudentOut(self.driver)
        s = Search(self.driver)
        s.type_stdout_search(iphone)
        po7.type_student_out()
        self.assertTrue(po7.type_student_out_success,msg=None)


if __name__ == '__main__':
    unittest.main()