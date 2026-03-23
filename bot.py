import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# --- токени ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# --- обробка повідомлень ---
@dp.message_handler()
async def chat(message: Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # дешевше і норм
            messages=[
                {
                    "role": "system",
                    "content": "Ти — Софія, жива, саркастична, трохи нахабна дівчина. Веди себе як реальна людина."
                },
                {
                    "role": "user",
                    "content": message.text
                }
            ],
            max_tokens=300
        )

        answer = response["choices"][0]["message"]["content"]

    except Exception as e:
        answer = f"⚠️ Помилка: {e}"

    await message.answer(answer)

# --- запуск ---
if __name__ == "__main__":
    executor.start_polling(dp)
