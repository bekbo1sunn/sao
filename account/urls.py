from django.urls import path, include
# from .views import RegisterUserView, activate_view
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import RegisterUserView, activate_view


urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('activate/<str:activation_code>/', activate_view),
]
