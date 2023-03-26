from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

help_admin = InlineKeyboardButton(
    '💡Что можно сделать в админке?💡', callback_data='help_admin')
create_event = InlineKeyboardButton(
    'Создать событие', callback_data='create_event')
show_all_event = InlineKeyboardButton(
    'Показать все события', callback_data='show_all_event')
add_result = InlineKeyboardButton(
    'Добавить результат события', callback_data='add_result_event')
show_all_user = InlineKeyboardButton(
    'Показать всех членов клуба', callback_data='show_all_user')
add_user = InlineKeyboardButton(
    'Добавить нового члена клуба', callback_data='add_user')
back_admin_menu = InlineKeyboardButton(
    'Назад', callback_data='back_to_admin_menu')
add_result = InlineKeyboardButton(
    'Изменить результат события', callback_data='update_result_tournament')


# Основное меню
kb_admin_menu = InlineKeyboardMarkup()
kb_admin_menu.row(help_admin).row(show_all_event, create_event).row(
    add_result).row(show_all_user, add_user)

# Назад меню
kb_back_admin = InlineKeyboardMarkup()
kb_back_admin.row(back_admin_menu)

# Меню для турниров
kb_tournament = InlineKeyboardMarkup()
kb_tournament.row(add_result)
