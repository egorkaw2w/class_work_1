num = int(input("Введите число: "))
if num <= 1:
    print(num, "это не простое число :(")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "это не простое число :(")
            break
    else:
        print(num, "Бинго! Это простое число!")
input()