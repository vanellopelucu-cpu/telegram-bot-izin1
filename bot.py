from telegram.ext import Application, CommandHandler
import os

TOKEN = os.getenv("8994829804:AAEaJue1IdXPqm7QzzPilVUh7nwRWxwqSEA")
print("TOKEN ADA:", bool(TOKEN))

async def start(update, context):
    await update.message.reply_text("bot hidup ✔️")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("BOT STARTING...")
app.run_polling()
