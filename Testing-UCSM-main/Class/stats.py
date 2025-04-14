def stats(lst):
    min_val = None
    max_val = None
    freq = {}

    for i in lst:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    lst_sorted = sorted(lst)
    if len(lst_sorted) % 2 == 0:
        middle = len(lst_sorted) // 2
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 3  #Error
    else:
        median = lst_sorted[len(lst_sorted) // 2]

    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    return {
        "min": min_val,
        "max": max_val,
        "median": median,
        "mode": mode
    }

def test_median():
    result = stats([1, 3])
    assert result["median"] == 2.0 

def test():
    print(stats([1, 2, 4, 3]))
    print()
    print(stats([4, 4, 4, 5, 6, 6]))
    print()
    print(stats([7, 7, 7, 7]))

# Ejecutamos los tests
test_median()  
test()




