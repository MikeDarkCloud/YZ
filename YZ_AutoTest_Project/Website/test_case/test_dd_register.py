from DingRegisterPage import *
from AdultRegisterPage import *
from AdultEntrance import *
from myunit import *

class DingDingRegisterTest(StartEnd):
    '''钉钉招生应用'''
    # @unittest.skip('skip this case')
    def test_dingding_register_1(self):
        '''测试钉钉招生应用成教学员录入'''
        log=Log()
        log.info("test_register_normal is start test..")
        log.info("开始测试钉钉录入成教学员信息！")
        po2 = Auto_DCJ_register(self.driver)
        po2.open_new('http://zm-3.yzwill.cn/recruit/login')
        po2.type_dd_login()
        po2.type_ddcj_register()
        log.info("断言！")
        self.assertIsNotNone(po2.type_dregister_success,msg=None)
        log.info("恭喜！钉钉录入学员通过")

if __name__ == '__main__':
    unittest.main()






