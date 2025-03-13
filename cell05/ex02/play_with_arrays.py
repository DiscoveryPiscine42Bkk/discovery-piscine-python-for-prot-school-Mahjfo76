number = [2, 8, 9, 48, 8, 22, -12, 2]

new_num = []

print(number)

x = 0

while x < 8 :
    
    if number[x] > 5 :
        new_num.append(number[x] + 2)
    x += 1

print(new_num)
