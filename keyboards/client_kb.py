from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

help = InlineKeyboardButton('💡Что может бот💡', callback_data='help')
location = InlineKeyboardButton(
    '📍Расположение клуба📍', callback_data='location')
schedule = InlineKeyboardButton(
    '♠️ Предстоящие события клуба ♠️', callback_data='schedule')
raiting = InlineKeyboardButton('🏆Рейтинг клуба🏆', callback_data='raiting')
enter = InlineKeyboardButton('♦️Вступить в клуб♦️', callback_data='enter')
back_main_menu = InlineKeyboardButton('Назад', callback_data='back_to_menu')
order_taxi = InlineKeyboardButton(
    '🚕Заказать Яндекс-такси🚕', request_location=True, callback_data='order_taxi')
structure = InlineKeyboardButton(
    'Структура', callback_data='structure')

# Основное меню
kb_main_menu = InlineKeyboardMarkup()
kb_main_menu.row(help).row(location).row(schedule).row(raiting).row(enter)

# Меню локации - не используется
kb_location_menu = InlineKeyboardMarkup()
kb_location_menu.row(order_taxi).row(back_main_menu)

# Меню возврата к основному меню
kb_back_to_menu = InlineKeyboardMarkup()
kb_back_to_menu.add(back_main_menu)

# Меню турнира
kb_tournament = InlineKeyboardMarkup()
kb_tournament.row(structure)
