N = (int(input("Введите количество чисел: ")))
a = []
for i in range(N):
    a.append(int(input("Введите число: ")))
print("Начальный массив")
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print("Массив после сортировки")
print(a)