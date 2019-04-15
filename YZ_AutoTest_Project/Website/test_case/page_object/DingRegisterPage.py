from BasePage import *
from selenium.webdriver.common.by import By
from XLExcel import *
from Log import *
from CreateIdentity import *
from CreateMobile import *

class Auto_DCJ_register(Action,rewrxl):
    url ='http: // test.yzwill.cn / recruit / login'
    ddusername = (By.CSS_SELECTOR, 'body > div > div > div.bd > div:nth-child(1) > input')
    ddpwd = (By.CSS_SELECTOR,'body > div > div > div.bd > div:nth-child(2) > input')
    ddsubmit = (By.CSS_SELECTOR,'body > div > div > div.bd > div.item.mt-23 > button')
    stdquery = (By.CSS_SELECTOR,'body > div > div > div.btns > a.link.bg1')
    addstd = (By.CSS_SELECTOR,'body > div > div > div.top-bar > div > div > div.rt > a')
    Adult_Education = (By.CSS_SELECTOR,'body > div > div > div.btns > a.link.bg1')
    ddname = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(1) > div.rt > input')
    ddid = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(3) > div.rt > input')
    ddiphone = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(6) > div.rt > input')
    dnation = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(7)')
    ensure1 = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(5) > div.mint-popup.mint-popup-bottom > div > div.commonPop-title > span:nth-child(2)')
    politics = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(8)')
    ensure2 = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(6) > div.mint-popup.mint-popup-bottom > div > div.commonPop-title > span:nth-child(2)')
    dhukou = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(9)')
    ensure3 = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(7) > div.mint-popup.mint-popup-bottom > div > div.commonPop-title > span:nth-child(2)')
    hukouadd = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(10)')
    ensure4 = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(10) > div.mint-popup.mint-popup-bottom > div > div.commonPop-title > span:nth-child(2)')
    eaddress = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(11)')
    eaddress1 = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(12) > div > div.commonPop-box-content > div.addressJD-content > div.addressJD-content-item > ul > li > span')
    eaddress2 = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(12) > div > div.commonPop-box-content > div.addressJD-content > div.addressJD-content-item > ul > li:nth-child(1)')
    eaddress3 = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(12) > div > div.commonPop-box-content > div.addressJD-content > div.addressJD-content-item > ul > li:nth-child(1)')
    eaddress4 = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(12) > div.rt > input')
    next1 = (By.CSS_SELECTOR,'body > div > div > div > div.footer > div > div')
    edutype = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div.item.mt')
    edusure = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(3) > div.mint-popup.mint-popup-bottom > div > div.commonPop-title > span:nth-child(2)')
    oldedu = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(2) > div.rt > input')
    eduadd = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(3)')
    eduasure = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(8) > div > div.commonPop-title > span:nth-child(2)')
    edutime = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(4)')
    edutsure = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(9) > div > div.picker-toolbar > span.mint-datetime-action.mint-datetime-confirm')
    edutime1 = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(5)')
    edutsure1 = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(10) > div > div.picker-toolbar > span.mint-datetime-action.mint-datetime-confirm')
    oldmajor = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(6) > div.rt > input')
    macode = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(7) > div.rt > input')
    oledu = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(8)')
    eduosure = (By.CSS_SELECTOR,'body > div > div > div > div:nth-child(4) > div.mint-popup.mint-popup-bottom > div > div.commonPop-title > span:nth-child(2)')
    edunext = (By.CSS_SELECTOR,'body > div > div > div > div.footer > div > div')
    edunext1 = (By.CSS_SELECTOR,'body > div > div > div > div.footer > div > div')
    uac = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(4)')
    nuac = (By.CSS_SELECTOR,'body > div > div > div > div.children-page > div > div > div > div:nth-child(3)')
    nmajor = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(5)')
    nmajor1 = (By.CSS_SELECTOR,'body > div > div > div > div.children-page > div > div > div > div:nth-child(4)')
    exar = (By.CSS_SELECTOR,'body > div > div > div > div.widget-list > div:nth-child(6)')
    exar1 = (By.CSS_SELECTOR,'body > div > div > div > div.children-page > div > div > div > div:nth-child(1)')
    savebutton = (By.CSS_SELECTOR,'body > div > div > div > div.footer > div > div')

    def type_dd_login(self):
        self.find_element(*self.ddusername).click()
        self.find_element(*self.ddusername).send_keys('蓝明勇')
        self.find_element(*self.ddpwd).click()
        self.find_element(*self.ddpwd).send_keys('Yz123456')
        sleep(15)
        self.find_element(*self.ddsubmit).click()

    def type_ddcj_register(self):
        log=Log()
        self.find_element(*self.stdquery).click()
        sleep(1)
        self.find_element(*self.addstd).click()
        sleep(1)
        self.find_element(*self.Adult_Education).click()
        num = self.sread_xl()
        auto_name = ('dautoTest%s' % num)
        self.swrite_xl(num + 1)
        self.write_xl('A', auto_name)
        log.info('钉钉学生姓名：%s' % auto_name)
        sleep(1)
        self.find_element(*self.ddname).click()
        sleep(1)
        self.find_element(*self.ddname).send_keys(auto_name)
        sleep(1)
        id_card = create_identity(int(area_dict1), 22, 1)
        self.write_xl('B', id_card)
        log.info('钉钉学生身份证：%s' % id_card)
        sleep(1)
        self.find_element(*self.ddid).click()
        sleep(1)
        self.find_element(*self.ddid).send_keys(id_card)
        iphone = create_mobile()
        self.write_xl('C', iphone)
        log.info('钉钉学生手机号：%s' % iphone)
        sleep(1)
        self.find_element(*self.ddiphone).click()
        sleep(5)
        self.find_element(*self.ddiphone).send_keys(iphone)
        sleep(1)
        self.find_element(*self.dnation).click()
        sleep(3)
        self.find_element(*self.ensure1).click()
        sleep(1)
        self.find_element(*self.politics).click()
        sleep(1)
        self.find_element(*self.ensure2).click()
        sleep(1)
        #顶部
        # js = "var q=document.getElementById('id').scrollTop=0"
        #底部
        js = "var q=document.documentElement.scrollTop=10000"
        self.get_execute_script(js)
        sleep(1)
        self.find_element(*self.dhukou).click()
        sleep(1)
        self.find_element(*self.ensure3).click()
        sleep(1)
        self.find_element(*self.hukouadd).click()
        sleep(1)
        self.find_element(*self.ensure4).click()
        sleep(1)
        self.find_element(*self.eaddress).click()
        sleep(1)
        self.find_element(*self.eaddress1).click()
        sleep(1)
        self.find_element(*self.eaddress2).click()
        sleep(1)
        self.find_element(*self.eaddress3).click()
        sleep(1)
        self.find_element(*self.eaddress4).click()
        sleep(1)
        self.find_element(*self.eaddress4).send_keys("猎德街冼村4号")
        sleep(1)
        self.find_element(*self.next1).click()
        sleep(1)
        self.find_element(*self.edutype).click()
        sleep(1)
        self.find_element(*self.edusure).click()
        sleep(1)
        self.find_element(*self.oldedu).click()
        sleep(1)
        self.find_element(*self.oldedu).send_keys("社会小学")
        sleep(1)
        self.find_element(*self.eduadd).click()
        sleep(1)
        self.find_element(*self.eduasure).click()
        sleep(1)
        self.find_element(*self.edutime).click()
        sleep(1)
        self.find_element(*self.edutsure).click()
        sleep(1)
        self.find_element(*self.edutime1).click()
        sleep(1)
        self.find_element(*self.edutsure1).click()
        sleep(1)
        self.find_element(*self.oldmajor).click()
        sleep(1)
        self.find_element(*self.oldmajor).send_keys("使劲玩")
        sleep(1)
        self.find_element(*self.macode).click()
        sleep(1)
        self.find_element(*self.macode).send_keys("888888")
        sleep(1)
        self.find_element(*self.oledu).click()
        sleep(1)
        self.find_element(*self.eduosure).click()
        sleep(1)
        self.find_element(*self.edunext).click()
        sleep(1)
        self.find_element(*self.uac).click()
        sleep(1)
        self.find_element(*self.nuac).click()
        sleep(1)
        self.find_element(*self.nmajor).click()
        sleep(1)
        self.find_element(*self.nmajor1).click()
        sleep(1)
        self.find_element(*self.exar).click()
        sleep(1)
        self.find_element(*self.exar1).click()
        sleep(1)
        self.find_element(*self.savebutton).click()
        sleep(5)

    def type_dregister_hint(self):
        return self.find_element(*self.Adult_Education).text















