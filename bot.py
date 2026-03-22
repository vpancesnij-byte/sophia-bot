import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from openai import AsyncOpenAI

TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TOKEN)
dp = Dispatcher()
client = AsyncOpenAI(api_key=OPENAI_API_KEY)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привіт! Я твій ШІ-бот. Напиши мені!")

@dp.message()
async def chat_handler(message: types.Message):
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=
        )
        await message.answer(response.choices.message.content)
    except Exception as e:
        await message.answer(f"Помилка: {e}")

async def main():
    print("Бот запускається...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
