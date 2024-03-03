from django import forms

from postmail.models import Client, Message, Mail, Logs

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model =Message
        fields = ("title", "body",)
