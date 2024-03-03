from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from postmail.forms import MessageForm
from postmail.models import Client, Mail, Message, Logs

# Create your views here.

class MessageListView(ListView):

    model = Message
    extra_context = {
        "title": 'Заголовок',
        'message_list': Message.objects.all()
    }
    form_class = MessageForm


class MessageDetailView(DetailView):

    model = Message
    form_class = MessageForm

    #def get_queryset(self, *args, **kwargs):
        #queryset = super().get_queryset()
        #queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        #return queryset

