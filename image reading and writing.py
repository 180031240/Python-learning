f = open('doraemon.jpg', 'rb')

f1 = open('copy_doraemon.jpg', 'wb')

for i in f:
    f1.write(i)