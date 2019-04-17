from LoginPage import *
from AdultRegisterPage import *
from HomePage import *
from PayPage import *
from PayCheckPage import *
from SearchPage import *
from AdultCheckFilePage import *
from AdultConfirmPage import *
from AdultEntrance import *
from time import sleep
from  myunit import *


class WholeProcessTest(StartEnd):
    # @unittest.skip('skip this case')
    def tests_whole_process(self):
        '''测试成教学员录入,缴辅导费，考前资料核查，考前确认，录入成绩，录取，缴学费'''
        log = Log()
        log.info("test_whole_process is start test..")
        po1=LoginPage(self.driver)
        log.info("输入账号密码！")
        po1.Login_action('autotester1', 'Yz123456')
        log.info("开始测试成教全流程！")
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
        po3.type_studentmanage(2)
        po7=AdultCheck(self.driver)
        po5.exam_search(iphone)
        po7.type_audit_data()
        po3.type_studentmanage(3)
        po5.exam_befor_search(iphone)
        po8 = AduitConfirm(self.driver)
        po8.type_aduilt_confirm()
        po3.type_entmanage(1)
        po9= AdultEntrance(self.driver)
        po5.type_enter_score(iphone)
        po9.type_entrance_score()
        po3.type_entmanage(2)
        po5.type_student_recruit(iphone)
        po9.type_student_recruit()
        sleep(6)
        po3.type_paymanage(1)
        po5.pay_search(iphone,3)
        po4.type_pay()
        self.assertTrue(po4.type_pay_success,msg=None)





if __name__ == '__main__':
    unittest.main()






