second = 0
while second < 1 or second > 86400:
    second = int(input("Введите секунды в диапозоне от 1 до 86400: "))
 # Часы
clock = int(second / 3600)

# Остаток секунд и минуты
secondOst = int(second - clock * 3600)
minutes = int(secondOst / 60)

# Оставшиеся секунды
secondMinutesOst = int(secondOst - minutes * 60)

print(f"Время {clock}:{minutes}:{secondMinutesOst}")
