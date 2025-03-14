import sys
import re

if len(sys.argv) == 1 :
    print("None")

else :
    check = "z"
    z_check = re.findall(check, str(sys.argv))

    print("z"*len(z_check))