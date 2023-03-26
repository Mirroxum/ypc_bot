import sqlite3 as sq
from create_bot import dp, bot


def sql_start():
    global base, cur
    base = sq.connect('ypc.db',
                      detect_types=sq.PARSE_DECLTYPES | sq.PARSE_COLNAMES)
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


def sql_read_tournament():
    return cur.execute('SELECT * FROM tournament').fetchall()
