from DingRegisterPage import *
from AdultRegisterPage import *
from AdultEntrance import *
from myunit import *

class DingDingRegisterTest(StartEnd):
    '''��������Ӧ��'''
    @unittest.skip('skip this case')
    def test_dingding_register_1(self):
        '''���Զ�������Ӧ�óɽ�ѧԱ¼��'''
        log=Log()
        log.info("test_register_normal is start test..")
        log.info("��ʼ���Զ���¼��ɽ�ѧԱ��Ϣ��")
        po2 = Auto_DCJ_register(self.driver)
        po2.open_new('http://test.yzwill.cn/recruit/login')
        po2.type_dd_login()
        po2.type_ddcj_register()
        log.info("���ԣ�")
        self.assertIsNotNone(po2.type_dregister_hint,msg=None)
        log.info("��ϲ������¼��ѧԱͨ��")

if __name__ == '__main__':
    unittest.main()






