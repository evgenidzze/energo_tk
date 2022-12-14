import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()


#    for value in sql.execute("SELECT department FROM departments WHERE name = ?", (name,)):

def db():
    dep_list = []
    for info in sql.execute("SELECT * FROM departments"):
        dep_list.append(info)
    return dep_list


def get_names():
    so_names = []
    for value in db():
        name = value[1]
        if name not in so_names:
            so_names.append(name)
    return so_names


