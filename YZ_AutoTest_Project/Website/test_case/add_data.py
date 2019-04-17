from LoginPage import *
from AdultRegisterPage import *
from HomePage import *
from myunit import *
from Log import *
class AddDataTest(StartEnd):
    # @unittest.skip('skip this case')
    def test_addcj_testdata_1(self):
        '''测试数据录入'''
        log=Log()
        log.info("test_test_add_testdata is start test..")
        po1 =LoginPage(self.driver)
        log = Log()
        log.info("输入账号密码！")
        po1.Login_action('蓝明勇', 'Yz123456')
        log.info("开始测试录入成教学员信息！")
        po2 = Auto_CJ_Register(self.driver)
        po3 = ListPage(self.driver)
        po3.type_studentmanage(1)
        log.info("批量数据录入开始！。。。。。")
        for i in range(0, 30):
            log.info("开始录入第%s个数据。" %i)
            po2.type_cheng_register()
            log.info("断言！")
            self.assertIsNotNone(po2.type_register_hint, msg=None)

if __name__ == '__main__':
    unittest.main()