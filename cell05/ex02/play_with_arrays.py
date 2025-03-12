number = [2, 8, 9, 48, 8, 22, -12, 2]

print(number)

number = [x + 2 for x in number]

print(number[1:6])

for num in number :
    if num > 5 :
        new_number.append(num + 2)

print(new_number)
