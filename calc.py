count = int(input("Введите количество операций "))
i = 0
print("Введите первое число ")
one = float(input())
print("Введите второе число ")
two = float(input())
print("Выберете операцию")
print("1 Сложение 2 Вычитание 3 Деление 4 Умножение")
operation = int(input())
while operation > 4 or operation <= 0:
        print("Введите предложенную операцию ")
        operation = int(input())
else:
        if operation == 1:
            rezult = one + two
            i += 1
            print("Ответ ", rezult )
        elif operation == 2:
            rezult = one - two
            i += 1
            print("Ответ ", rezult)
        elif operation == 3:
            while two == 0:
                print ("Ошибка, Введите новое число ")
                two = float(input())
            else:
                rezult = one / two
            print("Ответ ", rezult)
        elif operation == 4:
            rezult = one * two
            i += 1
            print("Ответ ", rezult)
        while i < count:
            print("Введите число ")
            one = float(input())
            print("Выберете операцию ")
            print("1 Сложение 2 Вычитание 3 Деление 4 Умножение ")
            operations = int(input())
            while operations > 4 and operations < 0:
                print("Введите предложенную операцию ")
                operations = int(input())
            else:
                if operations == 1:
                    rezult += one
                    i += 1
                    print("Ответ ", rezult )
                if operations == 2:
                    rezult = rezult - one
                    i += 1
                    print("Ответ ", rezult)
                if operations == 3:
                    while one == 0:
                        print ("Ошибка, Введите новое число")
                        one = float(input())
                    else:
                        rezult /= one
                        i += 1
                        print("Ответ ", rezult)
                if operations == 4:
                    rezult *= one
                    i += 1
                    print("Ответ ", rezult)
            