from BasePage import *
from selenium.webdriver.common.by import By
from Website.test_case.public.Log import *

class StudentInfoExamine(Action):
    '''新生信息修改申请'''
    iframe0 = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    smobile = (By.XPATH,'/html/body/div/div[1]/form/div/div[1]/div[2]/input')
    ssearch = (By.XPATH,'/html/body/div/div[1]/form/div/div[1]/div[4]/a[1]')
    allsele = (By.XPATH,'/html/body/div/div[2]/div/div/div/table/thead/tr/th[1]/input')
    examine = (By.XPATH,'/html/body/div/div[2]/div/span/a')
    btn = (By.XPATH,'/html/body/div[3]/div[3]/a[1]')
    assert_element =(By.XPATH,'//*[@id="phone"]')
    def type_student_examine(self,iphone):
        '''进入新生信息修改审核页面'''
        log=Log()
        log.info('新生信息修改审核页面！')
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.iframe0))
        sleep(1)
        self.find_element(*self.smobile).click()
        self.find_element(*self.smobile).send_keys(iphone)
        sleep(1)
        self.find_element(*self.ssearch).click()
        sleep(5)
        self.find_element(*self.allsele).click()
        sleep(1)
        self.find_element(*self.examine).click()
        sleep(2)
        self.find_element(*self.btn).click()
        sleep(2)
        log.info("新生信息审核完毕")

    def type_student_examine_success(self):
        '''新生信息修改审核断言'''
        return self.isElementExist(*self.assert_element)

