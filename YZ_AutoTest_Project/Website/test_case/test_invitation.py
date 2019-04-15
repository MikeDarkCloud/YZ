from AdultRegisterPage import *
from InvitationPage import *
from myunit import *

class InvitationTest(StartEnd):
    '''邀约关系'''
    @unittest.skip('skip this test_invition case')
    def test_invition_1(self):
        '''测试邀约'''
        log=Log()
        log.info("开始测试没有上级没有跟进人邀约！")
        po1 = Invitation(self.driver)
        po1.open_new('https://zm-3.yzwill.cn/active/dreamBuild?scholarship=29&inviteId=hX1z5n9r352dUUp0i5ZQ%2BGUAdGMVGGmlUUWbUFegRlCY%2BlJ%2BpFZsphqmcjrawzs6KtyNUwJ9l80%3D')
        # po1.open1('https://test.yzwill.cn/active/dreamBuild?action=login&scholarship=&inviteId=%2FGrOUu77ThnAUntZezDXSn1XHzg3Ru65ZHRQj9CqXrlbtGngBVIUrqNdqp6sVx%2FD42S0Ph6KIKg%3D')
        sleep(4)
        po1.type_invitationregister()
        po1.type_invitationadult()
        log.info('邀约录入完毕！')

if __name__ == '__main__':
    unittest.main()