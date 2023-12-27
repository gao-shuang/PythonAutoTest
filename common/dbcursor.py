import pymysql

## 打开数据库连接
db = pymysql.connect(host='10.60.48.2', user='trinahome', password='cSWnd5n36Pr9Aq7Fp3Du', database='th_db_ems', port=13206)
## 使用cursor()对象创建游标对象
cursor = db.cursor()
## 执行查询execute()执行查询
cursor.execute("select * from tb_enterprise")
## 使用fetchone()获取单条数据
data = cursor.fetchone()
print(data)
db.close()