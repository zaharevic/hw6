from random import randint

def FillArray(size):
    arr = list()
    for i in range(0,size):
        arr.append(randint(-100,100))
    return arr

max, min, size = int(input("max: ")), int(input("min: ")), int(input("размер списка: "))
if(max > min):
    arr = FillArray(size)
    true = list()
    print(f"Начальный список: \n{arr}")
    for i in range(0, size):
        if (arr[i] > min) and (arr[i] < max):
            true.append(arr[i])
    print(f"Конечный список: \n{true}")
else:
    print("Неверные данные!")