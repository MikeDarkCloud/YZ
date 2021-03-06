from BasePage import *
from selenium.webdriver.common.by import By
from Log import *
from CreateIdentity import *
class StudentInfoModify(Action):
    '''新生信息修改申请'''
    newadd = (By.XPATH,'/html/body/div/div[2]/div/span/a[1]')
    ifrome0 = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    ifrome1 = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    addbtn = (By.XPATH,'/html/body/div/div[2]/div/div/table/tbody/tr/td[5]/a/i')
    namebtn = (By.CSS_SELECTOR,'#modify > div:nth-child(3) > div > a')
    inputname = (By.CSS_SELECTOR,'#newStdName')
    cardbtn = (By.XPATH,'/html/body/article/form/div[2]/div[3]/div/a')
    inputcard = (By.XPATH,'/html/body/article/form/div[2]/div[3]/div/div/input')
    school = (By.CSS_SELECTOR,'#modify > div:nth-child(6) > div > a')
    inputschool = (By.CSS_SELECTOR,'#select2-newUnvsId-container')
    inputschool1 = (By.CSS_SELECTOR,'body > span > span > span.select2-search.select2-search--dropdown > input')
    inputschool2 = (By.CSS_SELECTOR,'#select2-newUnvsId-results > li')
    grade = (By.CSS_SELECTOR,'#select2-pfsnLevels2-container')
    grade1 = (By.CSS_SELECTOR,'body > span > span > span.select2-search.select2-search--dropdown > input')
    grade2 = (By.CSS_SELECTOR,'#select2-pfsnLevels2-result-jfyf-5')
    major = (By.CSS_SELECTOR,'#select2-newPfsnId-container')
    major1 = (By.CSS_SELECTOR,'#select2-newPfsnId-container')
    major2 = (By.CSS_SELECTOR,'##select2-newPfsnId-results > li.select2-results__option.select2-results__option--highlighted')
    area = (By.CSS_SELECTOR,'#select2-newTaId-container')
    area1 = (By.CSS_SELECTOR,'body > span > span > span.select2-search.select2-search--dropdown > input')
    area2 = (By.CSS_SELECTOR,'#select2-newTaId-results > li.select2-results__option.select2-results__option--highlighted')
    submit = (By.XPATH,'/html/body/article/form/div[3]/input[1]')
    chiframe = (By.XPATH,'/html/body/section/div[2]/div[1]/iframe')
    chiframe1 = (By.XPATH,'/html/body/div[3]/div[2]/iframe')
    chmobile = (By.XPATH,'/html/body/div/div[1]/div/div/div[2]/input')
    chsearch = (By.XPATH,'/html/body/div/div[1]/div/div/div[4]/a[1]')
    assert_element = (By.XPATH,'//*[@id="mobile"]')
    def type_student_change(self,iphone):
        '''进入新生信息修改页面'''
        log=Log()
        log.info('新生信息修改页面！')
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.chiframe))
        sleep(5)
        self.find_element(*self.newadd).click()
        sleep(6)
        wind = self.find_element(*self.ifrome1)
        self.switch_to_frame(wind)
        sleep(2)
        self.find_element(*self.chmobile).click()
        self.find_element(*self.chmobile).send_keys(iphone)
        sleep(1)
        self.find_element(*self.chsearch).click()
        sleep(2)
        self.find_element(*self.addbtn).click()
        sleep(2)
        self.switch_to_frame(self.find_element(*self.chiframe1))
        sleep(1)
        self.find_element(*self.cardbtn).click()
        sleep(1)
        log.info("修改更换身份证号！")
        id_card = create_identity(int(area_dict1), 22, 1)
        log.info("更换的身份证号为：%s" %id_card)
        self.find_element(*self.inputcard).click()
        self.find_element(*self.inputcard).send_keys(id_card)
        sleep(1)
        self.find_element(*self.submit).click()
        sleep(5)
        log.info("新生信息修改完毕！")

    def type_student_modify_success(self):
        '''新生信息修改完成断言'''
        self.isElementExist(*self.assert_element)



