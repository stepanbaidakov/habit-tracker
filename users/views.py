from rest_framework import generics, viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser
# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
