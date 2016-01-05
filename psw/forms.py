# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets
from psw.models import Commands


class CommandForm(forms.ModelForm):
    IP_CHOICES = (('192.168.0.10','192.168.0.10'),('192.168.0.11','192.168.0.11'))
    SYSTEM_CHOICES = (('Ubuntu','Ubuntu'),('Debian','Debian'))
    RAM_CHOICES = (('64','64'),('128','128'),('256','256'))
    QUOTE_CHOICES = (('5','5'),('10','10'),('15','15'))
    ip = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=IP_CHOICES)
    system = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=SYSTEM_CHOICES)
    ram = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=RAM_CHOICES)
    quote = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=QUOTE_CHOICES)

    class Meta:
        model = Commands
        fields = ('ip','system','ram','quote')
