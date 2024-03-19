from django.contrib import admin

from postmail.models import Client, Logs, Mail, Message


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('mail', 'last_mail_time', 'status', 'response',)


admin.site.register(Mail)


@admin.register(Client)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'email',)
    search_fields = ('first_name', 'last_name', )
    list_filter = ('email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
