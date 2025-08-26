from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_main = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=f'Привет'),
                        KeyboardButton(text=f'До свидания')
                    ]
                ],
                resize_keyboard=True)
