import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.1.90', port=3306, user='yanfa', passwd='yanfa#123', db='db_nono', charset='utf8')

# 通过cursor获取游标
cursor = db.cursor()

sql = '''
SELECT * from db_nono.finance_log where id=1863311026
'''

cursor.execute(sql)

date = cursor.fetchone()
print("查询结果", date)

findSql = """
SELECT * from db_nono.finance_log where id>=1863311026
"""
updateSql = "UPDATE db_nono.finance_log set account_id=159803073 where id=1863311026"

type = 'findSql'
try:
    cursor.execute(findSql)
    db.commit()
    print("影响行数", cursor.rowcount)
    if type == 'findSql':
        for date in cursor.fetchall():
            print(date)
except Exception as e:
    print("执行失败", e)
    db.rollback()

cursor.close()

