import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.110', username='root', password='TrudneHaslo123')
stdin, stdout, stderr = ssh.exec_command('/bin/bash /root/skrypt.sh')
ssh.close()