from django.urls import path
from postmail.apps import PostmailConfig

app_name = PostmailConfig.name
from postmail.views import MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    MailListView, MailCreateView, MailUpdateView, MailDeleteView, LogsListView, ClientListView, ClientCreateView, \
    ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_list', MessageListView.as_view(), name='message_list'),
    path('create_message', MessageCreateView.as_view(), name='create_message'),
    path('update_message', MessageUpdateView.as_view(), name='update_message'),
    path('delete_message', MessageDeleteView.as_view(), name='delete_message'),

    path('mail_list', MailListView.as_view(), name='mail_list'),
    path('create_mail', MailCreateView.as_view(), name='create_mail'),
    path('update_mail', MailUpdateView.as_view(), name='update_mail'),
    path('delete_mail', MailDeleteView.as_view(), name='delete_mail'),

    path('logs_list', LogsListView.as_view(), name='logs_list'),

    path('client_list', ClientListView.as_view(), name='client_list'),
    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('update_client', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client', ClientDeleteView.as_view(), name='delete_client'),

]
