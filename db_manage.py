# from sqlalchemy import *
# from sqlalchemy.sql import select
#
# engine = create_engine("sqlite:///server.db", echo=True)
# meta = MetaData(engine)
#
# department = Table('departments', meta, autoload=True)
#
# conn = engine.connect()
# s = select(department).where(department.c.so_id == 1)
# res = conn.execute(s)
#
# a = res.fetchall()
# print(a[0])
# print(a[1])
import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

q1 = sql.execute("SELECT D.department, S.name FROM departments D, so_names S"
                 "WHERE ")
for q in q1:
    print(q)