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
        Log().info("开始执行测试成教学员新生信息异动！！")
        Log().info("输入账号密码！")
        LoginPage(self.driver).Login_action('蓝明勇', 'Yz123456')
        Log().info("测试新生信息异动申请！")
        ListPage(self.driver).type_studentmanage(1)
        iphone = Auto_CJ_Register(self.driver).type_cheng_register()
        # self.assertTrue(po2.type_register_cj_success, msg=None)
        ListPage(self.driver).type_paymanage(1)
        Search(self.driver).pay_search(iphone,1)
        Pay(self.driver).type_pay()
        ListPage(self.driver).type_paymanage(2)
        Search(self.driver).pay_check_search(iphone)
        PayCheck(self.driver).type_pay_check()
        ListPage(self.driver).type_std_change(1)
        # self.assertTrue(po7.type_student_modify_success,msg = None)
        StudentInfoModify(self.driver).type_student_change(iphone)
        ListPage(self.driver).type_std_change(2)
        StudentInfoExamine(self.driver).type_student_examine(iphone)
        self.assertTrue(StudentInfoExamine(self.driver).type_student_examine_success,msg=None)



if __name__ == '__main__':
    unittest.main()