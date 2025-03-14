import sys

if len(sys.argv) == 1 :
      print("None")

else :
    print(f"Parameter : {len(sys.argv) -1 }")

    for x in sys.argv :
         print(f"{x} : {len(x)}")
