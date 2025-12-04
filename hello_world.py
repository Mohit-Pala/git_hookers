import os
import subprocess
 
 
# get the diff from the last commit  

diff = subprocess.check_output(['git', 'diff', 'HEAD^', 'HEAD']).decode('utf-8')
print("slop code written, heres whars changed:\n", diff)