from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserProfileView, CustomPasswordResetView, VerifyEmailView

app_name = UsersConfig.name

urlpatterns = [

    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/genpassword/', CustomPasswordResetView.as_view(), name='generate_new_password'),
    path('verify_email/<int:pk>/', VerifyEmailView.as_view(), name='verification'),

    ]
