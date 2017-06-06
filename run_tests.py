#!/usr/bin/python

import subprocess

if( subprocess.call(["python", "test1.py"]) ):
    print "Test1 failed"
    exit(1)
if( subprocess.call(["python", "test2.py"])):
    print "Test2 failed"

if( subprocess.call(["python", "test3.py"])):
    print "Test3 failed"
    exit(3)


