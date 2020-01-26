"""
File that helps create a new file or directory dataclass object for inital
creation and if the file changes and the data needs to be updated
"""

import os
from datastructure import *
def get_name(path):
    name = path.split('/')[-1]
    return(name)


def make_file(path):
    f_name     = get_name(path)
    f_info     = os.stat(path)
    f_perm     = f_info.st_mode
    f_size     = f_info.st_size
    f_time_acc = f_info.st_atime
    f_time_mod = f_info.st_mtime
    f_time_met = f_info.st_ctime
    f_user     = f_info.st_uid
    f_group    = f_info.st_gid
    f_links    = f_info.st_nlink
    return(File(f_name, path, f_size, f_perm, f_time_acc, f_time_mod, f_time_met, f_user, f_group, f_links))


def make_directory(directory):
    d_name     = get_name(directory)
    d_info     = os.stat(directory)
    d_perm     = d_info.st_mode
    d_size     = d_info.st_size
    d_time_acc = d_info.st_atime
    d_time_mod = d_info.st_mtime
    d_time_met = d_info.st_ctime
    d_user     = d_info.st_uid
    d_group    = d_info.st_gid
    d_links    = d_info.st_nlink
    return(Directory(d_name, directory, d_size, d_perm, d_time_acc, d_time_mod, d_time_met, d_user, d_group, d_links))
