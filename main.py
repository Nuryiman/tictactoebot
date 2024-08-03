import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from config import API_TOKEN
from datebase import Database
from keyboards import fields_kb, request_kb, cancel_kb

bot = Bot(API_TOKEN)
dp = Dispatcher()
db = Database(db_file="users.sqlite")
challenges = {}
senders = {}


class GamePlay(StatesGroup):
    move = State()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет {message.from_user.first_name}")
    db.add_user(user_id=int(message.chat.id), user_name=f"@{message.from_user.username}")
    print(db.get_all_records())


@dp.message(Command("play"))
async def play(message: Message, command: CommandObject):
    # print(db.get_user(user_name=command.args))
    await bot.send_message(int(db.get_user(user_name=command.args)[0]), f"Вам скинул вызов {message.from_user.username}", reply_markup=request_kb)
    challenges[message.chat.id] = int(db.get_user(user_name=command.args)[0])
    senders[int(db.get_user(user_name=command.args)[0])] = message.chat.id
    print(senders)
    print(challenges)
    await message.answer(f"Вызов к {command.args} отправлен", reply_markup=cancel_kb)


@dp.callback_query(F.data == "vyzov")
async def vyzov(callback_query: CallbackQuery):
    if callback_query.from_user.id in senders:
        await callback_query.message.edit_reply_markup(reply_markup=fields_kb)
        await bot.send_message(senders[callback_query.from_user.id], f"{db.get_user(user_id=callback_query.from_user.id)[1]} принял ваш вызов", reply_markup=fields_kb)
    else:
        await callback_query.message.delete()
    print(senders)
    print(challenges)


@dp.callback_query(F.data == "cancel")
async def cancel(callback_query: CallbackQuery):
    await callback_query.message.delete_reply_markup()
    await callback_query.message.edit_text("Вызов отменен")
    senders.pop(challenges[callback_query.from_user.id])
    challenges.pop(callback_query.from_user.id)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
