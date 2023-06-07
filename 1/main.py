def FillArray(a1, n, d, array):
    for i in range(0,n):
        array[i] = a1+i*d

a1, n, d = int(input("Первый элемент: ")), int(input("Кол-во элементов: ")), int(input("Шаг: "))
array = [0] * n
FillArray(a1,n,d,array)
print(array)