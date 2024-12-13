def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        right = [i for i in lst if i > pivot]
        left = [i for i in lst if i < pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

lst = [5, 3, 6, 1, 3, 4, 1000, 345, 545, 355, 765,8786, 54, 45]
print(quick_sort(lst))