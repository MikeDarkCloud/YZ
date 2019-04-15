from BasePage import *
from selenium.webdriver.common.by import By
from Log import *

class Pay(Action):
    '''学员缴费管理页面'''
    inpay = (By.XPATH,'/html/body/div/div[2]/div/div/div/table/tbody/tr[1]/td[8]/a[1]')
    allsele = (By.XPATH,'/html/body/article/form/div[2]/div[2]/div/div/div[1]/div[1]/label')
    paytype = (By.CSS_SELECTOR,'#form-std-pay > div.mb-15.bk-gray.radius > div:nth-child(11) > div > span > span.selection > span > span.select2-selection__arrow')
    mmoney = (By.XPATH,'//li[text()="--现金--"]')
    select1 = (By.CSS_SELECTOR,'body > span')
    savebtu = (By.XPATH,'/html/body/article/form/div[3]/input[1]')
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
        sleep(2)
        self.find_element(*self.select1).click()
        sleep(1)
        self.find_element(*self.mmoney).click()
        sleep(2)
        self.find_element(*self.savebtu) .click()
        sleep(3)

