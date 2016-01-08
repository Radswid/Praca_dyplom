# -*- coding: utf-8 -*-
import sys
import subprocess
from subprocess import PIPE

'''ip = sys.argv[1]
system = sys.argv[2]
ram = sys.argv[3]
quote = sys.argv[4]'''

user = 'Ktos'
system = 'Ubuntu'
ram = 128
quote = 5

def low_letters(*argsl):
    user = argsl[0].lower() 
    system = argsl[1].lower()

    return user, system

def creating_id():

    all_id = []
    command = "vzlist | awk '{print $1}'"
    uid = 1
    
    proc = subprocess.Popen(command, shell=True, stdout=PIPE, universal_newlines=True)

    for line in iter(proc.stdout.readline, ''):
        all_id.append(line.rstrip('\n'))

    all_id = [int(i) for i in all_id[1:]]
    
    for item in all_id:
        if item == uid: 
            uid = uid + 1
            
        else :
            uid 
    return uid       

def creating_name(*argsn):
    server_name = str(argsn[0]) + '_' + str(argsn[1]) + '_' + str(argsn[2]) + '_' + str(argsn[3])
    host_name = str(argsn[0]) + '_' + str(creating_id()) + '.test.pl'
    return server_name, host_name

def choose_system(*argss):
    system = ''

    if 'ubuntu' in argss[0]:
        system = 'ubuntu-12.04-x86_64'
    elif 'debian' in argss[0]:
        system = 'debian'
    else:
        system = 'inny'
    return system
    
    


def creating_contener(*argsc):
    uid = creating_id()
    uid = str(uid)
    server_name = creating_name(low[0],low[1],ram,quote)

    com_create = 'vzctl create ' + uid + ' --ostemplate ' + choose_system(low[1]) + ' --config vswap-1g'
    com_name = 'vzctl set ' + uid + ' --save --name ' + server_name[0]
    com_boot = 'vzctl set ' + uid + ' --save --onboot yes'
    com_host = 'vzctl set ' + uid + ' --save --hostname ' + server_name[1]
    

    return com_create, com_name, com_boot, com_host 
 





low = low_letters(user,system)
server_id = creating_id()
server_name = creating_name(low[0],low[1],ram,quote)
chsystem = choose_system(low[1])
con = creating_contener()
print ('ID: ', server_id)
print ('Server name: ', server_name[0])
print ('Host name: ', server_name[1])
print ('System:',chsystem)
print ('contener create:',con[0])
print ('contener name:',con[1])
print ('contener boot:',con[2])
print ('contener host:',con[3])



'''if system =='Ubuntu':
    subprocess.run(['vzctl','create'],shell=True,check=True)
    

        
else:
    pass




for arg in sys.argv:
    print (arg)'''

