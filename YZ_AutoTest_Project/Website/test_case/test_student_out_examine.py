from LoginPage import *
from AdultRegisterPage import *
from SearchPage import *
from HomePage import *
from PayPage import *
from PayCheckPage import *
from StudentModifyPage import *
from StudentChangePage import *
from StudentOutPage import *
from StudentOutExaminePage import *
from myunit import *
from Log import *
class StudentOutExamineTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_student_out_examine_1(self):
        '''测试退学申请'''
        Log().info("test_test_add_testdata is start test..")
        Log().info("输入账号密码！")
        LoginPage(self.driver).Login_action('蓝明勇', 'Yz123456')
        Log().info("开始测试退学申请！")
        ListPage(self.driver).type_studentmanage(1)
        iphone = Auto_CJ_Register(self.driver).type_cheng_register()
        ListPage(self.driver).type_paymanage(1)
        Search(self.driver).pay_search(iphone,1)
        Pay(self.driver).type_pay()
        ListPage(self.driver).type_paymanage(2)
        Search(self.driver).pay_check_search(iphone)
        PayCheck(self.driver).type_pay_check()
        ListPage(self.driver).type_std_change(5)
        Search(self.driver).type_stdout_search(iphone)
        StudentOut(self.driver).type_student_out()
        ListPage(self.driver).type_std_change(6)
        Search(self.driver).type_stdout_examine(iphone)
        StudentOutExamine(self.driver).type_student_out_examine()
        self.assertTrue(StudentOutExamine(self.driver).type_student_out_examine_success,msg=None)




if __name__ == '__main__':
    unittest.main()