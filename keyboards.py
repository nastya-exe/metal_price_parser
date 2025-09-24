from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def choose_metal_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text='Золото', callback_data='choose_gold'),
        InlineKeyboardButton(text='Серебро', callback_data='choose_silver')
    )
    return builder.as_markup()


def choose_graph_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text='Неделя', callback_data='weekly_graph'),
        InlineKeyboardButton(text='Месяц', callback_data='month_graph'),
        InlineKeyboardButton(text='День', callback_data='day_graph')
    )
    return builder.as_markup()


def choose_metal_graph_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text='Золото', callback_data='graph_gold'),
        InlineKeyboardButton(text='Серебро', callback_data='graph_silver')
    )
    return builder.as_markup()
