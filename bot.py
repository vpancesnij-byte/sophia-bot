import os, asyncio
from aiogram import Bot, Dispatcher, types
from openai import AsyncOpenAI

TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TOKEN)
dp = Dispatcher()
client = AsyncOpenAI(api_key=OPENAI_KEY)

@dp.message()
async def chat_handler(message: types.Message):
    try:
        response = await client.chat.completions.create(model="gpt-3.5-turbo", messages=)
        await message.answer(response.choices.message.content)
    except Exception as e:
        await message.answer(f"Помилка: {e}")

async def main():
    print("Бот працює!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
