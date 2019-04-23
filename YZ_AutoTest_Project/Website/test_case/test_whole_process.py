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
        Log().info("开始执行成教学员全流程测试！！！！")
        Log().info("输入账号密码！")
        LoginPage(self.driver).Login_action('蓝明勇', 'Yz123456')
        Log().info("开始测试成教全流程！")
        ListPage(self.driver).type_studentmanage(1)
        Log().info("开始录入成教学员信息！")
        iphone = Auto_CJ_Register(self.driver).type_cheng_register()
        # self.assertTrue(po2.type_register_cj_success, msg=None)
        Log().info("录入成教学员信息结束！")
        Log().info("开始缴纳成教学员辅导费！")
        ListPage(self.driver).type_paymanage(1)
        Search(self.driver).pay_search(iphone,1)
        Pay(self.driver).type_pay()
        Log().info("缴纳成教学员辅导费结束！")
        Log().info("开始成教学员辅导费审核！")
        ListPage(self.driver).type_paymanage(2)
        Search(self.driver).pay_check_search(iphone)
        PayCheck(self.driver).type_pay_check()
        Log().info("成教学员辅导费审核结束！")
        Log().info("开始成教学员考前资料核查！")
        ListPage(self.driver).type_studentmanage(2)
        Search(self.driver).exam_search(iphone)
        AdultCheck(self.driver).type_audit_data()
        Log().info("成教学员考前资料核查结束！")
        Log().info("开始成教学员考前确认！")
        ListPage(self.driver).type_studentmanage(3)
        Search(self.driver).exam_befor_search(iphone)
        AduitConfirm(self.driver).type_aduilt_confirm()
        Log().info("成教学员考前确认结束！")
        Log().info("开始成教学员考试成绩录入！")
        ListPage(self.driver).type_entmanage(1)
        Search(self.driver).type_enter_score(iphone)
        AdultEntrance(self.driver).type_entrance_score()
        Log().info("成教学员考试成绩录入结束！")
        Log().info("开始成教学员录取！")
        ListPage(self.driver).type_entmanage(2)
        Search(self.driver).type_student_recruit(iphone)
        AdultEntrance(self.driver).type_student_recruit()
        Log().info("成教学员录取结束！")
        Log().info("开始成教学员学费缴纳！")
        ListPage(self.driver).type_paymanage(1)
        Search(self.driver).pay_search(iphone,3)
        Pay(self.driver).type_pay()
        Log().info("成教学员学费缴纳结束！")
        self.assertTrue(Pay(self.driver).type_pay_success,msg=None)





if __name__ == '__main__':
    unittest.main()






