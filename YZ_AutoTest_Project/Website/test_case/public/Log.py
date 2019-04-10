import logging, time, os
class Log:
    def __init__(self):
        # 文件的命名
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
    def __console(self,level, message):
        # 创建一个FileHandler，用于写到本地
        pwd = os.getcwd()
        p1 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
        p2 = "test_reprot\log"
        file = os.path.join(p1, p2)
        # file = 'C:\\Py\\bms-3\\YZ_AutoTest_Project\\Website\\test_reprot\\loginfo'
        self.logname = os.path.join(file, '%s.log'%time.strftime('%Y_%m_%d'))
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的追加模式

        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
    def debug(self, message):
        self.__console('debug', message)
    def info(self, message):
        self.__console('info', message)
    def warning(self, message):
        self.__console('warning', message)
    def error(self, message):
        self.__console('error', message)
if __name__ == '__main__':
    log = Log()
    log.info("---测试开始----")
    log.info("输入密码")
    log.warning("----测试结束----")

