from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from CreateMobile import *
from CreateIdentity import *
from selenium.webdriver.common.action_chains import ActionChains
class Action(object):
    def __init__(self,driver):
        self.driver = driver
        self.base_url='http://bms.yzwill.cn/toLogin.do'
        # self.base_url='http://bms-3.yzwill.cn/toLogin.do'
        #线上
        # self.base_url='https://new.yzou.cn/'

    def open(self):
        # self.driver.maximize_window()
        print("Test page is %s" % self.base_url)
        self.driver.get(self.base_url)
        sleep(5)
        assert self.driver.current_url==self.base_url

    def open_new(self,url):
        print("Test page is %s" %url)
        self.driver.get(url)
        assert self.driver.current_url == url

    def find_element(self,*loc):
        '''重写元素定位方法'''
        try:
            WebDriverWait(self.driver,5).until(lambda X: X.find_element(*loc)).is_displayed()
            return self.driver.find_element(*loc)
        except:
            print("页面元素未能找到元素！")

    def find_elements(self,*loc):
        '''重写元素定位方法'''
        try:
            WebDriverWait(self.driver,5).until(lambda X: X.find_element(*loc)).is_displayed()
            return self.driver.find_elements(*loc)
        except:
            print("页面元素未能找到元素！")

    def def_send_keys(self,*loc, vaule, clear_first=True, click_first=True):
        "重写send_keys方法"
        try:
            loc = getattr(self, "_%s" %loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print ("%s 页面中未能找到 %s 元素" % (self,loc))

    def switch_to_frame(self,*loca):
        "重写switch_to_frame方法"
        return self.driver.switch_to_frame(*loca)

    def switch_to_parent(self):
        "重写driver.switch_to.parent_frame方法"
        return self.driver.switch_to.parent_frame()

    def switch_to_content(self):
        "重写switch_to.default_content方法"
        return self.driver.switch_to.default_content()

    def isElementExist(self,*element):
        "重写is_displayed方法"
        try:
            p = self.driver.find_element(*element).is_displayed()
            # self.driver.find_element(*element)
            return p
        except:
            return False


    def get_execute_script(self,jss):
        '''定义执行js脚本方法'''
        return self.driver.execute_script(jss)

    def get_idcard(self):
        '''获取自动生成身份证号'''
        return create_identity(int(area_dict1), 22, 1)

    def get_mobile(self):
        '''获取自动生成手机号'''
        return create_mobile()

    def ActionChains(self,right_click):
        '''封装鼠标操作'''
        return ActionChains(self.driver).context_click(right_click).perform()
