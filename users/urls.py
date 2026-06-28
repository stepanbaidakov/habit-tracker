# from .views import RegisterAPIView, UserUpdateAPIView, UserListAPIView, UserDestroyAPIView, UserRetrieveAPIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'users'
router = DefaultRouter()
router.register('profile', UserViewSet, basename='profile')

urlpatterns = [
    # path("profiles/<int:pk>/update/", UserUpdateAPIView.as_view(), name="profile-update"),
    #                path("profiles/<int:pk>/", UserRetrieveAPIView.as_view(), name="profile"),
    #                path("profiles/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="profile-delete"),
    #                path("profiles/", UserListAPIView.as_view(), name="profile-list"),
    #                path("register/", RegisterAPIView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), ] + router.urls
