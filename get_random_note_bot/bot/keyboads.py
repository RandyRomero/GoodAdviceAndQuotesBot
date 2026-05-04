from enum import StrEnum

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ButtonsText(StrEnum):
    GET_A_RANDOM_NOTE = "Get a random note"
    BE_RELENTLESS_NOTE = 'Get a "Be relentless" note'


GET_A_RANDOM_NOTE_BUTTON = KeyboardButton(text=ButtonsText.GET_A_RANDOM_NOTE)
GET_BE_RELENTLESS_BUTTON = KeyboardButton(text=ButtonsText.BE_RELENTLESS_NOTE)
DEFAULT_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[[GET_A_RANDOM_NOTE_BUTTON, GET_BE_RELENTLESS_BUTTON]],
)
