num_input = int(input("Enter your number : "))

if num_input > 25 :
    print("Error")

while num_input <= 25 :
    print(num_input)

    num_input = num_input + 1 

    if num_input == 26 :
        break