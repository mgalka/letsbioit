def remove_negative(lst):
    result = []
    for elem in lst:
        if elem > 0:
            result.append(elem)
    return result

l = [1, 2, 3, 4, -10, 20, 0, -100]
print(remove_negative(l))