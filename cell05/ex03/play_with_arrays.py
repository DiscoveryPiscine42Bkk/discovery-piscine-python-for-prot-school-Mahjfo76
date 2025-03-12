number = [2, 8, 9, 48, 8, 22, -12, 2]
new_number = set()


print(number)

for num in number :
    if num > 5 :
        new_number.add(num + 2)


print(new_number)
