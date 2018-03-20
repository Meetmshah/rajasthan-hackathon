import sqlite3
import io
import numpy as np

dbname = 'db/fencoding'
table_name = 'fencoding'


def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

def init():
    global conn
    global c

    # Converts np.array to TEXT when inserting
    sqlite3.register_adapter(np.ndarray, adapt_array)
    # Converts TEXT to np.array when selecting
    sqlite3.register_converter("array", convert_array)

    conn = sqlite3.connect(dbname, detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()

def create_table():
    sql = '''create table if not exists {}(
    ID integer primary key AUTOINCREMENT,
    NAME TEXT,
    FENCODING array,
    ACCESS_LVL integer)'''.format(table_name)
    c.execute(sql)

def clear_table():
    sql = 'drop table ' + table_name
    c.execute(sql)

def remake_table():
    clear_table()
    create_table()

def insert_record(name, fencoding, alvl):
    sql = '''insert into {} (NAME, FENCODING, ACCESS_LVL)
    values (?, ?, ?)'''.format(table_name)
    c.execute(sql, (name, fencoding, alvl))

def get_encodings():
    sql = '''select NAME, FENCODING from {}'''.format(table_name)
    c.execute(sql)
    data = c.fetchall()
    return data


def fcommit():
    conn.commit()
    c.close()
    conn.close()
