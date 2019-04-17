from BasePage import *
from selenium.webdriver.common.by import By
from Log import *
class StudentOutExamine(Action):
    '''学员退学审核页面'''
    Editer = (By.XPATH,'/html/body/div/div[3]/div/div/div/div/div/table/tbody/tr/td[16]/a/i')
    outiframe = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    Y0 = (By.XPATH,'/html/body/article/form/div[9]/div/table/tbody/tr/td[7]/input[2]')
    submit = (By.XPATH,'/html/body/article/form/div[11]/input[1]')

    examinepage = (By.XPATH,'/html/body/div/div[1]/span[2]')
    uiframe = (By.XPATH, '/html/body/section/div[2]/div[1]/iframe')
    editer1 = (By.XPATH,'/html/body/div/div[4]/div/div/div/div/div/table/tbody/tr/td[16]/a/i')
    outiframe1 = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    accessbtn = (By.XPATH,'/html/body/article/form/div[11]/input[1]')

    assert_element = (By.XPATH,'//*[@id="stdName"]')

    def type_student_out_examine(self):
        '''进入学员退学审核页面'''
        log=Log()
        log.info('开始退学审核！')
        sleep(1)
        self.find_element(*self.Editer).click()
        sleep(1)
        self.switch_to_frame(self.find_element(*self.outiframe))
        sleep(1)
        self.find_element(*self.Y0).clear()
        self.find_element(*self.Y0).send_keys('100')
        sleep(1)
        self.find_element(*self.submit).click()
        sleep(2)
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.uiframe))
        sleep(1)
        self.find_element(*self.examinepage).click()
        sleep(1)
        self.find_element(*self.editer1).click()
        sleep(1)
        self.switch_to_frame(self.find_element(*self.outiframe1))
        sleep(1)
        self.find_element(*self.accessbtn).click()
        sleep(3)
        log.info('退学审核结束！')

    def type_student_out_examine_success(self):
        '''退学审批成功断言'''
        self.isElementExist(*self.assert_element)
