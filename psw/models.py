# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.forms import widgets

class Commands(models.Model):
    
    ip = models.CharField('IP', max_length=50)
    system = models.CharField('System', max_length=50)
    ram = models.IntegerField('Ram')
    quote = models.IntegerField('Quote')

    class Meta:
        verbose_name = 'Komenda'
        verbose_name_plural = 'Komendy'
    def __str__(self):
        return self.ip

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    userLogin = models.CharField(max_length=20)
    password = models.CharField(max_length=24)
    class Meta:
        verbose_name = 'Klient'
        verbose_name_plural = 'Klienci'
    def __str__(self):
        return self.first_name + " " + self.last_name