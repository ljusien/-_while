l = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(l):
    number = l[index]
    if number < 0:
        break
    if number > 0:
        print(number)
    index += 1
