from BasePage import *
from selenium.webdriver.common.by import By
from ConnectMysql import *

class AdultEntrance(Action):
    '''入学成绩'''
    Student_iframe = (By.XPATH, '/html/body/section/div[2]/div[1]/iframe')
    Edit = (By.CSS_SELECTOR,'#DataTables_Table_0 > tbody > tr:nth-child(1) > td:nth-child(9) > a > i')
    Entrance = (By.XPATH,'//*[@id="layui-layer-iframe1"]')
    Maths = (By.CSS_SELECTOR,'#course > tr:nth-child(1) > td:nth-child(2) > input')
    Chinese = (By.CSS_SELECTOR,'#course > tr:nth-child(2) > td:nth-child(2) > input')
    English = (By.CSS_SELECTOR,'#course > tr:nth-child(3) > td:nth-child(2) > input')
    putin = (By.CSS_SELECTOR,'#form-member-add > div:nth-child(4) > div > input')
    search = (By.CSS_SELECTOR,'body > div > div.text-l.search > div > div:nth-child(1) > div.f-r.mr-15 > a.btn.btn-primary.radius')
    '''学员录取'''
    sEdit = (By.CSS_SELECTOR,'#enrollTable > tbody > tr > td:nth-child(13) > a > i')
    sEntrance = (By.XPATH, '//*[@id="layui-layer-iframe1"]')
    recruit = (By.CSS_SELECTOR,'#subDiv > input')
    ssearch = (By.CSS_SELECTOR,'#enrollForm > div > div:nth-child(1) > div.f-r.mr-5 > a.btn.btn-primary.radius')

    def type_entrance_score(self):
        '''入学成绩'''
        log=Log()
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.Student_iframe))
        sleep(3)
        self.find_element(*self.Edit).click()
        sleep(2)
        self.switch_to_frame(self.find_element(*self.Entrance))
        self.find_element(*self.Maths).click()
        self.find_element(*self.Maths).send_keys('80')
        self.find_element(*self.Chinese).click()
        self.find_element(*self.Chinese).send_keys('80')
        self.find_element(*self.English).click()
        self.find_element(*self.English).send_keys('80')
        sleep(1)
        self.find_element(*self.putin).click()
        log.info('学员入学成绩输入完毕！')

    def type_score_hint(self):
        log = Log()
        log.info('断言！')
        self.find_element(*self.search)


    def type_student_recruit(self):
        '''学员录取'''
        log=Log()
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.Student_iframe))
        sleep(3)
        self.find_element(*self.sEdit).click()
        sleep(2)
        self.switch_to_frame(self.find_element(*self.sEntrance))
        self.find_element(*self.recruit).click()
        log.info('学员录取完毕！')

    def type_recruit_hint(self):
        log = Log()
        log.info('断言！')
        self.find_element(*self.ssearch)

