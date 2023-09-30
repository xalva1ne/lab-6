import math

a = float(input('Введите коэффициент A: '))
b = float(input('Введите коэффициент B: '))
c = float(input('Введите коэффициент C: '))

D = (b**2)-(4*a*c)

if a == 0:
    x = -c / b
    print(f'Корень x = {round(x,2)}')
else:
    if D > 0:
        # Два корня
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f'Корень x1 = {round(x1, 2)}, корень x2 = {round(x2, 2)}')
    elif D == 0:
        # Один корень
        x1 = -b / (2*a)
        print(f'Корень один, он равен {round(x1, 2)}')
    else:
        # Комплексные корни
        x1 = -b / (2*a)
        x2 = math.sqrt(-D) / (2*a)
        print(f'Комплексные корни\n{round(x1, 2)} + {round(x2, 2)}i\n{round(x1, 2)} - {round(x1, 2)}i')


