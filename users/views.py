from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User

# Create your views here.

class RegisterView(CreateView):

    model = User
    form = UserRegisterForm
    success_url = reverse_lazy('users/register.html')
