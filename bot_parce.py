import asyncio

from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BotCommand, CallbackQuery, FSInputFile
from aiogram import Dispatcher, types, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State

from config import bot_token, url_silver, url_gold
from keyboards import choose_metal_keyboard, choose_graph_keyboard, choose_metal_graph_keyboard
from metal_price_parser import scrape_price_metal
from make_graph import make_graph_month, make_graph_week, make_graph_day

dp = Dispatcher(storage=MemoryStorage())


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description="Запустить бота"),
        BotCommand(command="price", description="Текущий курс"),
        BotCommand(command='graph', description='Графики')
    ]
    await bot.set_my_commands(commands)


@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выбери команду')


@dp.message(Command('price'))
async def price_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выбери металл', reply_markup=choose_metal_keyboard())


@dp.callback_query(F.data == 'choose_gold')
async def choose_gold(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    price = scrape_price_metal(url_gold)[1]
    date = scrape_price_metal(url_gold)[0]
    await callback.message.answer(f'На данный момент цена золота:\n{price} рублей\n\n{date}')


@dp.callback_query(F.data == 'choose_silver')
async def choose_gold(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    price = scrape_price_metal(url_silver)[1]
    date = scrape_price_metal(url_silver)[0]
    await callback.message.answer(f'На данный момент цена серебра:\n{price} рублей\n\n{date}')


@dp.message(Command('graph'))
async def graph_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('За какой период необходим график', reply_markup=choose_graph_keyboard())


@dp.callback_query(F.data.in_({'weekly_graph', 'month_graph', 'day_graph'}))
async def graph_period(callback: CallbackQuery, state: FSMContext):
    periods = {
        'weekly_graph': 'week',
        'month_graph': 'month',
        'day_graph': 'day'
    }

    await state.update_data(period=periods[callback.data])
    await callback.message.answer('Выберите металл', reply_markup=choose_metal_graph_keyboard())


@dp.callback_query(F.data.in_({'graph_gold', 'graph_silver'}))
async def graph_metal(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    period = data.get('period')
    if callback.data == 'graph_gold':
        metal = 'gold'
        metal_name = 'золото'
    else:
        metal = 'silver'
        metal_name = 'серебро'

    if period == 'week':
        await callback.message.answer(f'График за неделю: {metal_name}')
        file_path = make_graph_week(metal)
    elif period == 'day':
        await callback.message.answer(f'График за сегодняшний день: {metal_name}')
        file_path = make_graph_day(metal)
    else:
        await callback.message.answer(f'График за месяц: {metal_name}')
        file_path = make_graph_month(metal)

    photo = FSInputFile(file_path)

    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo=photo)


async def main():
    bot = Bot(token=bot_token)
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
