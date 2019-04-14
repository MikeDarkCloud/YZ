import pymysql
import datetime
from  Website.test_case.public.Log import *
# 打开数据库连接
class GetMsql():
    def updatalearnannex(self,learn_id):
        '''设置成教学员附件资料'''
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db = pymysql.connect("10.0.0.224", "root", "databases001", "bms")
        # db = pymysql.connect("120.24.167.89", "yzDev", "@yZdev0512!", "bms")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = ("UPDATE bms.bd_learn_annex SET annex_url = 'std/155114117217621675/3BD56545A9924CE0BB8C7333308D1695.jpg',annex_status = 2,upload_user = '蓝明勇',upload_user_id = '153968138096924081',upload_time = '%s' WHERE learn_id = '%s' AND annex_type IN ( '1', '2', '3' )" % (nowTime,learn_id))
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()

    def upgklearnannex(self,learn_id):
        '''设置国开学员附件资料'''
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db = pymysql.connect("10.0.0.224", "root", "databases001", "bms")
        # db = pymysql.connect("120.24.167.89", "yzDev", "@yZdev0512!", "bms")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = ("UPDATE bms.bd_learn_annex SET annex_url = 'std/155114117217621675/3BD56545A9924CE0BB8C7333308D1695.jpg',annex_status = 2,upload_user = '蓝明勇',upload_user_id = '153968138096924081',upload_time = '%s' WHERE learn_id = '%s' AND annex_type IN ( '5' )" % (nowTime,learn_id))
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()

    def getlearnid(self,mobile):
        '''获取学员learn_id'''
        log=Log()
        db = pymysql.connect("10.0.0.224","root","databases001","bms")
        # db = pymysql.connect("120.24.167.89", "yzDev", "@yZdev0512!", "bms")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT learn_id FROM bms.bd_learn_info where std_id =(SELECT std_id FROM bms.bd_student_info WHERE mobile = '%s') "% mobile)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # data = cursor.fetchall()
        # print(data)
        log.info("Database learn_id : %s " % data)
        # 关闭数据库连接
        db.close()
        return data

    def getstdid(self,mobile):
        '''获取学员std_id'''
        log=Log()
        db = pymysql.connect("10.0.0.224","root","databases001","bms")
        # db = pymysql.connect("120.24.167.89", "yzDev", "@yZdev0512!", "bms")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT std_id FROM bms.bd_student_info WHERE mobile = '%s' "% mobile)
        # 使用 fetchone() 方法获取元组单条数据.
        # data = cursor.fetchone()
        data = cursor.fetchall()
        log.info("Database learn_id : %s " % data)
        # 关闭数据库连接
        db.close()
        return data

    def updatalearn(self,learn_id):
        '''设置学员附件资料状态'''
        db = pymysql.connect("10.0.0.224","root","databases001","bms")
        # db = pymysql.connect("120.24.167.89", "yzDev", "@yZdev0512!", "bms")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = "update bd_learn_info set annex_status = '2' WHERE learn_id = '%s'" %learn_id
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()


    def upstudent(self,mobile):
        '''设置学员附件资料状态'''
        db = pymysql.connect("10.0.0.224","root","databases001","bms")
        # db = pymysql.connect("120.24.167.89", "yzDev", "@yZdev0512!", "bms")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql1= "SELECT sex FROM bms.bd_student_info WHERE mobile = '%s'" %mobile
        sql = "UPDATE bms.bd_student_info SET sex = '2', birthday  = '1992-07-07' WHERE mobile = '%s'" %mobile
        try:
            # 执行SQL语句
            cursor.execute(sql1)
            sex = cursor.fetchall()
            sex1=sex[0][0]
            if sex1 == '':
                cursor.execute(sql)
            else:
                pass
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()

if __name__ == '__main__':
    l=GetMsql()
    # l.upstudent(13956180400)
    learn = l.getlearnid('15019383463')
    # print('ffff'+learn)
    # learn = '155122744820156254'
    # l.updatalearnannex(learn)
    # l.updatalearn(learn)
