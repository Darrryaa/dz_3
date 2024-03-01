import math
a=float(input('Введите сторону а: '))
b=float(input('Введите сторону b: '))
c=float(input('Введите сторону c: '))

if a+b>c and a+c>b and b+c>a:

    #в радианах
    alpha_rad = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    beta_rad = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    gamma_rad = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    #в градусах
    alpha_deg = math.degrees(alpha_rad)
    beta_deg = math.degrees(beta_rad)
    gamma_deg = math.degrees(gamma_rad)

    print(f'Угол alpha : {alpha_deg} градусов')
    print(f'Угол beta : {beta_deg} градусов')
    print(f'Угол gamma : {gamma_deg} градусов')
else:
    print('Треугольник с такими сторонами не существует.')

