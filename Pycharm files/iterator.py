nums = [7,8,9,10]
it = iter(nums)
print(it)
print(it.__next__())

class TopTen:
    def __init__(self):
        self.num = 1#counter variable
    def __iter__(self): #This method gives object of iterator
        return self
    def __next__(self): #Which gives next value
        if(self.num <= 10):
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values))#1 will not be printed twice because it's quality of iterator to move
for i in values:
    print(i)