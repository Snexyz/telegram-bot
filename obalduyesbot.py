import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN не найден в переменных окружения")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот команды Obalduyes.\nДля других команд, пишите /help."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start\n/help\n/info\n/contact"
    )


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Мы команда FLL из Кокшетау!\n\n"
        "Instagram: <a href='https://www.instagram.com/obalduyes_fll_challenge'>клик</a>\n"
        "Сайт: <a href='https://obalduyes.github.io/Obalduyes-Info/#about'>клик</a>\n"
        "TikTok: <a href='https://www.tiktok.com/@obalduyes'>клик</a>\n"
        "FLL результаты: <a href='https://obalduyes.github.io/FLL-Teams/'>клик</a>\n"
        "Telegram: <a href='https://t.me/obalduyes'>клик</a>"
    )

    await update.message.reply_text(text, parse_mode="HTML")


async def contact_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Напиши @antarsag для связи."
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("contact", contact_us))

print("Бот запущен...")
app.run_polling()
