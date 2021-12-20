import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , earnings integer , exercise text , study text , diet text ,python text)")
    conn.commit()
    conn.close()

def insert(date, sleep, exercise, study, code, read):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)", (date, sleep, exercise, study, code, read))
    conn.commit()
    conn.close

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()


def search(date='' , sleep='' , exercise='' , study='' , code='' , read=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR sleep=? OR exercise=? OR study=? OR code=? OR read=?" , (date , sleep , exercise , study , code , read))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
