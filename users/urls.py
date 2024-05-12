from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from users.apps import UsersConfig
from users.views import (RegisterView, UserProfileView, CustomPasswordResetView, VerifyEmailView, UserListView,
                         UserDeleteView)


app_name = UsersConfig.name

urlpatterns = [

    path('login/', LoginView.as_view(template_name='users/login_enter.html'), name='login'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('profile/genpassword/', CustomPasswordResetView.as_view(), name='generate_new_password'),
    path('verify_email/<int:pk>/', VerifyEmailView.as_view(), name='verification'),
    path('user_list/',  UserListView.as_view(), name='user_list'),
    path('delete_user/<int:pk>/',  UserDeleteView.as_view(), name='delete_user'),
    path('logout/', LogoutView.as_view(), name='logout')

    ]
