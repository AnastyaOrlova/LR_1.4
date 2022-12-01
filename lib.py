from random import random

N = 100
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 50)
print(arr)

setarr = set(arr)
if len(arr) == len(setarr):
    print("Все элементы уникальны")
else:
    print("Есть одинаковые")

