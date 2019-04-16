from BasePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *
from Log import *

class Pay(Action):
    '''学员缴费管理页面'''
    inpay = (By.XPATH,'/html/body/div/div[2]/div/div/div/table/tbody/tr[1]/td[8]/a[1]')
    allsele = (By.XPATH,'/html/body/article/form/div[2]/div[2]/div/div/div[1]/div[1]/label')
    paytype = (By.XPATH,'/html/body/article/form/div[2]/div[10]/div/span/span[1]/span/span[2]')
    select1 = (By.XPATH,'/html/body/span/span/span[1]/input')
    mmoney = (By.CSS_SELECTOR,'#select2-paymentType-result-393c-1')
    savebtu = (By.CSS_SELECTOR,'.btn')
    Student_iframe = (By.XPATH, '//*[@id="iframe_box"]/div[1]/iframe')
    pay_iframe = (By.XPATH, '/html/body/div[3]/div[2]/iframe')
    def type_pay(self):
        log=Log()
        log.info('开始缴费！')
        sleep(3)
        self.find_element(*self.inpay).click()
        sleep(2)
        self.switch_to_frame(self.find_element(*self.pay_iframe))
        sleep(3)
        self.find_element(*self.allsele).click()
        sleep(2)
        self.find_element(*self.paytype).click()
        sleep(1)
        self.find_element(*self.select1).send_keys("现金")
        sleep(1)
        self.find_element(*self.select1).send_keys(Keys.ENTER)
        sleep(5)
        js = "var q=document.documentElement.scrollTop=10000"
        self.get_execute_script(js)
        self.find_element(*self.savebtu) .click()
        sleep(10)

