from BasePage import *
from Log import *
from selenium.webdriver.common.by import By
class CouponTest(Action):
    '''Domain'''
    id_card = (By.XPATH,'/html/body/div/div[1]/div/div[2]/div[1]/input')
    search = (By.XPATH,'/html/body/div/div[1]/div/div[1]/div[4]/a[1]')
    is_use = (By.XPATH,'/html/body/div/div[1]/div/div[1]/div[1]/span[2]/span[1]/span/span[1]')
    no_use = (By.XPATH,'/html/body/span/span/span[2]/ul/li[3]')
    coupon = (By.XPATH,'/html/body/div/div[1]/div/div[1]/div[2]/input')
    iframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    editer = (By.XPATH,'/html/body/div/div[2]/div/div/table/tbody/tr/td[13]/a[1]/i')
    iframe2 = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    submit = (By.XPATH,'/html/body/article/form/div[6]/div/input')

    def type_coupon_test_1(self,num):
        '''废弃优惠券'''
        id_card = [431121200012020047,440221198903244729]
        log=Log()
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.iframe))
        sleep(3)
        log.info("开始废弃优惠券！")
        self.find_element(*self.id_card).clear()
        sleep(1)
        log.info("输入用户身份证：%s" %id_card[num])
        self.find_element(*self.id_card).clear()
        self.find_element(*self.id_card).send_keys(id_card[num])
        sleep(1)
        self.find_element(*self.is_use).click()
        sleep(1)
        self.find_element(*self.no_use).click()
        sleep(1)
        self.find_element(*self.coupon).click()
        sleep(1)
        self.find_element(*self.coupon).clear()
        self.find_element(*self.coupon).send_keys("2019/2020转报Y1优惠")
        sleep(1)
        self.find_element(*self.search).click()
        sleep(5)
        self.find_element(*self.editer).click()
        sleep(5)
        self.switch_to_frame(self.find_element(*self.iframe2))
        sleep(5)
        self.find_element(*self.submit).click()
        sleep(2)
        log.info("废弃完毕！")
