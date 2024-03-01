X = int(input())
Y = int(input())

num = 1 if (X / Y) % 1 == 0 or (Y / X) % 1 == 0 else 0
print(num)