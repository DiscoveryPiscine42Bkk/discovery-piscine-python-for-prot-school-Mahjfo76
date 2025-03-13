import sys

x = 0

if len(sys.argv) < 2 :
    print("None")

else :
    while x < len(sys.argv) :
        print(sys.argv[::-1][x])

        x += 1

#x = 0

#user_input = input().split()

#if len(user_input) < 2 :
#    print("None")

#else :
#    while x < len(user_input) :
#        print((user_input[::-1][x]))
#        x += 1 