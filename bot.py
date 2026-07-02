import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # замени config на имя своего проекта
django.setup()


from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

load_dotenv()
API_KEY = os.getenv("API_KEY")


async def start(update, context):
    User = get_user_model()
    username = f"@{update.effective_user.username}"
    chat_id = update.effective_chat.id
    user = await sync_to_async(User.objects.get)(username=username)
    user.chat_id = chat_id
    await sync_to_async(user.save)()
    await update.message.reply_text("Вы успешно подписались на уведомления!")


app = Application.builder().token(API_KEY).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
