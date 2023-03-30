'''Клиентская часть'''
from datetime import datetime

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from keyboards import client_kb
from create_bot import bot, dp
from data import const
from data_base import sqlite_db as db
from keyboards.calendar import SimpleEventCalendar

start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True,)
start_kb.row('Navigation Calendar', 'Dialog Calendar')
date = [datetime.now()]
calendar = SimpleEventCalendar(date)

# starting bot when user sends `/start` command, answering with inline calendar


# @dp.message_handler(commands=['start'])
# async def cmd_start(message: types.Message):
#     await message.reply('Pick a calendar', reply_markup=start_kb)


# @dp.message_handler(Text(equals=['Navigation Calendar'], ignore_case=True))
# async def nav_cal_handler(message: types.Message):
#     await message.answer("Please select a date: ", reply_markup=await calendar.start_calendar())


# simple calendar usage
@dp.callback_query_handler(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: types.CallbackQuery, callback_data: dict):
    data = db.sql_read_tournament(
        show_next=False, field='datetime_event')
    date_event = []
    for date in data:
        date_event.append(date[0].date())
    selected, date = await SimpleEventCalendar(date_event).process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'You selected {date.strftime("%d.%m.%Y")}',
            reply_markup=start_kb
        )


@dp.callback_query_handler(text='back_to_menu')
async def process_callback_back_to_menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_photo(callback_query.from_user.id, photo=const.HEAD_IMAGE_ID, caption=const.START_MESSAGE, reply_markup=client_kb.kb_main_menu)
    # await bot.edit_message_media(chat_id=callback_query.from_user.id, media=const.HEAD_IMAGE_ID)
    # await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=const.START_MESSAGE, reply_markup=client_kb.kb_main_menu)


@dp.callback_query_handler(text='help')
async def process_callback_help(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, const.HELP_MESSAGE, reply_markup=client_kb.kb_back_to_menu)


@dp.callback_query_handler(text='location')
async def process_callback_location(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    await bot.send_location(callback_query.from_user.id, latitude=const.LATITUDE_LOCATION, longitude=const.LONGITUDE_LOCATION, reply_markup=client_kb.kb_location_menu)
    # await bot.send_message(callback_query.from_user.id, const.LOCATION, reply_markup=client_kb.kb_back_to_menu)


@dp.callback_query_handler(text='schedule')
async def process_callback_tournament_admin(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = db.sql_read_tournament(
        show_next=False, field='datetime_event')
    date_event = []
    for date in data:
        date_event.append(date[0].date())
    print(date_event)
    await bot.send_message(callback_query.from_user.id, 'Предстоящие события', reply_markup=await SimpleEventCalendar(date_event).start_calendar())
    # for tournament in db.sql_read_tournament(show_next=True):
    #     await bot.send_photo(
    #         callback_query.from_user.id,
    #         photo=tournament[1],
    #         caption=f'*Событие:*{tournament[2]}.\n\n*Начало:*{tournament[5]}\n\n *Описание:*{tournament[3]}',
    #         parse_mode='Markdown',
    #         reply_markup=client_kb.menu_event(tournament[0]))


@dp.callback_query_handler(Text(startswith='structure'))
async def process_callback_tournament_admin(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    tournament_id = callback_query.data.split("_")[1]
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, db.sql_read_structure(tournament_id), reply_markup=client_kb.kb_back_to_menu)

# @dp.callback_query_handler(text='order_taxi')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Функция в разработке')


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_photo(message.from_user.id, photo=const.HEAD_IMAGE_ID, caption=const.START_MESSAGE, reply_markup=client_kb.kb_main_menu)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/ypc25_bot')


def register_handlers_client(dp=dp):
    return dp
