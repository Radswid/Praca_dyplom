# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from psw.forms import CommandForm
import paramiko

def index(request):
    context = {'boldmessage': "I am bold font from the context"}
    return render(request, 'psw/index.html', context)

def servers(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            
            form.save()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('192.168.0.110', username='root', password='TrudneHaslo123')
            stdin, stdout, stderr = ssh.exec_command('/bin/bash /root/skrypt.sh')
            ssh.close()            
            return HttpResponseRedirect('/psw')
    else:
         form = CommandForm()
         
           
            
           
    return render(request, 'psw/servers.html', {'form': form})
