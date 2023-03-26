from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot, dp
from keyboards import admin_kb
from data_base import sqlite_db as db

id_admin = None


class EventAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    structure = State()
    datetime = State()


@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global id_admin
    id_admin = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин надо?', reply_markup=admin_kb.kb_admin_menu)
    await message.delete()


@dp.callback_query_handler(text='show_all_event')
async def process_callback_tournament_admin(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.from_user.id == id_admin:
        tournaments = db.sql_read_tournament(show_next=False)
        for tournament in tournaments:
            await bot.send_message(callback_query.from_user.id, f'Турнир:{tournament[2]}.\n\nНачало туринра:{tournament[5]}\n\n Описание турнира:{tournament[3]}', reply_markup=admin_kb.kb_tournament)


@dp.callback_query_handler(text='create_event')
async def process_callback_tournament_admin(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.from_user.id == id_admin:
        await EventAdmin.photo.set()
        await bot.send_message(callback_query.from_user.id, 'Загрузи фото к событию', reply_markup=admin_kb.kb_back_admin)


@dp.message_handler(state=EventAdmin.photo, content_types=['photo'])
async def load_image(message: types.Message, state: FSMContext):
    if message.from_user.id == id_admin:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await EventAdmin.next()
        await message.reply('Теперь введите название', reply_markup=admin_kb.kb_back_admin)


@dp.message_handler(state=EventAdmin.name)
async def set_name(message: types.Message, state: FSMContext):
    if message.from_user.id == id_admin:
        async with state.proxy() as data:
            data['name'] = message.text
        await EventAdmin.next()
        await message.reply('Теперь введите описание', reply_markup=admin_kb.kb_back_admin)


@dp.message_handler(state=EventAdmin.description)
async def set_description(message: types.Message, state: FSMContext):
    if message.from_user.id == id_admin:
        async with state.proxy() as data:
            data['description'] = message.text
        await EventAdmin.next()
        await message.reply('Теперь введите струтктуру турнира', reply_markup=admin_kb.kb_back_admin)


@dp.message_handler(state=EventAdmin.structure)
async def set_structure(message: types.Message, state: FSMContext):
    if message.from_user.id == id_admin:
        async with state.proxy() as data:
            data['structure'] = message.text
        await EventAdmin.next()
        await message.reply('Теперь введите дату и время меропирятия. Формат: день.месяц.год часы.минуты', reply_markup=admin_kb.kb_back_admin)


@dp.message_handler(state=EventAdmin.datetime)
async def set_datetime(message: types.Message, state: FSMContext):
    if message.from_user.id == id_admin:
        async with state.proxy() as data:
            datetime_tournament = datetime.strptime(
                message.text, '%d.%m.%Y %H.%M')
            data['datetime'] = datetime_tournament
        async with state.proxy() as data:
            await db.sql_add_tournament(data)
            await message.reply('Событие успешно создано!', reply_markup=admin_kb.kb_admin_menu)
        await state.finish()


@dp.callback_query_handler(text='back_to_admin_menu', state='*')
async def cancel_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.from_user.id == id_admin:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await bot.send_message(callback_query.from_user.id, 'Действие отменено', reply_markup=admin_kb.kb_admin_menu)


def register_handlers_admin(dp=dp):
    return dp
