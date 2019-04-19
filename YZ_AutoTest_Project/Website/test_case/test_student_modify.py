from LoginPage import *
from AdultRegisterPage import *
from SearchPage import *
from HomePage import *
from PayPage import *
from PayCheckPage import *
from StudentModifyPage import *
from StudentInfoExamine import *
from myunit import *
from Log import *
class StudentModifyTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_student_modify_1(self):
        '''测试新生信息异动申请'''
        log=Log()
        log.info("test_test_add_testdata is start test..")
        po1 =LoginPage(self.driver)
        log = Log()
        log.info("输入账号密码！")
        po1.Login_action('蓝明勇', 'Yz123456')
        log.info("测试新生信息异动申请！")
        po2 = Auto_CJ_Register(self.driver)
        po3 = ListPage(self.driver)
        po3.type_studentmanage(1)
        iphone = po2.type_cheng_register()
        # self.assertTrue(po2.type_register_cj_success, msg=None)
        po3.type_paymanage(1)
        po5 = Search(self.driver)
        po5.pay_search(iphone,1)
        po4 = Pay(self.driver)
        po4.type_pay()
        po3.type_paymanage(2)
        po5.pay_check_search(iphone)
        po6 = PayCheck(self.driver)
        po6.type_pay_check()
        po3.type_std_change(1)
        po7 = StudentInfoModify(self.driver)
        # self.assertTrue(po7.type_student_modify_success,msg = None)
        po7.type_student_change(iphone)
        po3.type_std_change(2)
        po8 = StudentInfoExamine(self.driver)
        po8.type_student_examine(iphone)
        self.assertTrue(po8.type_student_examine_success,msg=None)



if __name__ == '__main__':
    unittest.main()