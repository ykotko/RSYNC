#!/usr/bin/python
import subprocess
import sys
import os


#Comment
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
    rc = "rsync -rzv {0}:{1}".format(ip, path)
    subprocess.call( rc.split(' ') )
#subprocess.call(['rsync' ,'-rzv' ,ip+':'+path])
except Exception as e:
    print "Exception e"
	
