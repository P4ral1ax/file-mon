"""
The dataclass descriptioms for the program to reference. One description
for a file and one for a directory
"""

from dataclasses import dataclass
from typing import Union
from typing import List

@dataclass
class File:
    __slots__ = ['name', 'path', 'size', 'perm', 'time_acc', 'time_mod', 'time_met', 'user', 'group', 'links']
    name     : str
    path     : str
    size     : int
    perm     : int
    time_acc : int
    time_mod : int
    time_met : int
    user     : int
    group    : int
    links    : int

@dataclass
class Directory:
    __slots__ = ['name', 'path', 'size', 'perm', 'time_acc', 'time_mod', 'time_met', 'user', 'group', 'links', 'path']
    name     : str
    path     : str
    size     : int
    perm     : int
    time_acc : int
    time_mod : int
    time_met : int
    user     : int
    group    : int
    links    : int
