from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from postmail.forms import MessageForm, MailForm, ClientForm, LogsForm
from postmail.models import Client, Mail, Message, Logs

# Create your views here.

class MessageListView(LoginRequiredMixin, ListView):

    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):

    model = Message

class MessageCreateView(LoginRequiredMixin, CreateView):

    model = Message
    form_class = MessageForm
    extra_context = {
        "title": 'Заголовок',
        'message_list': Message.objects.all()
    }
    success_url = reverse_lazy('postmail:message_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('postmail:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):

    model = Message
    success_url = reverse_lazy('postmail:message_list')

class MailCreateView(LoginRequiredMixin, CreateView):

    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('postmail:mail_list')

    def get_queryset(self, *args, **kwargs):

        return super().get_queryset(self, *args, **kwargs)
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

class MailUpdateView(UpdateView):

    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('postmail:mail_list')

class MailListView(LoginRequiredMixin, ListView):

    model = Mail

class MailDeleteView(DeleteView):

    model = Mail
    success_url = reverse_lazy('postmail:mail_list')


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(logs_owner=self.request.user)
        return queryset

class ClientCreateView(LoginRequiredMixin, CreateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('postmail:client_list')

    def form_valid(self, form):
        send_params = form.save()
        send_params.client_owner = self.request.user
        send_params.save()
        return super().form_valid(form)

class ClientListView(LoginRequiredMixin, ListView):

    model = Client

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(client_owner=self.request.user)
        return queryset

class ClientUpdateView(LoginRequiredMixin, UpdateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('postmail:client_list')

class ClientDeleteView(LoginRequiredMixin, DeleteView):

    model = Client
    success_url = reverse_lazy('postmail:client_list')
