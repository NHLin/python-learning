print('\\\t\\')
print(r'\\\t\\')

print('''hello
world\n
niehonglin''')

print(True or False)
print(True and False)
print(not True)

print(None)
print(type(None))

print(10/3)
print(9/3)

print(10//3)
print(9//3)
print(10%3)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = '''Hello,\n
Lisa!'''

print(n,f,s1,s2,s3,s4)

#ord()函数获取字符的整数表示
print(ord('A'))
print(ord('中'))

#chr函数把编码转换为对应的字符
print(chr(90))
print(chr(2000))

print('abc'.encode('ascii'))
print('中文'.encode('utf-8'))
print(ord('文'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'abc'.decode('utf-8'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('中文'))
print(len('中文'.encode('utf-8')))

