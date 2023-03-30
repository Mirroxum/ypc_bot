from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data import const

help = InlineKeyboardButton('💡Что может бот💡', callback_data='help')
location = InlineKeyboardButton(
    '📍Расположение клуба📍', callback_data='location')
schedule = InlineKeyboardButton(
    '♠️ Предстоящие события клуба ♠️', callback_data='schedule')
raiting = InlineKeyboardButton('🏆Рейтинг клуба🏆', callback_data='raiting')
enter = InlineKeyboardButton(
    '♦️Вступить в клуб♦️', callback_data='enter', url='https://youtube.com')
back_main_menu = InlineKeyboardButton('Назад', callback_data='back_to_menu')
order_taxi = InlineKeyboardButton(
    '🚕Заказать Яндекс-такси🚕', request_location=True, callback_data='order_taxi')
location_place = InlineKeyboardButton(
    const.LOCATION, callback_data='None')

# Основное меню
kb_main_menu = InlineKeyboardMarkup()
kb_main_menu.row(help).row(location).row(schedule).row(raiting).row(enter)

# Меню локации
kb_location_menu = InlineKeyboardMarkup()
kb_location_menu.row(location_place).row(back_main_menu)

# Меню возврата к основному меню
kb_back_to_menu = InlineKeyboardMarkup()
kb_back_to_menu.add(back_main_menu)


def menu_event(id):
    structure = InlineKeyboardButton(
        'Структура', callback_data=f'structure_{id}')
    kb_event = InlineKeyboardMarkup()
    kb_event.row(structure)
    return kb_event
