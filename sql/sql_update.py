import pymysql
 
 
db = pymysql.connect(host='localhost', user='ogw', db='FLASK_BASIC', password='0515', charset='utf8')
curs = db.cursor()
 
sql = '''
update users set password = 'rhkd20801!'
where id = 'ogw0515';
'''
 
curs.execute(sql)
 
sql = "select * from users";
curs.execute(sql)
 
rows = curs.fetchall()
print(rows)
 
db.commit()
db.close()