#Filter
def is_even(n):
    return n % 2 == 0


nums = [2, 3, 4, 5, 67, 7, 8, 9, 1, 11]
evens = list(filter(is_even, nums))

print(evens)

odds = list(filter (lambda n : n%2 != 0, nums))
print(odds)

#Map - Changing all the values

doubles = list(map(lambda n: n+n,evens))
print(doubles)

#Reduce - When you want to find the one value out of the chunk like average, sum, product

from functools import reduce
sum = reduce(lambda a,b : a +b, evens)
print(sum)
