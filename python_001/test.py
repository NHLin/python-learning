#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#from numpy.core import double

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

#list列表，是可变的
l1 = [1, 2, 3, 4]
print(l1)
print(len(l1))
print(l1[-2])

l1.append(6)
print(l1)
l1.insert(2,8)
print(l1)
l1.pop(3)
print(l1)

#tuple元组，tuple一旦初始化就不能修改
classmates = (1,2,3,4)
print(classmates)
print(len(classmates))

t = ()      #空元组
print(len(t), type(t))

t1 = (1,)       #含有一个元素的元组
print(len(t1), type(t1))

t2 = (1)    #表示整数int
print( type(t2))

#元组中可以嵌套list
t = ('a','b',['A','B'])
print(t)

#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
t[2][0] = 'c'
print(t)

#条件判断
#bmi = input("please input the number:")
bmi = 25
bmi = float(bmi)
print('bmi =', bmi)
if bmi > 32:
    print("serious fat")
elif bmi >= 28:
    print('fat')
elif bmi >= 25:
    print('over weight')
elif bmi >= 18.5:
    print('normal')
else:
    print("over thin")

l1 = [1, 2, 3, 4]
for var in l1:
    print(var)

print(range(100))
print(type(range(50)))
print(type(list(range(100))))

print(list(range(20)))

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    if n < 50:
        break   #提前结束循环
print(sum)

n = 0
while n < 10:
    n = n + 1
    if n % 2 != 0:
        continue    #跳过某一次循环
    print(n)

#死循环
#while 1:
print('eldless circle')

#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
dict1 = {'tom': 90, 'jim': 85, 'sam': 87}
print(dict1)
print(type(dict1))
dict1['bob'] = 95
print(dict1)
dict1['tom'] = 93

print(dict1)

print(dict1['tom'])
dict1['xiaoming'] = 89
print(dict1['xiaoming'])
print('tom' in dict1)
print(dict1.get('bob'))
print(dict1.get('xiaohong', -2-2))

print(dict1)
dict1.pop('jim')
print(dict1)

dict1['xiaohong'] = 67
dict1['anly'] = 83
print(dict1)

#key = [1, 2, 3]
#print(type(key))
#dict1[key] = 94
key1 = (1, 2, 3)
print('debug log')
print(type(key1))
dict1[key1] = 99
print(dict1)
#print('debug log')

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
set1 = set([1, 2, 3, 4])
print(set1)
set2 = set((1, 3, 4, 5, 7))
print(set2)
print(set1 & set2)
print(set1 | set2)
set1.add(9)
set2.add(8)
set2.add(6)
print(set2)
set2.pop()      #删除第一个元素
set2.pop()
set2.remove(8)
print(set2)
#set2.clear()       #清除整个集合
#print(set2)

#t1 = (9, 10, 11, [12, 14])      #set中只能放入不可变对象，list是可变对象，会报错
t1 = (9, 10, 11)
set2.add(t1)
print(set2)

#当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
# 相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了.
# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
a = 'abc'
print(a.replace('a', 'A'))
print(a)








