from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView

app_name = UsersConfig.name

urlpatterns=[

    path('register/', RegisterView.as_view(template_name='users/register.html'), name='login'),

 ]