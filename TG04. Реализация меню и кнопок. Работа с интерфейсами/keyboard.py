from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_start = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=f'Привет'),
                        KeyboardButton(text=f'До свидания')
                    ]
                ],
                resize_keyboard=True)

menu_multimedia = InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(text='Новости 📰', url='https://news.com'),
                                InlineKeyboardButton(text='Музыка 🎵', url='https://music.com'),
                                InlineKeyboardButton(text='Видео 🎬', url='https://video.com')
                            ]
                        ])

dynamic_menu = InlineKeyboardMarkup(
                   inline_keyboard=[
                        [
                            InlineKeyboardButton(text=f'Показать больше', callback_data="show_more")
                        ]
                    ])

menu_options = InlineKeyboardMarkup(
                   inline_keyboard=[
                        [
                           InlineKeyboardButton(text="Опция 1", callback_data="option_1"),
                           InlineKeyboardButton(text="Опция 2", callback_data="option_2")
                        ]
                    ])