age_input = int(input("Please tell me your age : "))
age = 10

print(f"You are currently {age_input} years old.")

while age < 31 :
    
    print(f"In {age} years, you'll be {age_input+age} years old.")

    age += 10