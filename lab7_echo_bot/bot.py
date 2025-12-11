from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Завантаження токена з .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(text)

async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Обробник всіх текстових повідомлень
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот запущено!")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
