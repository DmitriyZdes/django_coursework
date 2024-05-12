from django import forms

from postmail.models import Client, Message, Mail, Logs


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = ("title", "body",)


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class LogsForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Logs
        fields = ('mail', 'status',)


class MailForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'
