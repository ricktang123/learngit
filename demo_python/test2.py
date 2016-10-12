#!/usr/bin/python
#import os
#val=os.system('ll')
#print val
import commands
a,b=commands.getstatusoutput('ls /lab/sgsn_st_logs/sgsn_R63/LSV/feature_and_function/MkX')
base=b.split('\n')
print b
#import subprocess
#subprocess.call('ls',shell=True)
#base=b.split('\n')
print base
