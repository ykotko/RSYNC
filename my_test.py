#!/usr/bin/python
import subprocess
import sys
import os
from fuel_health.common.ssh import Client

a = open('config.sh', 'r')
content = a.readlines()
for l in content:
    if l.find('data') != -1:
        data = l.split()[1]
    
#content = a.readlines()
for l in content:
    if l.find('user') != -1:
        user = l.split()[1]

#content = a.readlines()
for l in content:
    if l.find('pass') != -1:
        passwd = l.split()[1]
       

content = a.read()
data = content.find('/etc/hosts')

#cmdargs = (sys.argv)
#ip = sys.argv[1]
#path = sys.argv[2]

ip = raw_input("Enter the ip address: ")
if os.path.exists('path_file'):
    a = open('path_file', 'r')
    for line in a:
         path = line    
else:
    path = raw_input("Enter the path: ")
    #f = open('~/path_file', 'w+')
    f = open('path_file', 'w+')
    f.write(path)
try:
#    rc = "rsync -rzv {0}:{1}:{2}".format(ip, data, path)
#    subprocess.call( rc.split(' ') )
    subprocess.call(['rsync' ,'-rzv' ,data,user+'@'+ip+':'+path])
except Exception as e:
    print 'Exception {var}'.format(var = e)

ip = str(ip)
user = str(user)
#passd = str(passd)
print ip
print user
#print passwd

cl = Client(host = ip, username = user, password = passwd)
#cl = Client(host = '172.18.166.197', username = 'root', password = 'r00tme')	
#cl.exec_command("a=(`ps axuf | grep -v grep | grep supervisor | awk '{print $2}'`); if [[ -n \"$a\" ]]; then kill $a; else echo 'No supervisord process'; fi")
s = cl.exec_command("ps axuf | grep -v grep | grep supervisor") # hole string with pid 
rc = s.split()
cl.exec_command("kill {var}".format(var = rc[1])) # will give a <pid> of process supervisord


