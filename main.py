import datetime

from aiogram.utils import executor

from create_bot import dp
from handlers import client, admin, other
from data_base.sqlite_db import sql_start


def on_startup():
    print('Бот работает')


client.register_handlers_client()
admin.register_handlers_admin()
# other.register_handlers_other(dp)

sql_start()
executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
