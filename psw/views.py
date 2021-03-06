# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from psw.forms import CommandForm, ClientForm
import paramiko
from subprocess import call
from psw.models import Commands

def index(request):
    context = {'boldmessage': "I am bold font from the context"}
    return render(request, 'psw/index.html', context)

def servers(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['ip']
            system = form.cleaned_data['system']
            ram = form.cleaned_data['ram']
            quote = form.cleaned_data['quote']
            commandlog = 'python3.5 /root/log_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote + ' >> PSW_log.log'

            command = 'python3.5 /root/main_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote + '  > wyniki_testy.txt'
            
            #form.save()

#Tworzenie ze skryptu.py Python 3.5 
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('89.206.7.46', username='root', password='TrudneHaslo123')
                # Tworzenie Log
                stdin, stdout, stderr = ssh.exec_command(commandlog)
                # Tworzenie kontenerow
                stdin, stdout, stderr = ssh.exec_command(command)
                ssh.close()
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                print ('Error %s' %e)
                return HttpResponseRedirect('/psw/servers/')
                      
            return HttpResponseRedirect('/psw/')
        
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'psw/userview.html')
        else:
            return render(request, 'psw/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'psw/login.html', {'form': form})