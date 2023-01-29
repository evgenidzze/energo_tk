import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()


def get_departments():
    res = sql.execute("SELECT * FROM departments").fetchall()
    my_dict = {i[0]: list(i[1:]) for i in res}
    return my_dict


def get_so():
    res = sql.execute("SELECT * FROM so_names").fetchall()
    my_dict = {i[1]: [i[0], i[2], i[3], i[4]] for i in res}
    return my_dict


rod_months = {'січень': ['січня', '01'], 'лютий': ['лютого', '02'], 'березень': ['березня', '03'],
              'квітень': ['квітня', '04'],
              'травень': ['травня', '05'], 'червень': ['червня', '06'], 'липень': ['липня', '07'],
              'серпень': ['серпня', '08'],
              'вереснь': ['вересня', '09'], 'жовтень': ['жовтня', '10'], 'листопад': ['листопада', '11'],
              'грудень': ['грудня', '12']}
