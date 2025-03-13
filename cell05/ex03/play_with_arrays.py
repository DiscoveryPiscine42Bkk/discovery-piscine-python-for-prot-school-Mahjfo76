number = [2, 8, 9, 48, 8, 22, -12, 2]
new_number = set()
num = 0

print(number)

while num < 8 :

    if number[num] > 5 :
        new_number.add(number[num] + 2)

    num += 1

print(new_number)
