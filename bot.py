from telegram.ext import Application, CommandHandler
from datetime import datetime, timedelta

TOKEN = "8994829804:AAEaJue1IdXPqm7QzzPilVUh7nwRWxwqSEA"
GROUP_ID = -1001234567890

last_izin = {}
COOLDOWN = 30

async def izin(update, context):
    user = update.effective_user
    now = datetime.now()

    if user.id in last_izin:
        next_time = last_izin[user.id] + timedelta(minutes=COOLDOWN)
        if now < next_time:
            await update.message.reply_text("masih cooldown ya")
            return

    last_izin[user.id] = now

    # reply ke user
    await update.message.reply_text("izin diterima 👍")

    # kirim log ke grup
    await context.bot.send_message(
        chat_id=GROUP_ID,
        text=f"{user.first_name} izin jam {now.strftime('%H:%M')}"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("izin", izin))

app.run_polling()
