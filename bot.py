from telegram.ext import Application, CommandHandler
import os

TOKEN = os.getenv("8852023772:AAGUb_rZXsMxKIYqAvtOoH_5awpn6pk_D0g")

if not TOKEN:
    print("TOKEN kosong")
    exit()

async def start(update, context):
    await update.message.reply_text("bot hidup ✔️")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("bot jalan...")

app.run_polling(drop_pending_updates=True)
