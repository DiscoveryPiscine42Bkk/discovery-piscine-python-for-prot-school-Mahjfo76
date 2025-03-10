print("Enter the first number")
first_number = int(input())

print("Enter the second number")
second_number = int(input())

result = first_number*second_number

print(str(first_number) + "x" + str(second_number) + "=" + str(result))

if result > 0 :
    print("The result is positive.")

elif result < 0 :
    print("The result is negative.")

elif result == 0 :
    print("The result is positive and negative.")