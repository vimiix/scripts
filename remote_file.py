#coding=utf-8
#
#**************************************
# 文件名:remote_file.py
# 功能：实现本地主机和远程主机之间上传文件或下载文件
# 使用：上传：python remote_file.py put [localfilepath] [remotefilepath]
#       下载：python remote_file.py get [localfilepath] [remotefilepath]
# 作者：vimiix
#***************************************

import paramiko
import sys

#远程主机信息
hostname = '192.168.xx.xx'
port = 22
username = 'root'
password = '123456'
if len(sys.argv) > 4:
    #本地文件路径
    localFilePath = sys.argv[2]
    #远程主机文件路径
    remoteFilePath = sys.argv[3]

    trans = paramiko.Transport(hostname, port)
    trans.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(trans)
    if sys.argv[1] == 'put':
        sftp.put(localFilePath,remoteFilePath)
        trans.close()
    elif sys.argv[1] == 'get':
        sftp.get(remoteFilePath, localFilePath)
        trans.close()
    else:
        print('Wrong input.\n Usage:\nPutfile cmd : python remote_file.py put [localfilepath] [remotefilepath]\nGetfile cmd : python remote_file.py get [localfilepath] [remotefilepath]')
else:
    print('Wrong input.\n Usage:\nPutfile cmd : python remote_file.py put [localfilepath] [remotefilepath]\nGetfile cmd : python remote_file.py get [localfilepath] [remotefilepath]')



