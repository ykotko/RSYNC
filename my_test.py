#!/usr/bin/python
import subprocess
import sys
import os
from fuel_health.common.ssh import Client



#cmdargs = (sys.argv)
#ip = sys.argv[1]
#path = sys.argv[2]
data = '/etc/hosts'
user = 'root'
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
#    subprocess.call(['rsync' ,'-rzv' ,ip+':'+path])
    subprocess.call(['rsync' ,'-rzv' ,data,user+'@'+ip+':'+path])
except Exception as e:
    print 'Exception {var}'.format(var = e)
cl = Client(host = '172.18.166.197', username = 'root', password = 'r00tme')	
cl.exec_command("a=(`ps axuf | grep -v grep | grep supervisor | awk '{print $2}'`); if [[ -n \"$a\" ]]; then kill $a; else echo 'No supervisord process'; fi")
