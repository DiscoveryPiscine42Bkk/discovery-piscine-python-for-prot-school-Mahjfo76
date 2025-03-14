import sys

if len(sys.argv) == 3 :
    a = [new for new in range(int(sys.argv[1]),int(sys.argv[2]) + 1)]
    print(a)

else :
    print("None")