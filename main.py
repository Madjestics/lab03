N = (int(input("Введите количество чисел: ")))
a = []
for i in range(N):
    a.append(int(input("Введите число: ")))
print("Начальный массив")
print(a)

b = int(input("Введите 1, если необходимо сортировать по возрастанию и 2, если по убыванию: "))
if (b!=1 or b!=2):
    print("Вы ввели неверные числа")
for i in range(N - 1):
    for j in range(N - i - 1):
        if (b==1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        else:
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
print("Массив после сортировки")
print(a)