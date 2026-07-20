from rest_framework.routers import DefaultRouter

from habits.views import HabitViewSet

app_name = "habits"
router = DefaultRouter()


router.register("habit", HabitViewSet, "habit")

urlpatterns = [] + router.urls
