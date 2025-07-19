from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7592422208:AAEgrZ09KpWltyJDMyqGutb6dgovii8T-xM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات جدید شما هستم 🤖\nدستور /help رو امتحان کن!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("من می‌تونم پیام‌هات رو دریافت و تکرار کنم!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"شما گفتید: {user_message}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    print("ربات در حال اجرا است...")
    app.run_polling()

if __name__ == '__main__':
    main()
