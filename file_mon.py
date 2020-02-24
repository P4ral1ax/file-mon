"""
This program will monitor directories and files to see if they were edited
or changed in any way. If there are any changes it alerts the user and
logs the action.
"""

import os
import time
import sys
from os import path
from monitor import *
from datastructure import *
from create_dataclass import *


def path_exists(path):
    return path.exists(path)


def make_file_array():
    file_array = []
    file = open('files.txt')
    for line in file:
        line = line.strip('\n')
        if path.exists(line):
            file_array.append(make_file(line))
        else:
            print("File \'" + line + "\' is not valid path")
    return(file_array)


def make_directory_array():
    directory_array = []
    file = open('directories.txt')
    for line in file:
        line = line.strip('\n')
        if path.exists(line):
            directory_array.append(make_directory(line))
        else:
            print("Dir \'" + line + "\' is not valid path")
    return(directory_array)


def quickrun():
    files = make_file_array()
    directories = make_directory_array()
    monitor_main(files, directories)


def custom_mode():
    type = input("\n1. File\n2. Directory\n3. Both\n: ")
    if type == '1':
        files = make_file_array()
        monitor_main(files, [])
    elif type == '2':
        directories = make_directory_array()
        monitor_main([], directories)
    elif type == '3':
        files = make_file_array()
        directories = make_directory_array()
        monitor_main(files, directories)
    else:
        print("Not a valid input.")


def single_mode():
    type = input("\n1. File\n2. Directory\n: ")
    if type == '1':
        filepath = input("What is the path to the file : ")
        if path.exists(filepath):
            object = make_file(filepath)
            monitor_main([object], [])
        else:
            print("\nFile \'" + filepath + "\' is not valid path")
            single_mode()
    elif type == '2':
        directory = input("Directory Path : ")
        if path.exists(directory):
            object = make_directory(directory)
            monitor_main([], [object])
        else:
            print("\nDir \'" + directory + "\' is not valid path")
            single_mode()
    else:
        print("Invalid input\n")
        single_mode()



def main():
    mode = input("---Modes---\n1. Quickrun\n2. Custom Mode\n3. Single Mode\n: ")
    if mode == '1':
        quickrun()
    elif mode == '2':
        custom_mode()
    elif mode == '3':
        single_mode()
    elif mode == 'q' or mode == 'Q':
        sys.exit()
    else:
        print("Invalid Input.")
        main()

main()
