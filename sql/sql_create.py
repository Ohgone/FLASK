import pymysql
 
def create(name, id, password):
    db = pymysql.connect(host='localhost', user='ogw', db='FLASK_BASIC', password='0515', charset='utf8')
    curs = db.cursor()
    sql = f"insert into users values ('{name}', '{id}', '{password}')";
    curs.execute(sql)
    db.commit()
    db.close()