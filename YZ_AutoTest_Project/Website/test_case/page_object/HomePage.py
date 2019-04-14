from BasePage import *
from Log import *
from selenium.webdriver.common.by import By


class ListPage(Action):
    '''招生管理'''
    Recruit_students_loc=(By.XPATH,'/html/body/aside/div/dl[2]/dt')
    My_Student_loc=(By.CSS_SELECTOR,'.menu_dropdown > dl:nth-child(2) > dd:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)')
    DataVerification=(By.XPATH,'/html/body/aside/div/dl[2]/dd/ul/li[4]/a')
    ExamConfirm=(By.CSS_SELECTOR,'#menu-admin > dd > ul > li:nth-child(5) > a')
    '''入学管理'''
    EntMange=(By.XPATH,'/html/body/aside/div/dl[6]/dt')
    EntScore=(By.XPATH,'/html/body/aside/div/dl[6]/dd/ul/li[1]/a')
    EnrollStudent=(By.XPATH,'/html/body/aside/div/dl[6]/dd/ul/li[2]/a')
    StudentSeg=(By.CSS_SELECTOR,'#menu-admin > dd > ul > li:nth-child(3) > a')
    '''财务管理'''
    PayManage = (By.XPATH,'/html/body/aside/div/dl[15]/dt/i[2]')
    stdPay = (By.XPATH,'/html/body/aside/div/dl[15]/dd/ul/li[6]/a')
    PayChack = (By.XPATH,'/html/body/aside/div/dl[11]/dd/ul/li[6]/a')
    coupon = (By.XPATH,'/html/body/aside/div/dl[15]/dd/ul/li[11]')
    '''学员异动管理'''
    stdchange = (By.XPATH,'/html/body/aside/div/dl[4]/dt/span')
    stdchgapply = (By.XPATH,'/html/body/aside/div/dl[4]/dd/ul/li[1]/a')
    stdchgch = (By.XPATH,'/html/body/aside/div/dl[4]/dd/ul/li[2]/a')
    lench = (By.XPATH,'/html/body/aside/div/dl[4]/dd/ul/li[7]/a')
    lenchch = (By.XPATH,'/html/body/aside/div/dl[4]/dd/ul/li[9]/a')
    stdout = (By.XPATH,'/html/body/aside/div/dl[4]/dd/ul/li[4]/a')
    stdoutch = (By.XPATH,'/html/body/aside/div/dl[4]/dd/ul/li[5]/a')
    learnch = (By.XPATH,'/html/body/aside/div/dl[4]/dd/ul/li[3]/a')
    '''Domain'''
    base = (By.XPATH,'/html/body/aside/div/dl[1]/dt')
    domain = (By.XPATH,'/html/body/aside/div/dl[25]/dt/i[2]')
    domain1 = (By.XPATH,'/html/body/aside/div/dl[25]/dd/ul/li/a')


    def type_std_change(self,num):
        '''学员异动管理'''
        log = Log()
        self.switch_to_content()
        if num ==1:
            l = self.isElementExist(*self.stdchgapply)
            if l:
                self.find_element(*self.stdchgapply).click()
            else:
                self.find_element(*self.stdchange).click()
                sleep(3)
                self.find_element(*self.stdchgapply).click()
            sleep(3)
            log.info('进入新生信息修改页面')
        elif num ==2:
            l = self.isElementExist(*self.stdchgch)
            if l:
                self.find_element(*self.stdchgch).click()
            else:
                self.find_element(*self.stdchange).click()
                sleep(3)
                self.find_element(*self.stdchgch).click()
            sleep(3)
            log.info('进入新生信息修改审核页面')
        elif num ==3:
            l = self.isElementExist(*self.lench)
            if l:
                self.find_element(*self.lench).click()
            else:
                self.find_element(*self.stdchange).click()
                sleep(3)
                self.find_element(*self.lench).click()
            sleep(3)
            log.info('进入学籍信息异动申请页面')
        elif num ==4:
            l = self.isElementExist(*self.lenchch)
            if l:
                self.find_element(*self.lenchch).click()
            else:
                self.find_element(*self.stdchange).click()
                sleep(3)
                self.find_element(*self.lenchch).click()
            sleep(3)
            log.info('进入学籍信息异动审核页面')

        elif num ==5:
            l = self.isElementExist(*self.stdout)
            if l:
                self.find_element(*self.stdout).click()
            else:
                self.find_element(*self.stdchange).click()
                sleep(3)
                self.find_element(*self.stdout).click()
            sleep(3)
            log.info('退学学员页面')

        elif num ==6:
            l = self.isElementExist(*self.stdoutch)
            if l:
                self.find_element(*self.stdoutch).click()
            else:
                self.find_element(*self.stdchange).click()
                sleep(3)
                self.find_element(*self.stdoutch).click()
            sleep(3)
            log.info('退学学员审核页面')
        elif num ==7:
            l = self.isElementExist(*self.learnch)
            if l:
                self.find_element(*self.learnch).click()
            else:
                self.find_element(*self.stdchange).click()
                sleep(3)
                self.find_element(*self.learnch).click()
            sleep(3)
            log.info('转报学员页面')

    def type_studentmanage(self,num):
        '''招生管理'''
        log = Log()
        self.switch_to_content()
        if num ==1:
            l = self.isElementExist(*self.My_Student_loc)
            if l:
                self.find_element(*self.My_Student_loc).click()
            else:
                self.find_element(*self.Recruit_students_loc).click()
                sleep(3)
                self.find_element(*self.My_Student_loc).click()
            sleep(3)
            log.info('进入我的学员页面')
        elif num ==2:
            l = self.isElementExist(*self.My_Student_loc)
            if l:
                self.find_element(*self.DataVerification).click()
            else:
                self.find_element(*self.Recruit_students_loc).click()
                sleep(3)
                self.find_element(*self.DataVerification).click()
            sleep(3)
            log.info('进入考前资料核查页面')
        elif num ==3:
            l = self.isElementExist(*self.My_Student_loc)
            if l:
                self.find_element(*self.ExamConfirm).click()
            else:
                self.find_element(*self.Recruit_students_loc).click()
                sleep(3)
                self.find_element(*self.ExamConfirm).click()
            sleep(3)
            log.info('进入考前确认页面')

    def type_entmanage(self,num):
        '''入学管理'''
        log = Log()
        self.switch_to_content()
        if num ==1:
            l = self.isElementExist(*self.EntScore)
            if l:
                self.find_element(*self.EntScore).click()
            else:
                self.find_element(*self.EntMange).click()
                sleep(3)
                self.find_element(*self.EntScore).click()
            sleep(3)
            log.info('进入入学成绩页面')
        elif num ==2:
            l = self.isElementExist(*self.EnrollStudent)
            if l:
                self.find_element(*self.EnrollStudent).click()
            else:
                self.find_element(*self.EntMange).click()
                sleep(3)
                self.find_element(*self.EnrollStudent).click()
            sleep(3)
            log.info('进入学员录取页面')
        elif num ==3:
            l = self.isElementExist(*self.My_Student_loc)
            if l:
                self.find_element(*self.StudentSeg).click()
            else:
                self.find_element(*self.EntMange).click()
                sleep(3)
                self.find_element(*self.StudentSeg).click()
            sleep(3)
            log.info('进入学员注册页面')

    def type_paymanage(self,num):
        '''财务管理'''
        log = Log()
        self.switch_to_content()
        if num ==1:
            l = self.isElementExist(*self.stdPay)
            if l:
                self.find_element(*self.stdPay).click()
            else:
                self.find_element(*self.PayManage).click()
                sleep(3)
                self.find_element(*self.stdPay).click()
            sleep(3)

            log.info('学员缴费管理页面！')
        elif num ==2:
            l = self.isElementExist(*self.stdPay)
            if l:
                self.find_element(*self.PayChack).click()
            else:
                self.find_element(*self.PayManage).click()
                sleep(3)
                self.find_element(*self.PayChack).click()
            sleep(3)
            log.info('学员缴费审核页面')

        elif num ==3:
            l = self.isElementExist(*self.stdPay)
            if l:
                self.find_element(*self.coupon).click()
            else:
                sleep(1)
                self.find_element(*self.PayManage).click()
                sleep(3)
                self.find_element(*self.coupon).click()
            sleep(3)
            log.info('学员优惠券管理页面')

        else: pass

    def type_domain(self):
        '''Domain'''
        log = Log()
        self.switch_to_content()
        self.find_element(*self.base).click()
        #顶部
        # js = "var q=document.getElementById('id').scrollTop=0"
        #底部
        js = "var q=document.documentElement.scrollTop=10000"
        self.get_execute_script(js)
        sleep(2)
        l = self.isElementExist(*self.domain1)
        if l:
            self.find_element(*self.domain1).click()
        else:
            self.find_element(*self.domain).click()
            sleep(3)
            self.find_element(*self.domain1).click()
            sleep(3)
        log.info('Domain页面！')


