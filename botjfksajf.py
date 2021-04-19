import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def first_or_help_commands(message: types.Message):
    await message.reply("Напиши мне что-нибудь!")

@dp.message_handler(commands=['ekaterina'])
async def ekaterina_command(message: types.Message):
    await message.reply("Привет! А что ей передать?")

# если не указано, что обрабатывать точно, то по умолчанию обрабатывется текст
@dp.message_handler()
async def echo_message(msg: types.Message):
    print(msg.from_user.id)
    await bot.send_message(msg.from_user.id, f'You wrote, {msg.text}')


if __name__ == '__main__':
    executor.start_polling(dp)
