#!/usr/bin/python

import subprocess

if( subprocess.call(["python", "test1.py"]) ):
    print "Test1 failed"
    exit(1)
if( subprocess.call(["python", "test2.py"])):
    print "Test2 failed"

