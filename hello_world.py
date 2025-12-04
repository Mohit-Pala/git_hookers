import os
import subprocess



# get git diff
diff = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1'], capture_output=True, text=True).stdout
print("slop code written, heres whars changed:")
print(diff)