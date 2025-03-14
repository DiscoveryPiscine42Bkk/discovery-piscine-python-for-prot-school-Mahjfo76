import sys

if len(sys.argv) == 3 :
        if sys.argv[2] < sys.argv[1] :
             a = list(range(int(sys.argv[1]),int(sys.argv[2]) - 1, -1)) 
             print(a)
        else :
            a = list(range(int(sys.argv[1]),int(sys.argv[2]) + 1))
            print(a)

else :
    print("None")
