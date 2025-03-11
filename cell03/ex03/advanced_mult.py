x = 0

while x < 11 :
    number = 0
    print(f"Table de {x}", end="")
    
    while number < 11 :
        print(x*number , end=" ")

        number += 1
        
    print()
    x += 1
