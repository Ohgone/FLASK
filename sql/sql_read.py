import pymysql
 
def read(id, password):  
    code = False
    db = pymysql.connect(host='localhost', user='ogw', db='FLASK_BASIC', password='0515', charset='utf8')
    curs = db.cursor()
    sql = f"select count(*) from users where id='{id}' and password='{password}'";
    curs.execute(sql)
    rows = curs.fetchone()
    if rows[0] == 1:
        code = True
    db.commit()
    db.close()
    return code

def read_name(id):  
    name = ''
    db = pymysql.connect(host='localhost', user='ogw', db='FLASK_BASIC', password='0515', charset='utf8')
    curs = db.cursor()
    sql = f"select name from users where id='{id}'";
    curs.execute(sql)
    rows = curs.fetchone()
    name = rows[0] 
    db.commit()
    db.close()
    return name