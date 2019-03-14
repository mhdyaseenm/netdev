"""Simple script that implements scp"""
import os
import sys
import getpass
import paramiko

from scp import SCPClient


dir = sys.argv[1]
dst_filename = sys.argv[2]


def scp_image(host,username,password,file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password, look_for_keys=False,allow_agent=False, timeout=20)
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(file,dst_filename)
        print "File Copied to "+host


username=raw_input("Username:")
password=getpass.getpass()

hostnames=os.listdir(dir)

for i in hostnames:
    i_file=dir+i
    scp_image(i,username,password,i_file)
