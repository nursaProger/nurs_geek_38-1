from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"

    )
    markup.add(questionnaire_button)
    return markup


async def check_ban_keyboard():
    markup = InlineKeyboardMarkup()
    check_ban_button = InlineKeyboardButton(
        "Check ban status",
        callback_data="check_ban"
    )

    markup.add(check_ban_button)
    return markup


