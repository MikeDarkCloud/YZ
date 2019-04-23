from LoginPage import *
from AdultRegisterPage import *
from SearchPage import *
from HomePage import *
from PayPage import *
from PayCheckPage import *
from StudentModifyPage import *
from StudentChangePage import *
from StudentInfoExamine import *
from myunit import *
from Log import *
class StudentRollTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_student_roll_1(self):
        '''测试新生信息异动申请'''
        Log().info("test_student_roll is start test..")
        Log().info("输入账号密码！")
        LoginPage(self.driver).Login_action('蓝明勇', 'Yz123456')
        Log().info("测试新生信息异动申请！")
        ListPage(self.driver).type_studentmanage(1)
        iphone = Auto_CJ_Register(self.driver).type_cheng_register()
        ListPage(self.driver).type_paymanage(1)
        Search(self.driver).pay_search(iphone,1)
        Pay(self.driver).type_pay()
        ListPage(self.driver).type_paymanage(2)
        Search(self.driver).pay_check_search(iphone)
        PayCheck(self.driver).type_pay_check()
        ListPage(self.driver).type_std_change(7)
        Search(self.driver).type_zbnew_search(iphone)
        StudentChange(self.driver).type_student_change()
        Log().info("转报断言！")
        self.assertTrue(StudentChange(self.driver).type_assert_student_roll(), msg=None)
        Log().info("转报测试完成")




if __name__ == '__main__':
    unittest.main()