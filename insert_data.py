# coding=utf-8


import pymysql


db = pymysql.connect("localhost", "zhidu", "zhidu123456", "tchat")
cursor = db.cursor()
sql = """
    insert into userinfo(username, nickname, email, password) values("xqs", "xqs", "001qq@.com", "12345");
"""
cursor.execute(sql)
db.commit()
db.close()
