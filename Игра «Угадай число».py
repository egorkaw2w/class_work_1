import random

print("Я загадал число от 1 до 100. Попробуйте угадать его за минимальное количество попыток.")

number = random.randint(1, 100)
thought = int(input("Введите число: "))
tries = 1

while thought != number:
    if thought > number:
        print("Меньше...")
    else:
        print("Больше...")
    thought = int(input("Введите число: "))
    tries += 1

print("Поздравляю, вы угадали число за", tries, "попыток!")
input()