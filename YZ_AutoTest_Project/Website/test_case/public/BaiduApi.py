from aip import AipOcr
import os
""" 你的 APPID AK SK """
APP_ID = '15734152'
API_KEY = 'o9M8Fesmj8GQGnyFAb8ZEOkM'
SECRET_KEY = '0XLVhSyukTT0DZjhsWMWvIjuI2t4vQu9'
class BaiduApi():
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    """ 读取图片 """
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def get_code(self):
        p1 = os.path.dirname(os.path.abspath('.'))
        p2 = "test_case\public\image\img0.png"
        file = os.path.join(p1, p2)
        image = self.get_file_content(file)
        """ 调用通用文字识别（高精度版） """
        # client.basicAccurate(image)

        """ 如果有可选参数 """
        options = {}
        options["detect_direction"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别（高精度版） """
        json1 = self.client.basicAccurate(image, options)
        x1 = json1['words_result'][0]['words']
        x2=x1.replace(' ', '')
        print(x1)
        print(x2)
        return x2



if __name__ == '__main__':
    code = BaiduApi()
    print(code.get_code())

