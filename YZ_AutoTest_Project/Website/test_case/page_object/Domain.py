from BasePage import *
from Log import *
from selenium.webdriver.common.by import By


class DomianTest(Action):
    '''Domain'''
    iframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    selectt  = (By.XPATH,'/html/body/div/div[1]/div/div/div[1]/span[2]/span[1]/span/span[1]')
    std = (By.XPATH,'/html/body/span/span/span[2]/ul/li[2]')
    user = (By.XPATH,'/html/body/div/div[1]/div/div/div[2]/input')
    search = (By.XPATH,'/html/body/div/div[1]/div/div/div[8]/a[1]')
    clear1 = (By.XPATH,'/html/body/div/div[3]/div/a')

    def type_domain_manage(self,num):
        '''Domian'''
        user_id = [39183,108458,154235898535486400,155240118007681345,153131479426085850,153551345108155370,457743676853230500]
        log=Log()
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.iframe))
        sleep(3)
        log.info("开始清除域数据！")
        self.find_element(*self.selectt).click()
        sleep(1)
        self.find_element(*self.std).click()
        sleep(1)
        self.find_element(*self.user).clear()
        sleep(1)
        log.info("开始清除：%s" %user_id[num])
        self.find_element(*self.user).send_keys(user_id[num])
        sleep(1)
        self.find_element(*self.search).click()
        sleep(1)
        self.find_element(*self.clear1).click()
        log.info("清除完毕！")
