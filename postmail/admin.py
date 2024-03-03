from django.contrib import admin

from postmail.models import Client, Logs, Mail, Message


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('mail', 'last_mail_time', 'status', 'response',)


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'message', 'start_date', 'nest-date', 'end_date', 'status',)
    list_filter = ('is_active', 'status',)
    search_fields = ('name', 'client', 'start_date', 'end_date',)


@admin.register(Client)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'email',)
    search_fields = ('first_name', 'last_name', )
    list_filter = ('email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
