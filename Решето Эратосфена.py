#находим все простые числа до n
#создаем решето и вычеркиваем числа, кратные i, пока само i^2 не будет >= n

n = int(input())
prime = []
arr = [i for i in range(0, n+1)]
i = 2
while i*i <= n:
    if arr[i] != 0:
        for x in range(i*i, n+1, i):
            arr[x] = 0
    i += 1
for i in range(n):
    if arr[i] != 0:
        print(arr[i])