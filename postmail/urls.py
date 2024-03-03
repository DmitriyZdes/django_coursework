from django.urls import path
from postmail.apps import PostmailConfig

app_name = PostmailConfig.name
from postmail.views import MessageListView, MessageDetailView

urlpatterns = [
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='view'),
    path('message_list', MessageListView.as_view(), name='pr_list'),
]
