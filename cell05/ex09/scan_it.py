import re
import sys


if len(sys.argv) == 3 :

    check_word = re.findall(sys.argv[1], str(sys.argv[2::]))

    print(len(check_word))

else :
    print("None")
