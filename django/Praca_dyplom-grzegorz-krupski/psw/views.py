# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from psw.forms import CommandForm, ClientForm
from psw.models import Commands
from django.shortcuts import render_to_response
from django.template import RequestContext
import paramiko

def index(request):
    context = {'boldmessage': "I am bold font from the context"}
    return render(request, 'psw/index.html', context)

def servers(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            
            form.save()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('89.206.7.46', username='root', password='TrudneHaslo123')
                stdin, stdout, stderr = ssh.exec_command('/bin/bash /root/skrypt.sh')
                ssh.close()
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                print ('Error %s' %e)
                return HttpResponseRedirect('/psw/servers/')
                      
            return HttpResponseRedirect('/psw')
    else:
         form = CommandForm()
         
           
            
           
    return render(request, 'psw/servers.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/psw')
    else:
         form = ClientForm()
    return render(request, 'psw/register.html', {'form': form})

def listservers(request):
    servers = Commands.objects.all
    context_dict = {'servers': servers}
    return render(request, 'psw/listservers.html' , context_dict)