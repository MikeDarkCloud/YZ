from BasePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *
from XLExcel import *
from ConnectMysql import *
from CreateIdentity import *
from CreateMobile import *
from Log import *

class Auto_CJ_Register(Action,rewrxl):
    Recruit_students_loc=(By.CSS_SELECTOR,'.menu_dropdown > dl:nth-child(2) > dt:nth-child(1) > span:nth-child(2)')
    My_Student_loc=(By.CSS_SELECTOR,'.menu_dropdown > dl:nth-child(2) > dd:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)')
    Add_Student_loc=(By.CSS_SELECTOR,'span.r > a:nth-child(1)')
    Adult_Education_loc=(By.CSS_SELECTOR,'.layui-layer-content > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    Name_loc=(By.CSS_SELECTOR,'#stdName')
    Id_Card_loc=(By.CSS_SELECTOR,'#select2-idType-container')
    Id_Card1_loc=(By.CSS_SELECTOR,'//*[@id="select2-idType-result-cisn-1"]')
    Id_Code_loc=(By.CSS_SELECTOR,'#idCard')
    My_Iphone_loc=(By.CSS_SELECTOR,'#mobile')
    Nation_loc=(By.CSS_SELECTOR,'#select2-nation-container')
    H_Nation_loc=(By.CSS_SELECTOR,'#select2-nation-result-ulv2-01')
    Political_loc=(By.CSS_SELECTOR,'#select2-politicalStatus-container')
    Hukou_type_loc=(By.CSS_SELECTOR,'#select2-rprType-container')
    Hukou_type1_loc=(By.CSS_SELECTOR,'#select2-rprAddressCode-result-2yqv-440101')
    Hukou_addr_loc=(By.CSS_SELECTOR,'#select2-rprAddressCode-container')
    Hukou_addr1_loc=(By.CSS_SELECTOR,'#select2-nowProvinceCode-result-upct-19')
    E_Addr1_loc=(By.CSS_SELECTOR,'#select2-nowProvinceCode-container')
    E_Addr2_loc=(By.CSS_SELECTOR,'#select2-nowCityCode-container > span')
    E_Addr3_loc=(By.CSS_SELECTOR,'#select2-nowDistrictCode-container > span')
    Addr_loc=(By.CSS_SELECTOR,'#address')
    Occupation_loc=(By.CSS_SELECTOR,'#select2-jobType-container')
    Occupation1_loc=(By.CSS_SELECTOR,'#select2-jobType-result-cbby-00')
    Next_loc=(By.XPATH,'//*[@id="bt_baseInfo_next" and @class="next btn btn-primary radius"]')
    Next2_loc=(By.XPATH,'/html/body/article/div/form/fieldset[1]/div[2]/input')
    input_tag=(By.XPATH,'/html/body/article/div/form/fieldset[1]/div[2]/input')
    Education_loc=(By.XPATH,'//*[@id="select2-edcsType-container"]')
    Education1_loc=(By.CSS_SELECTOR,'#select2-edcsType-result-djw5-1')
    Academy_loc=(By.CSS_SELECTOR,'#unvsName')
    Graduation_Time_loc=(By.CSS_SELECTOR,'#graduateTime')
    Graduation_major_loc=(By.CSS_SELECTOR,'#profession')
    Graduation_Code_loc=(By.CSS_SELECTOR,'#diploma')
    Next1_loc =(By.CSS_SELECTOR,'#bt_baseInfo_next')
    Grade_loc=(By.CSS_SELECTOR,'#select2-pfsnLevel-container')
    Grade1_loc=(By.CSS_SELECTOR,'#select2-pfsnLevel-result-juzz-5')
    Type_loc=(By.CSS_SELECTOR,'#select2-enrollType-container')
    Type1_loc=(By.CSS_SELECTOR,'#select2-enrollType-result-nrps-1')
    Year_loc=(By.CSS_SELECTOR,'#select2-grade-container')
    Year1_loc=(By.CSS_SELECTOR,'#select2-grade-result-i65a-2020')
    First_Choice_loc=(By.CSS_SELECTOR,'#select2-unvsId-container ')
    First_Choice1_loc=(By.CSS_SELECTOR,'#select2-unvsId-container ')
    First_major=(By.CSS_SELECTOR,'#select2-pfsnId-container')
    Area_loc=(By.CSS_SELECTOR,'#select2-taId-container')
    Preservation_loc=(By.CSS_SELECTOR,'#bt_submit')
    Student_iframe=(By.XPATH,'//*[@id="iframe_box"]/div[1]/iframe')
    Addinfo_iframe=(By.XPATH,'/html/body/div[4]/div[2]/iframe')
    student_info=(By.XPATH,'//*[@id="layui-layer-iframe1"]')
    Dataa=(By.CSS_SELECTOR,'#birthdayInput')
    info=(By.CSS_SELECTOR,'#remark')
    Occupation3_loc=(By.CLASS_NAME,'onWindow-r-b')
    myPerformance_loc=(By.CSS_SELECTOR,'a.btn-success:nth-child(2)')
    #上传图片元素
    upload = "document.querySelectorALL(#DataTables_Table_0 > tbody > tr:nth-child(1) > td:nth-child(12) > a)[0].click()"
    upload3 = (By.NAME,'annexFile')
    Editor=(By.CSS_SELECTOR,'#DataTables_Table_0 > tbody > tr:nth-child(1) > td:nth-child(15) > a > i')
    Enclosure=(By.XPATH,'//*[@id="tab_demo"]/div[1]/span[4]')
    addphoto=(By.XPATH,'//a[text()="退出"]')
    inputimg=(By.CSS_SELECTOR,'#annexListTable > tbody > tr:nth-child(1) > td:nth-child(3) > form > div > input[type="hidden"]:nth-child(4)')
    click1 = (By.XPATH,'//*[@id="annexListTable"]/tbody/tr[1]/td[3]/form/div/p/a')
    text = (By.LINK_TEXT,'添加')
    def type_cheng_register(self):
        '''注册新的成教学员'''
        log=Log()
        self.switch_to_content()
        self.switch_to_frame(self.find_element(*self.Student_iframe))
        sleep(3)
        self.find_element(*self.Add_Student_loc).click()
        sleep(3)
        self.find_element(*self.Adult_Education_loc).click()
        sleep(3)
        self.switch_to_frame(self.find_element(*self.Addinfo_iframe))
        sleep(3)
        num=self.sread_xl()
        auto_name=('autoTest%s'%num)
        self.swrite_xl(num+1)
        self.write_xl('A',auto_name)
        log.info('学生姓名：%s' %auto_name)
        self.find_element(*self.Name_loc).click()
        self.find_element(*self.Name_loc).send_keys(auto_name)
        # self.def_send_keys(*self.Id_Card_loc,'身份证')
        # self.find_element(*self.Id_Card1_loc).click()
        # self.find_element(*self.Id_Card_loc).click()
        # self.find_element(*self.Id_Card_loc).send_keys(Keys.ENTER)
        # sleep(2)
        id_card = create_identity(int(area_dict1), 22, 1)
        self.write_xl('B',id_card)
        log.info('学生身份证：%s' %id_card)
        self.find_element(*self.Id_Code_loc).click()
        self.find_element(*self.Id_Code_loc).send_keys(id_card)
        sleep(2)
        self.find_element(*self.My_Iphone_loc).click()
        iphone=create_mobile()
        log.info('学生手机号：%s' % iphone)
        self.write_xl('C',iphone)
        self.find_element(*self.My_Iphone_loc).send_keys(iphone)
        sleep(2)
        self.find_element(*self.Nation_loc).click()
        sleep(1)
        self.find_element(*self.Nation_loc).send_keys('汉族')
        self.find_element(*self.Nation_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Political_loc).click()
        sleep(1)
        self.find_element(*self.Political_loc).send_keys('群众')
        self.find_element(*self.Political_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Hukou_type_loc).click()
        sleep(1)
        self.find_element(*self.Hukou_type_loc).send_keys('农村户口')
        self.find_element(*self.Hukou_type_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Hukou_addr_loc).click()
        sleep(1)
        self.find_element(*self.Hukou_addr_loc).send_keys('广州市辖')
        self.find_element(*self.Hukou_addr_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.E_Addr1_loc).click()
        sleep(1)
        self.find_element(*self.E_Addr1_loc).send_keys('广东')
        self.find_element(*self.E_Addr1_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.E_Addr2_loc).click()
        sleep(1)
        self.find_element(*self.E_Addr2_loc).send_keys('广州市')
        self.find_element(*self.E_Addr2_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.E_Addr3_loc).click()
        sleep(1)
        self.find_element(*self.E_Addr3_loc).send_keys('天河区')
        self.find_element(*self.E_Addr3_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Addr_loc).click()
        self.find_element(*self.Addr_loc).send_keys('冼村路5号')
        sleep(1)
        self.find_element(*self.Occupation_loc).click()
        sleep(2)
        self.find_element(*self.Occupation_loc).send_keys('专业技术人员')
        self.find_element(*self.Occupation_loc).send_keys(Keys.ENTER)
        sleep(2)
        jq_userName = "$('#bt_baseInfo_next').click()"
        self.get_execute_script(jq_userName)
        sleep(2)
        self.find_element(*self.Education_loc).click()
        sleep(1)
        self.find_element(*self.Education_loc).send_keys('普通高中毕业')
        self.find_element(*self.Education_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Academy_loc).click()
        self.find_element(*self.Academy_loc).send_keys('社会大学')
        sleep(1)
        js_time='document.getElementById("graduateTime").removeAttribute("readonly");'
        self.get_execute_script(js_time)
        js_value='document.getElementById("graduateTime").value="2012-01-01"'
        self.get_execute_script(js_value)
        # sleep(1)
        # self.find_element(*self.Graduation_Time_loc).clear()
        # self.find_element(*self.Graduation_Time_loc).send_keys('2012-01-01')
        sleep(0.5)
        self.find_element(*self.Graduation_major_loc).click()
        self.find_element(*self.Graduation_major_loc).send_keys('理科')
        sleep(1)
        self.find_element(*self.Graduation_Code_loc).click()
        self.find_element(*self.Graduation_Code_loc).send_keys('888888888')
        sleep(2)
        jq_userName1 = "$('#form-student-info > fieldset:nth-child(10) > div.text-r.mt-20 > input.next.btn.btn-primary.radius').click()"
        self.get_execute_script(jq_userName1)
        sleep(2)
        self.find_element(*self.Grade_loc).click()
        self.find_element(*self.Grade_loc).send_keys('高中起点高职高专')
        sleep(1)
        self.find_element(*self.Grade_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Type_loc).click()
        self.find_element(*self.Type_loc).send_keys('考试')
        sleep(1)
        self.find_element(*self.Type_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Year_loc).click()
        self.find_element(*self.Year_loc).send_keys('2020')
        sleep(1)
        self.find_element(*self.Year_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.First_Choice_loc).click()
        self.find_element(*self.First_Choice_loc).send_keys('华南农业大学')
        sleep(1)
        self.find_element(*self.First_Choice_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.First_major).click()
        self.find_element(*self.First_major).send_keys('工商企业管理')
        sleep(1)
        self.find_element(*self.First_major).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Area_loc).click()
        self.find_element(*self.Area_loc).send_keys('惠州惠城')
        sleep(1)
        self.find_element(*self.Area_loc).send_keys(Keys.ENTER)
        sleep(1)
        self.find_element(*self.Preservation_loc).send_keys(Keys.ENTER)
        sleep(5)
        m=ConnectMysql()
        learn_id = m.getlearnid(iphone)
        sleep(1)
        m.updatalearnannex(learn_id[0])
        sleep(2)
        m.updatalearn(learn_id)
        sleep(1)
        m.upstudent(iphone)
        sleep(5)
        return iphone


    def type_register_hint(self):
        '''录入成功断言：检查是否能定位到“我的绩效”'''
        return self.find_element(*self.myPerformance_loc).text




