#!/usr/bin/python
import subprocess
import sys
import os
from ssh import Client

class Rsync():
    def rsync(self, user, ip, path, data): 
        try:
            subprocess.call(['rsync' ,'-rzv' ,data,'{user}@{ip}:{path}'.format(user=user, ip=ip, path=path)])
        except Exception as e:
            print 'Exception {var}'.format(var = e)
        #return

class Kill():
    def supervisor(self, ip,user, passwd):
        cl = Client(host = ip, username = user, password = passwd)
        s = cl.exec_command("ps axuf | grep -v grep | grep supervisor")  
        rc = s.split()
        cl.exec_command("kill {var}".format(var = rc[1]))
        #return

class Start():
    def supervisor(self, ip,user, passwd):
        cl = Client(host = ip, username = user, password = passwd)
        s = cl.exec_command("sleep 5; /etc/init.d/supervisord start") 
        #return 

class Interface():
    def __init__(self):
        data, user, passwd = self.settings()
        path = self.input_func()
        ip = raw_input("Enter the ip address: ")
        Rsync().rsync(ip=ip, user=user, path=path, data=data)
        Kill().supervisor(ip=ip, user=user, passwd=passwd)
        Start().supervisor(ip=ip, user=user, passwd=passwd)

    def settings(self):
        a = open('config.sh', 'r')
        content = a.readlines()
        points = map(lambda line: line.split()[1], content) 
        data = points[0]
        user = points[1]
        passwd = points[2]
        a.close()
        return data,user,passwd

    def input_func(self):
        if os.path.exists('path_file'):
            path = []
            a = open('path_file', 'r')
            for line in a:
                path.append(line)
            a.close()
        else:
            path = raw_input("Enter the path: ")
            f = open('path_file', 'w+')
            f.write(path)
            f.close()
        return path[0]

if __name__=='__main__':
    i = Interface()
      

