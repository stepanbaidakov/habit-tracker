from habits.views import HabitViewSet
from rest_framework.routers import DefaultRouter

app_name = 'habits'
router = DefaultRouter()


router.register("habit", HabitViewSet, "habit")

urlpatterns = [] + router.urls