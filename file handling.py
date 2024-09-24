#open("<Name of the file>", mode as read r write w overwrite)

f = open('fh_filehandling_text', 'r')

#print(f.read()) #prints all the content of the file

#print(f.readline(),end = "#")
#print(f.readline(10))#prints 10 characters


f1 = open('abc', 'w')#Creates a file abc in write mode
f1.write("I am now writing in f1")

#If you want to append the lines instead of overwriting the file
f2 = open('abc', 'a')
f2.write("I am now using append")

#Copying every content in fh_filehandling_test to abc file

f3 = open('abc','w')
for i in f:
    f3.write(i)

