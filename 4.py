data = input("Введите через пробел X Y N:").split(" ")
print(f"{int((int(data[0]) * int(data[2])) + (int(data[1]) * int(data[2])) / 100)} руб. {(int(data[1]) * int(data[2])) % 100} коп.")