start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for num in range(start, end + 1):

    if num <= 1:
        continue
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num, "ура! Это простое число !")
input()