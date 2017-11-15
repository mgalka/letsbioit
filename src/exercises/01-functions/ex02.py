def my_sum(lst):
    result = 0
    for elem in lst:
        result = result + elem
    return result

l = [1, 2, 3]
print(my_sum(l))
print(my_sum([1,2,3,4,10]))