import sys

if len(sys.argv) == 1 :
    print("None")

else :
    x = 1
    while x < len(sys.argv) :
        if not sys.argv[x].endswith("ism") :
            print(sys.argv[x] + "ism")
        
        x += 1