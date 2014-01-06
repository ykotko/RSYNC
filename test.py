#!/usr/bin/python
import subprocess
import sys

#cmdargs = (sys.argv)
#ip = sys.argv[1]
#path = sys.argv[2]
ip = raw_input("Enter the ip address: ")
path = raw_input("Enter the path: ")


try:
    rc = "rsync -rzv {0}:{1}".format(ip, path)
    subprocess.call( rc.split(' ') )
#subprocess.call(['rsync' ,'-rzv' ,ip+':'+path])
except Exception as e:
    print "Exception e"
	
