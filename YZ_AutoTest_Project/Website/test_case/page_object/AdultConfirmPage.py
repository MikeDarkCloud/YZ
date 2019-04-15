from BasePage import *
from selenium.webdriver.common.by import By
from Log import *

class AduitConfirm(Action):
    '''考前确认页面'''
    into = (By.XPATH,'/html/body/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]/td[9]/a')
    Confirm = (By.XPATH,'/html/body/div[3]/div[3]/a[1]')

    def type_aduilt_confirm(self):
        '''进入确认'''
        log=Log()
        log.info('成考确认！')
        sleep(2)
        self.find_element(*self.into).click()
        sleep(1)
        self.find_element(*self.Confirm).click()





