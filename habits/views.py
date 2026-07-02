from habits.models import Habit
from rest_framework import viewsets
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from .paginators import MyPageNumberPaginator
from .permissions import IsOwner
from django.db.models import Q

# Create your views here.

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = MyPageNumberPaginator

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Habit.objects.filter(Q(user=self.request.user) | Q(is_public=True))
        return Habit.objects.filter(is_public=True)

    def get_permissions(self):
        if self.action == "retrieve":
            self.permission_classes = [IsOwner]
        elif self.action == "update":
            self.permission_classes = [IsOwner]
        elif self.action == "partial_update":
            self.permission_classes = [IsOwner]
        elif self.action == "destroy":
            self.permission_classes = [IsOwner]
        elif self.action == "create":
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]
