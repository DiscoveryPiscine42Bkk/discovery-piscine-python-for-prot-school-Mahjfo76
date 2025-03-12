num_input = int(input("Enter a number less than 25 : "))

if num_input > 25 :
    print("Error")

while num_input <= 25 :
    print(f"Inside the loop, my variable is : {num_input}")

    num_input = num_input + 1 

    if num_input == 26 :
        break
