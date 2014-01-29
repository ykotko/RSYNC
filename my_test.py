#!/usr/bin/python
import subprocess
import sys
import os
#from fuel_health.common.ssh import Client
from ssh import Client

class Rsync():
    def rsync(self, user, ip, path, data): 
        try:
        #    rc = "rsync -rzv {0} {1}@{2}:{3}".format(data,user,ip,path)
        #    subprocess.call( rc.split(' ') )
        #    subprocess.call(['rsync' ,'-rzv' ,data,user+'@'+ip+':'+path])
            #print path[0]
            subprocess.call(['rsync' ,'-rzv' ,data,'{user}@{ip}:{path}'.format(user=user, ip=ip, path=path)])
        except Exception as e:
            print 'Exception {var}'.format(var = e)
        return
    #rsync(user,ip,path)


class Kill():
    def supervisor(self, ip,user, passwd):
        cl = Client(host = ip, username = user, password = passwd)
        #cl.exec_command("a=(`ps axuf | grep -v grep | grep supervisor | awk '{print $2}'`); if [[ -n \"$a\" ]]; then kill $a; else echo 'No supervisord process'; fi")
        s = cl.exec_command("ps axuf | grep -v grep | grep supervisor") # hole string with pid 
        rc = s.split()
        cl.exec_command("kill {var}".format(var = rc[1]))
        return
    #supevisor(ip,user,passwd)




class Interface():
    def __init__(self):
        #clr = Rsync()
        #clk = Kill()    
        data, user, passwd = self.settings()
        path = self.input_func()
        ip = raw_input("Enter the ip address: ")
        Rsync().rsync(ip=ip, user=user, path=path, data=data)
        Kill().supervisor(ip=ip, user=user, passwd=passwd)

    def settings(self):
        a = open('config.sh', 'r')
        content = a.readlines()
        for l in content:
            if l.find('data') != -1:
                data = l.split()[1]
            if l.find('user') != -1:
                user = l.split()[1]
            if l.find('passwd') != -1:
                passwd = l.split()[1]
        a.close()
        return [data,user,passwd]
    #data,user,passwd = settings()


    #cmdargs = (sys.argv)
    #ip = sys.argv[1]
    #path = sys.argv[2]


    def input_func(self):
        if os.path.exists('path_file'):
            path = []
            a = open('path_file', 'r')
            for line in a:
                path.append(line)
            a.close()
        else:
            path = raw_input("Enter the path: ")
            #f = open('~/path_file', 'w+')
            f = open('path_file', 'w+')
            f.write(path)
            f.close()
        #return path;
        return path[0]
    #path = input_func()
    #path = path


        

if __name__=='__main__':
    #cl = sync()
    #data,user,passwd = cl.settings()
    #path = cl.input_func()
    #cl.rsync(user,ip,path)
    #cl.supevisor(ip,user,passwd)
    #Rsync(ip = ip, user = user, path = path)
    #Kill(ip = ip, user = user, passwd = password)
    i = Interface()
      

