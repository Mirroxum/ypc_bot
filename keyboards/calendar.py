import calendar
from datetime import datetime, timedelta, date

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram_calendar import SimpleCalendar

# setting callback_data prefix and parts
calendar_callback = CallbackData(
    'simple_calendar', 'act', 'year', 'month', 'day')


class SimpleEventCalendar(SimpleCalendar):
    def __init__(self, date_event) -> None:
        self.date_event = date_event

    async def start_calendar(
        self,
        year: int = datetime.now().year,
        month: int = datetime.now().month
    ) -> InlineKeyboardMarkup:
        """
        Creates an inline keyboard with the provided year and month
        :param int year: Year to use in the calendar, if None the current year is used.
        :param int month: Month to use in the calendar, if None the current month is used.
        :return: Returns InlineKeyboardMarkup object with the calendar.
        """
        inline_kb = InlineKeyboardMarkup(row_width=7)
        ignore_callback = calendar_callback.new(
            "IGNORE", year, month, 0)  # for buttons with no answer
        # First row - Month and Year
        inline_kb.row()
        inline_kb.insert(InlineKeyboardButton(
            "<<",
            callback_data=calendar_callback.new("PREV-YEAR", year, month, 1)
        ))
        inline_kb.insert(InlineKeyboardButton(
            f'{calendar.month_name[month]} {str(year)}',
            callback_data=ignore_callback
        ))
        inline_kb.insert(InlineKeyboardButton(
            ">>",
            callback_data=calendar_callback.new("NEXT-YEAR", year, month, 1)
        ))
        # Second row - Week Days
        inline_kb.row()
        for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]:
            inline_kb.insert(InlineKeyboardButton(
                day, callback_data=ignore_callback))

        # Calendar rows - Days of month
        month_calendar = calendar.monthcalendar(year, month)

        for week in month_calendar:
            inline_kb.row()
            for day in week:
                if (day == 0):
                    inline_kb.insert(InlineKeyboardButton(
                        " ", callback_data=ignore_callback))
                    continue
                current_day = date(year, month, day)
                if current_day in self.date_event:
                    inline_kb.insert(InlineKeyboardButton(
                        f'{day}✅', callback_data=calendar_callback.new("DAY", year, month, day)
                    ))
                else:
                    inline_kb.insert(InlineKeyboardButton(
                        str(day), callback_data=calendar_callback.new("DAY", year, month, day)
                    ))

        # Last row - Buttons
        inline_kb.row()
        inline_kb.insert(InlineKeyboardButton(
            "<", callback_data=calendar_callback.new("PREV-MONTH", year, month, day)
        ))
        inline_kb.insert(InlineKeyboardButton(
            " ", callback_data=ignore_callback))
        inline_kb.insert(InlineKeyboardButton(
            ">", callback_data=calendar_callback.new("NEXT-MONTH", year, month, day)
        ))

        return inline_kb
