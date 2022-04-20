#@Author:Hanpan
#@Time:2022/4/18  10:20
#@File:pymysqlTools.py


import pymysql


class pymysqlTools:
    '''
     pymysql常用操作封装：表数据查询、表数据更新（包含删除、插入、更新内容，一样的代码，只写了一个方法，都能用）
    数据库操作暂时没写
    '''

    def __init__(self):
        '''
        测试数据库连接
        '''
        test_port = 3306
        test_host = 'localhost'
        test_name = 'root'
        test_pwd = '123456'
        database = 'hptest'
        self.dbcon =pymysql.connect(user=test_name,password=test_pwd,host=test_host,port=test_port,database=database)

    def select_table(self,sql):
        '''
        查询，传select语句
        :param sql:传查询的sql语句
        :return:select结果数据全返回
        '''
        #创建游标，执行sql，最后关闭游标
        cursor = self.dbcon.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print('数据库查询错误')
            raise e
        finally:
            cursor.close()
            self.dbcon.close()

    def update_table(self,sql):
        '''
        表里数据更新、插入、删除，都适用
        :param sql:传表里insert、update、delete语句
        :return:
        '''
        cursor = self.dbcon.cursor()
        try:
           cursor.execute(sql)
           self.dbcon.commit()
        except Exception as e:
            #执行失败后，回滚，再抛出异常及提示语,updata/delete同
            self.dbcon.rollback()
            print('数据修改异常已回滚，报错信息：')
            raise e
        finally:
            cursor.close()
            self.dbcon.close()

    def updata_db(self):
        '''用不上，不写了，用的时候再写吧（(●'◡'●)）'''
        pass



# if __name__ == '__main__':
    # sql = 'insert into hp_users (userid,username,address,phone,createtime) values (2,"pp","北京市东城区","13200000001",current_timestamp());'
    # sqltool = pymysqlTools()
    # sqltool.update_table(sql=sql)
    # tol = pymysqlTools()
    # print(tol.dbcon)
    # sqlup = 'update hp_users set username="韩攀",address="北京市大兴区" where userid=1'
    # update = tol.update_table(sqlup)

    # sql = 'select * from hp_users;'
    # da = tol.select_table(sql)
    # print(da[0][1])








