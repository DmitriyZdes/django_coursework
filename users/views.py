from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.views import PasswordResetView
from users.forms import UserRegisterForm, UserUpdateForm, VerificationForm
from users.models import User
import random

# Create your views here.


class RegisterView(CreateView):

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject='Подтверждение почты в Сервисе рассылок.',
            message=f'Вы зарегистрировались в Сервисе рассылок. Введите код в форму подтверждения - '
                    f'{user.verification_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:user_profile')

    def get_object(self, queryset=None):
        return self.request.user


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        # Генерация нового случайного пароля
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()

        send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль: {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
        return super().form_valid(form)


class VerifyEmailView(View):

    model = User
    template_name = 'users/verification.html'

    def post(self, request, *args, **kwargs):
        form = VerificationForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['verification_code']
            user_pk = kwargs.get('pk')
            user = get_object_or_404(User, pk=user_pk)
            if entered_code == user.verify_code:
                user.is_active = True
                user.save()
                messages.success(request, 'Аккаунт успешно активирован!')
                return redirect(reverse('users:login'))
            else:
                messages.error(request, 'Неверный код верификации. Попробуйте снова.')

            return render(request, self.template_name, {'form': form})


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.view_user'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['users_list'] = User.objects.all()
        return context_data


class UserDeleteView(UserPassesTestMixin, PermissionRequiredMixin, DeleteView):
    model = User
    permission_required = 'users.delete_user'
    login_url = 'users:login'
    success_url = reverse_lazy('users:user_list')

    def test_func(self):
        return self.request.user.is_staff
