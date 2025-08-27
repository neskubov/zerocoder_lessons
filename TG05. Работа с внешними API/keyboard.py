from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_start = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=f'Старт')
                    ]
                ],
                resize_keyboard=True)

class ChoiceMenu:
    def __init__(self, **list_variant):  # исправлено на __init__
        self.list_variant = list_variant

    def create(self):
        keyboard = InlineKeyboardBuilder()
        for key, value in self.list_variant.items():
            keyboard.add(
                InlineKeyboardButton(text=str(value), callback_data=str(key))  # гарантируем строки
            )
        return keyboard.adjust(2).as_markup()

