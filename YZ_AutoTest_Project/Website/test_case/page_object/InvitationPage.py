from BasePage import *
from selenium.webdriver.common.by import By

class Invitation(Action):
    '''邀约注册'''
    register2 = (By.XPATH,'/html/body/div/div/div/div[3]/a')
    Register1 = (By.CSS_SELECTOR,'body > div > div > div > a')
    Rname = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(3) > input[type="text"]')
    Rmobile = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(4) > input[type="text"]')
    Rcode = (By.CSS_SELECTOR,'body > div > div > div > div.login-item.group > div > input[type="text"]')
    RegBtn = (By.CSS_SELECTOR,'body > div > div > div > div.login-item.item-btn > button')

    '''邀约报读'''
    Register = (By.CSS_SELECTOR,'body > div > div > div > div.fixBtn > a')
    ID = (By.CSS_SELECTOR,'body > div.wraper > div > div.form-enroll.mt > div:nth-child(2) > input')
    Gradation = (By.CSS_SELECTOR,'body > div.wraper > div > div.widget-list.mt > div:nth-child(3) > i')
    Highschool = (By.CSS_SELECTOR,'body > div.wraper > div > div.children-page > div > div > div > div:nth-child(1)')
    City = (By.CSS_SELECTOR,'body > div.wraper > div > div.widget-list.mt > div:nth-child(4) > i')
    CityName = (By.CSS_SELECTOR,'body > div.wraper > div > div.children-page > div > div > div > div:nth-child(1)')
    Academy = (By.CSS_SELECTOR,'body > div.wraper > div > div.widget-list.mt > div:nth-child(5) > i')
    AcademyName = (By.CSS_SELECTOR,'body > div.wraper > div > div.children-page > div > div > div > div:nth-child(10)')
    Major = (By.CSS_SELECTOR,'body > div.wraper > div > div.widget-list.mt > div:nth-child(6) > i')
    MajorName = (By.CSS_SELECTOR,'body > div.wraper > div > div.children-page > div > div > div > div:nth-child(5)')
    Address = (By.CSS_SELECTOR,'body > div.wraper > div > div.widget-list.mt > a > i')
    AddressName = (By.CSS_SELECTOR,'body > div.wraper > div > div.children-page > div > div > div > div:nth-child(1)')
    NextBtn = (By.CSS_SELECTOR,'body > div.wraper > div > div.footer.active > div > div')
    SaveBtn = (By.CSS_SELECTOR,'body > div.wraper > div > div.children-page > div.footer.active > div > div')

    '''断言'''
    Access = (By.CSS_SELECTOR,'body > div.wraper > div > div.children-page > div.commonPop.success > div > div > div.sjlb.mt > div > div.yj > img')
    def type_invitationregister(self):
        self.find_element(*self.register2).cilck()
        self.find_element(*self.Register1).cilck()
        sleep(1)
        self.find_element(*self.Rname).cilck()
        sleep(1)
        self.find_element(*self.Rmobile).cilck()
        sleep(1)
        self.find_element(*self.Rcode).cilck()
        sleep(1)
        self.find_element(*self.RegBtn).cilck()
        sleep(6)
        return


    def type_invitationadult(self):
        self.find_element(*self.Register).click()
        self.find_element(*self.Gradation).click()
        self.find_element(*self.Highschool).click()
        self.find_element(*self.City).click()
        self.find_element(*self.CityName).click()
        self.find_element(*self.Academy).click()
        self.find_element(*self.AcademyName).click()
        self.find_element(*self.Major).click()
        self.find_element(*self.MajorName).click()
        self.find_element(*self.Address).click()
        self.find_element(*self.AddressName).click()
        self.find_element(*self.NextBtn).click()
        self.find_element(*self.SaveBtn).click()

    def type_dd_assert_success(self):
        '''钉钉录入信息断言'''
        return self.isElementExist(*self.Access)