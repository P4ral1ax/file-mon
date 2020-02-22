import os
import time
import sys
from datastructure import *
from create_dataclass import *

"""
After the UI is collected and all the files are set to be monitored, this
is where the program will do the monitoring.
"""
def path_exists(path):
    return path.exists(path)


def check_dir(files, directories, index):
    if not path_exists(dir.path):
        dir.name == 'DEL'

    dir_changed = False
    dir = directories[index]
    log = open('log.txt', 'a')
    info = os.stat(dir.path)

    if dir.name == "DEL":
        continue
    #Dir Permissions
    if info.st_mode != dir.perm:
        print("Permissions : " + dir.name + " | time : " + time.strftime('%H:%M:%S') + "\n    Old Perm: " \
        + str(oct(dir.perm)) + "\n    New Perm: " + str(oct(info.st_mode)), file=log, end='\n')
        dir_changed = True
    #Dir Access Time
    if info.st_atime != dir.time_acc:
        print("Size : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        dir_changed = True
    #Dir UID Changed
    if info.st_uid != dir.user:
        print("UID Changed : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        dir_changed = True
    #Dir GID Changed
    if info.st_gid != dir.group:
        print("GID Changed : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        dir_changed = True
    #Dir Links changed
    if info.st_nlink != dir.links:
        print("DIR Changed : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        dir_changed = True
    log.close()

    if dir_changed:
        update_directory(files, directories, index)


def check_file(files, directories, index):
    file_changed = False
    file = files[index]
    log = open('log.txt', 'a')
    info = os.stat(file.path)


    if file.name == 'DEL':
        pass
    #File Size
    if info.st_size != file.size:
        print("Size Changed : " + file.name + " | time : " +  time.strftime('%H:%M:%S') + "\n    Old Size:  " \
        + str(file.size) + "B\n    New Size: " + str(info.st_size) + "B", file=log, end='\n')
>>>>>>> ae36cf4d6cf53a26b90249e865224d84ff8b4f09
        file_changed = True
    #File Permissions
    if info.st_mode != file.perm:
        print("Permissions Changed: " + file.name + " | time : " + time.strftime('%H:%M:%S') + "\n    Old Perm: " \
        + str(oct(file.perm)) + "\n    New Perm: " + str(oct(info.st_mode)), file=log, end='\n')
        file_changed = True
    #File Access Time
    if info.st_atime != file.time_acc:
        print("File Accessed : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        file_changed = True
    #File Modify Time
    if info.st_mtime != file.time_mod:
        print("File Modify Time : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        file_changed = True
    #File Metadata Time
    if info.st_ctime != file.time_met:
        print("File Metadata Time : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        file_changed = True
    #File UID changed
    if info.st_uid != file.user:
        print("File UID Changed: " + file.name + " | time : " + time.strftime('%H:%M:%S') + "\n    Old UID: " \
        + str(file.user) + "\n    New UID: " + str(info.st_uid), file=log, end='\n')
        file_changed = True
    #File GID Changed
    if info.st_gid != file.group:
        print("File GID Changed : " + file.name + " | time : " + time.strftime('%H:%M:%S') + "\n    Old GID: " \
        + str(file.group) + "\n    New GID: " + str(info.st_gid), file=log, end='\n')
        file_changed = True
    #File Hard Links Amount Changed
    if info.st_nlink != file.links:
        print("Hard Links : " + file.name + " | time : " + time.strftime('%H:%M:%S') + "\n    Old Links: " \
        + str(file.links) + "\n    New Links: " + str(info.st_nlink), file=log, end='\n')
        file_changed = True

    log.close()

    if file_changed:
        update_file(files, directories, index)


def update_file(files, directories, index):
    file = files[index]
    if path_exists(file.path):
        temp = make_file(file.path)
        files[index] = temp
        print(temp)
    else:
        print("Deleted : " + file.path + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        file.name = 'DEL'


def update_directory(files, directories, index):
    dir = directories[index]
    if path_exists(dir.path):
        temp = make_directory(dir.path)
        directories[index] = temp
        print(temp)
    else:
        print("Deleted : " + dir.path + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        dir.name = 'DEL'



def monitor_main(files, directories):
    run = True
    while run:
        if files != []:
            for index in range(0, len(files)):
                check_file(files, directories, index)

        if directories != []:
            for index in range(0, len(directories)):
                check_dir(files, directories, index)
        time.sleep(.3)
