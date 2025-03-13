#user_input = str(input())

#if len(user_input) == 0 :
#    print("None")

#else :
#    print(user_input.upper())

import sys

user_input = " ".join(sys.argv[1:])

if len(sys.argv) == 1 :
    print("None")

else :
    print(user_input.upper())
