#eucledus - НОД

a = int(input())
b = int(input())
d = 100000000000
step = 0
while d != 0:
    step += 1
    d = max(a, b) % min(a, b)
    if a > b:
        a = d
    else:
        b = d
    print(step, a, b, d)