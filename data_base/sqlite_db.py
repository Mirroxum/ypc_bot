import sqlite3 as sq
from datetime import datetime


def sql_start():
    global base, cur
    base = sq.connect('ypc.db',
                      detect_types=sq.PARSE_DECLTYPES | sq.PARSE_COLNAMES
                      )
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS tournament('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'img TEXT,'
        'name TEXT,'
        'description TEXT,'
        'structure TEXT,'
        'datetime_event timestamp)'
    )
    base.execute(
        'CREATE TABLE IF NOT EXISTS result('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'user TEXT,'
        'point INTEGER,'
        'tournament_id INTEGER)'
    )
    base.execute(
        'CREATE TABLE IF NOT EXISTS img_tournament('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'img TEXT,'
        'tournament_id INTEGER)'
    )
    base.execute(
        'CREATE TABLE IF NOT EXISTS users('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'phone TEXT,'
        'telegram_id TEXT,'
        'name TEXT)'
    )
    base.commit()


async def sql_add_tournament(data):
    cur.execute('INSERT INTO tournament (img, name, description, structure, datetime_event) VALUES (?, ?, ?, ?, ?);',
                tuple(data.values()))
    base.commit()


def sql_read_tournament(show_next=True):
    if show_next:
        today = datetime.now().today()
        print(today)
        next = f' WHERE datetime_event >= "{today}"'
    else:
        next = ''
    return cur.execute(f'SELECT * FROM tournament{next};').fetchall()


# def test_sql():
#     query = cur.execute(
#         'SELECT * FROM tournament WHERE datetime_event > "2023-07-26";').fetchall()
#     print(query)


# sql_start()
# test_sql()
