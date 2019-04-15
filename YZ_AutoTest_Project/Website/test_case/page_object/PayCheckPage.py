from BasePage import *
from selenium.webdriver.common.by import By
from Log import *
class PayCheck(Action):
    '''学员缴费审核页面'''
    select2 = (By.XPATH,'//*[@id="tab"]/thead/tr/th[1]/input')
    check = (By.CSS_SELECTOR,'body > div > div > div > span.l.mt-5.mb-15 > a.btn.btn-primary.radius')
    ifrome  = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    enter = (By.XPATH,'/html/body/div[3]/div[3]/a[1]')
    def type_pay_check(self):
        log=Log()
        log.info('开始缴费审核！')
        self.find_element(*self.select2).click()
        sleep(2)
        self.find_element(*self.check).click()
        sleep(2)
        self.find_element(*self.enter).click()
        sleep(2)




