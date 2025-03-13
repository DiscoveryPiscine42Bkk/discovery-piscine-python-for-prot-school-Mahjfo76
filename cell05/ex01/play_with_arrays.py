number = [2, 8, 9, 48, 8, 22, -12, 2]

new_num = []

print(f"Original array:{number}")

x = 0 

while x < 8 :
    new_num.append(number[x] + 2)

    x += 1



# number = [x + 2 for x in number]
print(f"New array:{new_num}")
