from django import forms

class NotificationForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"id": "msg"}))