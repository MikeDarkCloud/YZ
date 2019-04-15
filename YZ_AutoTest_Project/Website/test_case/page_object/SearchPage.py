from BasePage import *
from selenium.webdriver.common.by import By
from Log import *
class Search(Action):
    '''我的学员页面搜索'''
    mobile = (By.CSS_SELECTOR,'#mobile')
    stdname = (By.CSS_SELECTOR,'#stdName')
    card_id = (By.CSS_SELECTOR,'#idCard')
    empty = (By.CSS_SELECTOR,'#searchForm > div:nth-child(1) > div.f-r.mr-15 > a.btn.btn-normal-outline.radius')
    search = (By.CSS_SELECTOR,'#searchForm > div:nth-child(1) > div.f-r.mr-15 > a.btn.btn-primary.radius')
    '''学员缴费管理页面搜索'''
    Student_iframe = (By.XPATH, '/html/body/section/div[2]/div[1]/iframe')
    pmobile = (By.XPATH,'/html/body/div/div[1]/div/div[1]/div[2]/input')
    pname = (By.CSS_SELECTOR,'#stdName')
    pcard_id = (By.CSS_SELECTOR,'#idCard')
    pempty = (By.XPATH,'/html/body/div/div[1]/div/div[1]/div[4]/a[2]')
    psearch = (By.XPATH,'/html/body/div/div[1]/div/div[1]/div[4]/a[1]')
    '''学员缴费审核页面搜索'''
    siframe = (By.XPATH, '/html/body/section/div[2]/div[1]/iframe')
    siframe2 = (By.XPATH,'/html/body/section/div[2]/div[6]/iframe')
    siframe3 = (By.XPATH,'/html/body/section/div[2]/div[6]/iframe')
    cmobile = (By.CSS_SELECTOR,'#mobile')
    cname = (By.CSS_SELECTOR,'#stdName')
    ccard_id = (By.CSS_SELECTOR,'#idCard')
    cempty = (By.CSS_SELECTOR,'#export-form > div > div > div:nth-child(1) > div.f-r.mr-15 > a.btn.btn-normal-outline.radius')
    csearch = (By.CSS_SELECTOR,'#export-form > div > div > div:nth-child(1) > div.f-r.mr-15 > a.btn.btn-primary.radius')
    '''考前确认'''
    iframe = (By.XPATH, '/html/body/section/div[2]/div[1]/iframe')
    kname = (By.CSS_SELECTOR,'#stdName')
    kcard = (By.CSS_SELECTOR,'#idCard')
    kmobile = (By.CSS_SELECTOR,'#telephone')
    ksearch = (By.CSS_SELECTOR,'#tab_demo > div:nth-child(2) > div > div.text-l.search > div > div:nth-child(1) > div.f-r.mr-5 > a.btn.btn-primary.radius')
    kempty = (By.CSS_SELECTOR,'#searchForm > div:nth-child(1) > div.f-r.mr-5 > a.btn.btn-normal-outline.radius')
    '''考前资料核查'''
    qname = (By.CSS_SELECTOR,'#stdName')
    qcard =(By.CSS_SELECTOR,'#idCard')
    qmobile = (By.XPATH,'//*[@id="mobile"]')
    qsearcch = (By.XPATH,'/html/body/div/div[1]/div/form/div[1]/div[4]/a[1]')
    qempty = (By.CSS_SELECTOR,'#tab_demo > div:nth-child(2) > div > div.text-l.search > div > div:nth-child(1) > div.f-r.mr-5 > a.btn.btn-normal-outline.radius')
    '''入学考试搜索'''
    Eiframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    Emobile = (By.XPATH,'/html/body/div/div[1]/div/div[1]/div[2]/input')
    Esearch = (By.XPATH,'/html/body/div/div[1]/div/div[1]/div[4]/a[1]')
    '''学员录取'''
    riframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    rmobile = (By.XPATH,'/html/body/div/div[2]/div/form/div/div[1]/div[3]/input')
    rsearch = (By.XPATH,'/html/body/div/div[2]/div/form/div/div[1]/div[4]/a[1]')
    '''学员异动管理'''
    chiframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    chmobile = (By.XPATH,'/html/body/div/div[1]/form/div/div[1]/div[2]/input')
    chsearch = (By.XPATH,'/html/body/div/div[1]/form/div/div[1]/div[4]/a[1]')
    '''转报学员'''
    zbiframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    zbiframe1 = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    zbnewadd = (By.XPATH,'/html/body/div/div[2]/div/span/a[1]')
    zbmobile = (By.XPATH,'/html/body/div/div[1]/div/div/div[2]/input')
    zbsearch = (By.XPATH,'/html/body/div/div[1]/div/div/div[4]/a[1]')
    '''退学学员'''
    oiframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    oadd = (By.XPATH,'/html/body/div/div[2]/div/span/a[1]')
    oiframe1 = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    omobile = (By.XPATH,'/html/body/div/div[1]/div/div/div[2]/input')
    osearch = (By.XPATH,'/html/body/div/div[1]/div/div/div[4]/a[1]')
    outadd = (By.XPATH,'/html/body/div/div[2]/div/div/table/tbody/tr/td[5]/a/i')

    '''退学审核'''
    uiframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    umobile = (By.XPATH,'/html/body/div/div[2]/form/div/div/div/div[1]/div[3]/input')
    usearch = (By.XPATH,'/html/body/div/div[2]/form/div/div/div/div[1]/div[4]/a[1]')
    ueduiter = (By.XPATH,'/html/body/div/div[3]/div/div/div/div/div/table/tbody/tr/td[16]/a/i')


    def mystd_search(self,iphone):
        '''我的学员页面搜索'''
        log=Log()
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.Student_iframe))
        log.info('搜索学员')
        self.find_element(*self.empty).click()
        sleep(3)
        self.find_element(*self.mobile).click()
        self.find_element(*self.mobile).send_keys(iphone)
        self.find_element(*self.search).click()

    def pay_search(self,iphone,num):
        '''学员缴费管理页面搜索'''
        log=Log()
        self.switch_to_content()
        if num == 1:
            self.switch_to_frame(self.find_element(*self.siframe))
        elif num == 2:
            self.switch_to_frame(self.find_element(*self.siframe))
        elif num == 3:
            self.switch_to_frame(self.find_element(*self.siframe2))
        log.info('搜索学员')
        sleep(2)
        self.find_element(*self.pmobile).clear()
        sleep(2)
        self.find_element(*self.pmobile).click()
        sleep(2)
        self.find_element(*self.pmobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.psearch).click()
        sleep(2)

    def pay_check_search(self,iphone):
        '''学员缴费审核页面搜索'''
        log=Log()
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.Student_iframe))
        log.info('搜索学员')
        self.find_element(*self.cempty).click()
        sleep(2)
        self.find_element(*self.cmobile).click()
        sleep(2)
        self.find_element(*self.cmobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.csearch).click()
        sleep(2)




    def exam_search(self,iphone):
        '''考前资料核查'''
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.iframe))
        sleep(2)
        self.find_element(*self.qmobile).click()
        self.find_element(*self.qmobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.qsearcch).click()

    def exam_befor_search(self,iphone):
        '''考前确认搜索'''
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.iframe))
        sleep(2)
        self.find_element(*self.kmobile).click()
        self.find_element(*self.kmobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.ksearch).click()

    def type_enter_score(self,iphone):
        '''入学考试搜索'''
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.Eiframe))
        sleep(2)
        self.find_element(*self.Emobile).click()
        self.find_element(*self.Emobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.Esearch).click()
        sleep(2)

    def type_student_recruit(self,iphone):
        '''入学考试搜索'''
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.riframe))
        sleep(2)
        self.find_element(*self.rmobile).click()
        self.find_element(*self.rmobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.rsearch).click()
        sleep(2)

    def type_std_change(self,iphone):
        '''入学考试搜索'''
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.chiframe))
        sleep(2)
        self.find_element(*self.chmobile).click()
        self.find_element(*self.chmobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.chsearch).click()
        sleep(2)

    def type_zbnew_search(self,iphone):
        '''新增转报搜索'''
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.zbiframe))
        sleep(2)
        self.find_element(*self.zbnewadd).click()
        sleep(4)
        self.switch_to_frame(self.find_element(*self.zbiframe1))
        self.find_element(*self.zbmobile).clear()
        self.find_element(*self.zbmobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.zbsearch).click()
        sleep(2)

    def type_stdout_search(self,iphone):
        '''新增退学搜索'''
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.oiframe))
        sleep(2)
        self.find_element(*self.oadd).click()
        sleep(4)
        self.switch_to_frame(self.find_element(*self.oiframe1))
        self.find_element(*self.omobile).clear()
        self.find_element(*self.omobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.osearch).click()
        sleep(2)
        self.find_element(*self.outadd).click()
        sleep(5)


    def type_stdout_examine(self,iphone):
        '''退学审核搜索'''
        self.switch_to_frame(self.find_element(*self.uiframe))
        sleep(1)
        self.find_element(*self.umobile).click()
        self.find_element(*self.umobile).send_keys(iphone)
        sleep(2)
        self.find_element(*self.usearch).click()
        sleep(2)






