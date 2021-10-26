a = 21
b = 44
c = 32


def arithmetic(a, b, c):
    return


if c == "+":

    print(a, "+", b, "=", a + b)
elif c == "-":
    print(a, "-", b, "=", a - b)
elif c == "*":
    print(a, "*", b, "=", a * b)
elif c == "/":
    print(a, "/", b, "=", a / b)
else:
    print("Неизвестная операция ")


def season(num):
    if num == 12 or 1 <= num <= 2:
        print("Зима")

    elif 3 <= num <= 5:
        print("Весна")

    elif 6 <= num <= 8:
        print("Лето")

    elif 9 <= num <= 11:
        print("Осень")

    else:
        print("Неверно введён номер месяца!")


n = int(input("Введите номер месяца (1-12): "))




def is_prime(a):
    if a % 2 == 0:
     return a == 2
    d = 3
    while d * d <= a and a % d != 0:
     d += 2


     return d * d > a


year=int(input(2003))
if (year%4 == 0 and year%100 == 0) or year%400 == 0:
    print('yes')
else:
    print('no')

def square(a):
 return "Периметр квадрата равен:  " + str(4 * a) + "\n" + "Площадь квадрата равна:  " + str(a**2) + "\n" + "длина квадрата " + str(a + a + a + a)

print(square(2))