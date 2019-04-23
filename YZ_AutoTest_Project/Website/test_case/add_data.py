from LoginPage import *
from AdultRegisterPage import *
from HomePage import *
from myunit import *
from Log import *
class AddDataTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_addcj_testdata_1(self):
        '''测试数据录入'''
        Log().info("test_test_add_testdata is start test..")
        Log().info("输入账号密码！")
        LoginPage(self.driver).Login_action('蓝明勇', 'Yz123456')
        Log().info("开始测试录入成教学员信息！")
        ListPage(self.driver).type_studentmanage(1)
        Log().info("批量数据录入开始！。。。。。")
        for i in range(0, 30):
            Log().info("开始录入第%s个数据。" %i)
            Auto_CJ_Register(self.driver).type_cheng_register()
            Log().info("断言！")
            self.assertTrue(Auto_CJ_Register(self.driver).type_register_cj_success, msg=None)

if __name__ == '__main__':
    unittest.main()