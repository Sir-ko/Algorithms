def binary_search(list, item): #ищем индекс вхождения
    lst = sorted(list)
    low = 0
    high = len(lst)-1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return mid
a = [0, 1, 2, 3, 4, 5, 6, 7, 100]
print(binary_search(a, 100))