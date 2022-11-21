import pymysql
 
db = pymysql.connect(host='localhost', user='ogw', db='FLASK_BASIC', password='0515', charset='utf8')
curs = db.cursor()
 
sql = '''insert into users values ('osw0218', 'tkd1885!')
'''
 
curs.execute(sql)
 
sql = "select * from users";
curs.execute(sql)
 
rows = curs.fetchall()
print(rows)
 
db.commit()
db.close()