from BasePage import *
from selenium.webdriver.common.by import By
from Log import *
class StudentOut(Action):
    '''学员退学申请页面'''
    outiframe = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    outreason = (By.XPATH,'/html/body/article/form/div[3]/div[1]/div/span/span[1]/span/span[1]')
    reason = (By.XPATH,'/html/body/span/span/span[2]/ul/li[2]')
    remarks = (By.XPATH,'/html/body/article/form/div[3]/div[3]/div/textarea')
    submit = (By.XPATH,'/html/body/article/form/div[4]/input')
    def type_student_out(self):
        '''进入学员退学申请页面'''
        log=Log()
        log.info('开始退学申请！')
        self.switch_to_frame(self.find_element(*self.outiframe))
        sleep(1)
        self.find_element(*self.outreason).click()
        sleep(1)
        self.find_element(*self.reason).click()
        sleep(1)
        self.find_element(*self.remarks).click()
        sleep(1)
        self.find_element(*self.remarks).send_keys("test student out !")
        sleep(1)
        self.find_element(*self.submit).click()
        sleep(4)
        log.info('退学申请结束！')



