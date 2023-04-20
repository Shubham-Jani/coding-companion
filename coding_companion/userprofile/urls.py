from django.urls import path
from .views import UserRetrieveAPIView, UserCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('current/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('create/', UserCreateAPIView.as_view(), name="user_create"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
