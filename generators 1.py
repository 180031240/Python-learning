#since it's a generator to give iterator,
def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n+=1




values = topten()
for i in values:
    print(i)

#Generators are used for?
# When we want to fetch 1000 records, they all will be fetched in a memory which we don't want. If we want to use one value at a time, we can use a generator