from django import forms

class AddComment(forms.Form):
    name = forms.CharField(max_length=50, label='نام', required=True)
    comment = forms.CharField(required=True, label='نظر')