from Website.test_case.page_object.LoginPage import *
from time import sleep
from myunit import *

class LoginTest(StartEnd):
    #@unittest.skip('skip this case')
    def test_register1_normal(self):
        '''登陆测试'''
        print("test_register_normal is start test..")
        po1=LoginPage(self.driver)
        po1.open()
        po1.type_username("蓝明勇")
        po1.type_password('Yz123456')
        sleep(15)
        po1.type_submit()
        sleep(5)
        po1.type_loginPass_hint()


if __name__ == '__main__':
    unittest.main()






