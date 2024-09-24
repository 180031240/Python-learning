list = [5, 4, 6, 7, 8, 10, 42, 3]
n = 100
def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False

if search(list,n):
    print("Found")
else:
    print("Not Found")

search(list,n)