
from django import forms
from django.forms import ModelForm
from .models import Chat


class MessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":3, "placeholder": "Type message here"}))
    class Meta:
        model = Chat
        fields = ["body","files"]
   


