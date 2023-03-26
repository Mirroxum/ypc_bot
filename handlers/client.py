'''Клиентская часть'''
from aiogram import types

from keyboards import client_kb
from create_bot import bot, dp
from data import const


@dp.callback_query_handler(text='back_to_menu')
async def process_callback_back_to_menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, const.START_MESSAGE, reply_markup=client_kb.kb_main_menu)


@dp.callback_query_handler(text='help')
async def process_callback_help(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, const.HELP_MESSAGE)


@dp.callback_query_handler(text='location')
async def process_callback_location(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_location(callback_query.from_user.id, latitude=const.LATITUDE_LOCATION, longitude=const.LONGITUDE_LOCATION)
    await bot.send_message(callback_query.from_user.id, const.LOCATION, reply_markup=client_kb.kb_back_to_menu)


@dp.callback_query_handler(text='enter')
async def process_callback_enter(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_location(callback_query.from_user.id, latitude=const.LATITUDE_LOCATION, longitude=const.LONGITUDE_LOCATION)
    await bot.send_message(callback_query.from_user.id, const.LOCATION, reply_markup=client_kb.kb_back_to_menu)

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
