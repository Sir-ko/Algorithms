def divide_and_conquer(x, y):
    a = min(x, y)
    b = max(x, y)
    if b % a == 0: #базовый случай
        return a
    else:
        print(a, b % a)
        return divide_and_conquer(a, b % a) #рекурсивный случай

print(divide_and_conquer(1680, 640))