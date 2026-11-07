from django.utils import timezone

from celery import shared_task

from .models import Habit
from .services import send_message


@shared_task
def check_habits():
    now = timezone.localtime()
    today = now.date()
    current_time = now.time().replace(second=0, microsecond=0)

    habits = Habit.objects.filter(time=current_time)

    for habit in habits:
        if habit.last_sent is None:
            should_send = True
        else:
            days = (today - habit.last_sent.date()).days
            should_send = days >= habit.period

        if should_send:
            text = f"A reminder for your good habit: I will {habit.action} at {habit.time} in {habit.location}."
            send_message(habit.user.chat_id, text)
            habit.last_sent = today
            habit.save()
