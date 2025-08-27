from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Главное меню
menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Старт")]
    ],
    resize_keyboard=True
)


# Меню выбора породы
class ChoiceMenu:
    def __init__(self, **list_variant):
        self.list_variant = list_variant

    def create(self):
        keyboard = InlineKeyboardBuilder()
        for key, value in self.list_variant.items():
            keyboard.add(
                InlineKeyboardButton(text=str(value), callback_data=str(key))
            )
        return keyboard.adjust(2).as_markup()


# Меню с результатом (правильный/неправильный выбор)
class ChoiceMenuWithAnswer:
    def __init__(self, keyboard, true_answer):
        self.true_answer = true_answer
        self.keyboard = keyboard

    def create(self, chosen_answer):
        new_keyboard = []
        for row in self.keyboard:
            new_row = []
            for button in row:
                if button.callback_data == self.true_answer:
                    # правильный вариант ✅
                    new_row.append(
                        InlineKeyboardButton(text=f"{button.text} ✅", callback_data=button.callback_data)
                    )
                elif button.callback_data == chosen_answer:
                    # выбранный, но неправильный ❌
                    new_row.append(
                        InlineKeyboardButton(text=f"{button.text} ❌", callback_data=button.callback_data)
                    )
                else:
                    # остальные просто текст
                    new_row.append(
                        InlineKeyboardButton(text=button.text, callback_data=button.callback_data)
                    )
            new_keyboard.append(new_row)
        return {"inline_keyboard": new_keyboard}