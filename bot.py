import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

from asgiref.sync import sync_to_async
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

load_dotenv()
API_KEY = os.getenv("API_KEY")


@sync_to_async
def get_user(telegram_username):
    User = get_user_model()

    return User.objects.filter(telegram_username=telegram_username).first()


@sync_to_async
def save_user_chat(user, chat_id):
    user.chat_id = chat_id
    user.save()


async def start(update, context):
    telegram_username = f"@{update.effective_user.username}"
    chat_id = update.effective_chat.id

    user = await get_user(telegram_username)
    await save_user_chat(user, chat_id)

    await update.message.reply_text("Вы успешно подписались на уведомления!")


def main():
    app = Application.builder().token(API_KEY).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
