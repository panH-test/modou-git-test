#@Author:Hanpan
#@Time:2022/4/18  10:20
#@File:pymysqlTools.py


import pymysql


class pymysqlTools:
    '''
    pymysql常用操作封装：表数据查询、表数据更新、表数据删除、表数据插入
    数据库操作没写
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
            print('数据修改异常，回归了，报错信息：')
            raise e
        finally:

            cursor.close()
            self.dbcon.close()

    def insert_table(self):
        '''
        表数据更新，传insert语句
        :param sql:
        :return:
        '''
        pass

    def delect_table(self):
        '''
        表数据删除，传delete语句
        :param sql:
        :return:
        '''
        pass

    def updata_db(self):
        '''用不上，不写了，用的时候再写吧（(●'◡'●)）'''
        pass



# if __name__ == '__main__':
#     tol = pymysqlTools()
#     print(tol.dbcon)
#     sqlup = 'update hp_users set username="韩攀",address="北京市大兴区" where userid=1'
#     update = tol.update_table(sqlup)

    # sql = 'select * from hp_users;'
    # da = tol.select_table(sql)
    # print(da[0][1])





