#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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

print('%04d-%04d' % (3, 1))
print('%.3f' % 3.1415926)

print('hi,%s,you have $%06x' %('niehonglin',10000))

print('the growth is %%%d' %20)

s1 = 72
s2 = 85
r = (85 - 72)/72
print('hello,{0},成绩提升了{1:.4f}%'.format('xiaoming',r))

print('中文'.encode('utf-8'))
print('中文'.encode('gb2312'))