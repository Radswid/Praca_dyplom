# -*- coding: utf-8 -*-
from django.db import models

class Commands(models.Model):
    
    ip = models.CharField('IP', max_length=50)
    system = models.CharField('System', max_length=50)
    ram = models.IntegerField('Ram')
    quote = models.IntegerField('Quote')
    wykonana = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Komenda'
        verbose_name_plural = 'Komendy'
    def __unicode__(self):
        return self.ip
