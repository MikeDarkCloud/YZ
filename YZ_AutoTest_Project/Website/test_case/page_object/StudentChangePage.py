from BasePage import *
from selenium.webdriver.common.by import By
from Log import *
from selenium.webdriver.common.keys import Keys
from Website.test_case.page_object.SearchPage import *

class StudentChange(Action):
    '''学员转报页面'''
    chifream0 = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    stdadd = (By.XPATH,'/html/body/div/div[2]/div/div/table/tbody/tr/td[5]/a/i')
    chifream = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    pfsnlevel = (By.XPATH,'/html/body/article/form/div[3]/div[2]/div/span/span[1]/span/span[1]')
    pfsnlevel1 = (By.XPATH,'/html/body/span/span/span[2]/ul/li[1]')
    grade = (By.XPATH,'/html/body/article/form/div[3]/div[3]/div/span/span[1]/span/span[1]')
    grade1 = (By.XPATH,'/html/body/span/span/span[2]/ul/li[2]')
    unvsid = (By.XPATH,'/html/body/article/form/div[3]/div[4]/div/span[1]/span[1]/span/span[1]')
    unvsidinput = (By.XPATH,'/html/body/span/span/span[1]/input')
    unvsid1 = (By.XPATH,'/html/body/article/form/div[3]/div[4]/div/span[2]/span[1]/span/span[1]')
    unvsid1input = (By.XPATH,'/html/body/article/form/div[3]/div[4]/div/span[2]/span[1]/span/span[1]')
    unvsid2 = (By.XPATH,'/html/body/article/form/div[3]/div[4]/div/span[3]/span[1]/span/span[1]')
    unvsid2input = (By.XPATH,'/html/body/span/span/span[1]/input')
    submit = (By.XPATH,'/html/body/article/form/div[4]/input')
    assert_element=(By.XPATH,'//*[@id="mobile"]')

    def type_student_change(self):
        '''开始学员转报'''
        log=Log()
        log.info('开始学员转报！')
        self.find_element(*self.stdadd).click()
        sleep(4)
        self.switch_to_frame(self.find_element(*self.chifream))
        sleep(1)
        self.find_element(*self.pfsnlevel).click()
        self.find_element(*self.pfsnlevel1).click()
        sleep(1)
        self.find_element(*self.grade).click()
        sleep(1)
        self.find_element(*self.grade1).click()
        sleep(1)
        self.find_element(*self.unvsid).click()
        sleep(1)
        self.find_element(*self.unvsidinput).send_keys("51161")
        sleep(1)
        self.find_element(*self.unvsidinput).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.unvsid1input).click()
        self.find_element(*self.unvsid1input).send_keys("高中起点高职高专")
        self.find_element(*self.unvsid1input).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.unvsid2).click()
        sleep(1)
        self.find_element(*self.unvsid2input).send_keys("广州天河")
        self.find_element(*self.unvsid2input).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.submit).click()
        sleep(4)

    def type_assert_student_roll(self):
        '''转报断言”'''
        return self.isElementExist(*self.assert_element)



