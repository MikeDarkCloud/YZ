from AdultRegisterPage import *
from InvitationPage import *
from myunit import *

class InvitationTest(StartEnd):
    '''邀约关系'''
    # @unittest.skip('skip this test_invition case')
    def test_invition_1(self):
        '''测试邀约'''
        # log=Log()
        # log.info("开始测试没有上级没有跟进人邀约！")
        po1 = Invitation(self.driver)
        po1.open_new('http://zm-3.yzwill.cn/invite?action=login&inviteId=UZ5tMwCISnWidZpIrg3JG%2Bdhkr9RqkZfcmh8vruXLhlYEjlbHjCmdex%2Fy9LgEE%2Fykq82LOn8YIIzkCBkxnDdkw%3D%3D')
        # po1.open1('https://test.yzwill.cn/active/dreamBuild?action=login&scholarship=&inviteId=%2FGrOUu77ThnAUntZezDXSn1XHzg3Ru65ZHRQj9CqXrlbtGngBVIUrqNdqp6sVx%2FD42S0Ph6KIKg%3D')
        sleep(4)
        po1.type_invitationregister()
        po1.type_invitationadult()
        # log.info('邀约录入完毕！')

if __name__ == '__main__':
    unittest.main()