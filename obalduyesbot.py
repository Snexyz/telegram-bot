import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("TOKEN")

print(TOKEN)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот команды Obalduyes.\nДля других команд, пишите /help."
    )

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступные команды:\n"
        "----------------------------------------\n"
        "/start\n"
        "----------------------------------------\n"
        "/help\n"
        "----------------------------------------\n"
        "/info\n"
        "----------------------------------------\n"
        "/contact"
    )

# /info (С ТВОИМ СТАРЫМ СТИЛЕМ + КЛИКАБЕЛЬНЫЕ ССЫЛКИ)
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Мы команда FLL с города Кокшетау со школы BIL!\n"
        "--------------------------------------------------------------------------------\n"
        "Наш Instagram: <a href='https://www.instagram.com/obalduyes_fll_challenge'>клик</a>\n"
        "--------------------------------------------------------------------------------\n"
        "Наш сайт: <a href='https://obalduyes.github.io/Obalduyes-Info/#about'>клик</a>\n"
        "--------------------------------------------------------------------------------\n"
        "Наш Тикток: <a href='https://www.tiktok.com/@obalduyes'>клик</a>\n"
        "--------------------------------------------------------------------------------\n"
        "Наш сайт с результатами FLL: <a href='https://obalduyes.github.io/FLL-Teams/'>клик</a>\n"
        "--------------------------------------------------------------------------------\n"
        "Наш телеграмм канал: <a href='https://t.me/obalduyes'>клик</a>"
    )

    await update.message.reply_text(text, parse_mode="HTML")

# /contact
async def contact_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ты можешь написать '@antarsag' чтобы связаться с нами."
    )

# запуск
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("contact", contact_us))

print("Бот работает...")
app.run_polling()
