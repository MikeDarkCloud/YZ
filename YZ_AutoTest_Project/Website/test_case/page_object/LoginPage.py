from BasePage import *
from selenium.webdriver.common.by import By
from time import sleep
class LoginPage(Action):
    #定位器
    username_loc=(By.ID,'username')
    password_loc=(By.ID,'password')
    vcode=(By.CSS_SELECTOR,'#validCode')
    submit=(By.CSS_SELECTOR,'.btn')
    img_code = (By.CSS_SELECTOR,'#validCodeImg')
    Recruit_students_loc = (By.XPATH, '/html/body/aside/div/dl[2]/dt')

    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        # self.def_send_keys(*self.username_loc,password)
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)


    # def type_vcode(self):
    #     sleep(2)
    #     p1 = os.path.dirname(os.path.abspath('.'))
    #     p2 = "public\image\img0.png"
    #     file = os.path.join(p1, p2)
    #     ele = self.find_element(*self.img_code)
    #     ele.screenshot(file)
    #     sleep(2)
    #     img1 = BaiduApi()
    #     icode=img1.get_code()
    #     sleep(2)
    #     self.find_element(*self.vcode_loc).clear()
    #     self.find_element(*self.vcode_loc).send_keys(icode)
    #     sleep(5)

    def type_submit(self):
        self.find_element(*self.submit).click()
        # l = self.isElementExist(*self.Recruit_students_loc)
        # if l:
        #     pass
        # else:
        #     self.type_vcode()
        #     self.find_element(*self.submit_loc).click()
        #     if l:
        #         pass
        #     else:
        #         self.type_vcode()
        #         self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password):
        self.open()
        sleep(5)
        self.type_username(username)
        self.type_password(password)
        sleep(2)
        # self.type_vcode()
        sleep(15)
        self.type_submit()


    loginPass_loc=(By.CSS_SELECTOR,'#menu-admin > dt > span')
    loginFail_loc=(By.CSS_SELECTOR,'.btn')

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc)

    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc)



if __name__ == '__main__':
    LoginPage.Login_action('蓝明勇','Yz123456')
