#!/usr/bin/python3
import os
path = '/tmp/testfile.txt'
if os.path.isdir(path):
    print("It is a Directpry")
elif os.path.isfile(path):
    print("It is file")
else:
    print("File or dir does not exist")

