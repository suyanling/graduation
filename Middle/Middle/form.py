# -*- coding: utf-8 -*-
from django import forms

# 测试使用Form类库


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(max_length=100)
