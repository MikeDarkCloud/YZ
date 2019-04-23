from BasePage import *
from selenium.webdriver.common.by import By
from Log import *


class AdultCheck(Action):
    '''考前资料核查页面'''
    Editer = (By.CSS_SELECTOR,'#DataTables_Table_0 > tbody > tr:nth-child(1) > td:nth-child(10) > a > i')
    AdoptOne = (By.XPATH,'/html/body/div/div[5]/div[1]/div/div/table/tbody/tr[1]/td[8]/a[1]')
    AdoptTwo = (By.XPATH,'/html/body/div/div[5]/div[1]/div/div/table/tbody/tr[2]/td[8]/a[1]')
    AdoptThree = (By.XPATH,'/html/body/div/div[5]/div[1]/div/div/table/tbody/tr[3]/td[8]/a[1]')
    ToExamine = (By.CSS_SELECTOR,'#tab_demo > div.tabBar.clearfix > span:nth-child(5)')
    AdoptFour = (By.XPATH,'/html/body/div/div[6]/div/div/table/tbody/tr/td[5]/a[1]')
    iframe1 = (By.XPATH, '/html/body/div[3]/div[2]/iframe')
    '''断言元素'''
    Text = (By.XPATH,'//*[@id="checkBody"]/tr/td[2]')

    def type_audit_data(self):
        '''考前资料核查通过'''
        Log().info("======开始考前资料核查======")
        sleep(2)
        self.find_element(*self.Editer).click()
        sleep(2)
        self.switch_to_frame(self.find_element(*self.iframe1))
        self.implicity_wait(5)
        Log().info("======审核附件======")
        self.find_element(*self.AdoptOne).click()
        sleep(2)
        self.find_element(*self.AdoptTwo).click()
        sleep(2)
        self.find_element(*self.AdoptThree).click()
        sleep(2)
        self.find_element(*self.ToExamine).click()
        sleep(2)
        self.find_element(*self.AdoptFour).click()
        Log().info("======审核完毕======")
    def type_audit_pass(self):
        '''审核通过断言'''
        passText = self.find_element(*self.Text).text()
        try:
            assert passText == u'审核通过'
            Log().info('audit_data_Testcase pass')
        except Exception as e:
            Log().info('audit_data_Testcase Fail')



