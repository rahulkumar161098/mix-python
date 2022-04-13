# ****************8 file handling *******************
'''
These mode are only applicable only for text files.

r = read      f=open('abc.txt', 'r')
w = write    f=open('abc.txt', 'w')
a = append    f=open('abc.txt', 'a')
r+ =  to read and then write     f=open('abc.txt', 'r+')
w+ = to write and then read (it will over write exiting data)     f=open('abc.txt', 'w+')
a+ = first append and then read it won't over write existring data    f=open('abc.txt', 'a+')
x = (exclusive)= compulary fiel sholud not be available     f=open('abc.txt', 'x')

'''


# eng Pro

# f=open('abc.txt','a')
# print('file name is : ', f.name)
# print('file mode is : ', f.mode)
# print('Is file readable : ', f.readable())
# print('Is file writable : ', f.writable())
# print('Is file closed : ', f.closed)
# f.close()
# print('Is file closed : ', f.closed)


# write data in programe
# f=open('abc.txt', 'w')
f=open('abc.txt', 'a')
f.write('Hello ')
f.write('Rahul\n')

'''
for binary file these modess are available .

'''