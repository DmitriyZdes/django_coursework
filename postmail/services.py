from django.utils import timezone
import smtplib
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from datetime import datetime, timedelta
from postmail.models import Mail, Logs


def send_mail(obj: Mail):
    for obj_email in obj.client.all():
        try:
            email = EmailMultiAlternatives(
                subject=obj.message.title,
                body=obj.message.body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[obj_email.client],
            )
            now = datetime.now()
            now = timezone.make_aware(now, timezone.get_current_timezone())

            email.send()
            Logs.objects.create(
                send_name=obj.message.title,
                last_try=now,
                status_try='Успешно',
                logs_owner=obj.logs_owner,
                send_email=obj_email.email
            )
        except smtplib.SMTPException as exc:
            Logs.objects.create(
                send_name=obj.message.title,
                last_try=now,
                status_try='Ошибка',
                logs_owner=obj.logs_owner,
                server_answer=exc,
                send_email=obj_email.email
            )


def set_period():
    now = datetime.now()
    now = timezone.make_aware(now, timezone.get_current_timezone())
    next_try = now + timedelta(minutes=1)
    return next_try


def job():
    now = datetime.now()
    now = timezone.make_aware(now, timezone.get_current_timezone())
    mailing_list = Mail.objects.all()
    for obj in mailing_list:
        if obj.is_active:
            if now - timedelta(minutes=1) < obj.next_try < now + timedelta(minutes=1):
                if obj.status == 'Создана':
                    if obj.start_date <= now:
                        obj.start_date = now
                        obj.status = 'Активна'
                        obj.save()
                if obj.status == 'Активна':
                    if obj.end_date <= now:
                        obj.status = 'Завершена'
                        obj.save()
                    elif obj.start_date <= now:
                        send_mail(obj)
                        if obj.interval == 'Ежедневно':
                            obj.next_date += timedelta(days=1)
                            obj.save()
                        elif obj.interval == 'Еженедельно':
                            obj.next_date += timedelta(days=7)
                            obj.save()
                        elif obj.interval == 'Ежемесячно':
                            obj.next_date += timedelta(days=30)
                            obj.save()
