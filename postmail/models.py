from django.db import models
from django.utils import timezone


class Client(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='отчество')
    email = models.EmailField(unique=True, verbose_name='почта')
    comment = models.CharField(max_length=100, verbose_name='комментарий')

    class Meta:

        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):

        return f'{self.first_name}, {self.last_name}, {self.email}, {self.comment}'


class Message(models.Model):

    title = models.CharField(max_length=50, verbose_name='тема письма')
    body = models.CharField(max_length=100, verbose_name='тело письма')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return f'{self.title}, {self.body}'


class Mail(models.Model):

    name = models.CharField(verbose_name="название рассылки", max_length=50)
    client = models.ManyToManyField(Client, verbose_name="получатель")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="сообщение", blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now, verbose_name="начало")
    next_date = models.DateTimeField(default=timezone.now, verbose_name="следующее")
    end_date = models.DateTimeField(default=timezone.now, verbose_name="конец")
    interval = models.CharField(default="разовая", max_length=50, verbose_name="интервал")
    status = models.CharField(max_length=50, verbose_name="статус")
    is_active = models.BooleanField(default=True, verbose_name="действующая")

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def __str__(self):

        return self.name


class Logs(models.Model):

    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='рассылка', blank=True, null=True)
    last_mail_time = models.DateTimeField(auto_now=True, verbose_name='время последней рассылки')
    status = models.CharField(max_length=50, verbose_name='статус попытки')
    response = models.CharField(max_length=200, verbose_name="ответ почтового сервера", blank=True, null=True)

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'

    def __str__(self):

        return f'''Отправлено: {self.last_mail_time},
               f'Статус: {self.status}'''
