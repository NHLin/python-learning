#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#from numpy.core import double
import math

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


#函数
print(abs(-2))
print(abs(100))
print(abs(1.2))
# abs('a')       #bad operand type for abs(): 'str'

a = max(1, 2, 3, 4, 5, 6)
print(a)

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = max
print(a(1, 3, 4))

#数据类型转换函数
print(int(2.3))
print(float(3))
print(str(100))
print(bool(1))
print(bool(0))

def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-2))
print(my_abs(0))
print(my_abs(3))

def nop():
    pass

#abs('a')
#my_abs('a')

print(math.pi)
#函数可以同时返回多个值，但其实就是一个tuple

#求解一元二次方程
def quadratic(a, b, c):
    x = -b/(2*a)
    y = math.sqrt(b*b - 4*a*c)/(2*a)
    return x+y,x-y

r = quadratic(2, 3, 1)
print(r)

print(quadratic(1, 3, -4))

str = '中华人民共和国'
print(ascii(str))
str = 'abc'
print(ascii(str))

def power(x, n = 2):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum

print(power(5, 1))
print(power(5, 3))
print(power(6))

def register(name, gender, age = 6, city = 'BeiJing'):
    print('name =', name)
    print('gender =', gender)
    print('age =', age)
    print('city =', city)

register('Jim', 'Male')
register('Tom', 'F', 7)
register('Sam', 'F', city = 'Tianjin')

def add_end(L = []):
    L.append('end')
    return  L

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
print(add_end())
print(add_end())

def add_end(L = None):
    if L is None:
        L = []
    L.append('end')
    return L

print(add_end())
print(add_end())

#可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#print(calc((1,2,3,4)))

print(calc(1,2,3,4))

#*nums表示把nums这个list的所有元素作为可变参数传进去
l = [2, 3, 4, 5]
print(calc(*l))

#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    if 'city' in kw:
        #print(kw['city'])
        str = kw['city'].replace('B', 'b')
        print(str)
    if 'sex' in kw:
        #print(kw['sex'])
        str = kw['sex'].replace('M', 'm')
        print(str)
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)

person('Jim', 25, city = 'BeiJing')

person('Tom', 17, tel = '123456', sex = 'Female')

dict = {'city' : 'Beijing', 'sex' : 'Male', 'Tel' : '123456'}       #键和值之间用冒号
person('Sam', 28, city = dict['city'], sex = dict['sex'], Tel = dict['Tel'])

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
person('Jim', 19, **dict)

#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)

person('xaoming', 31, city = 'Chengdu', job = 'Enginner')       #调用时必须传入关键字参数

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city = 'Beijing', job = 'farmer'):
    print(name, age, city, job)
    print(args)

l = ['english', 'chinese', 'math']
person('xiaohong', 29, *l, city = 'Hangzhou', job = 'teacher')
person('xiaodong', '31', *l)

#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

