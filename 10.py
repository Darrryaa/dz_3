raw = input('Enter number:')
try:
    num = int(raw)
    print(num)
except ValueError:
    print('Введено не число')