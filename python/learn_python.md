##Python for循环
for i in range(1,5):
    print i

使用range函数获取序列，返回的是list而不是字典,[1,2,3,4]，默认range步长为1，如果提供第三个参数就是步长。
例如
for i in range(1,5,2):
    print i

for的格式是
for i in range(1,5):
    print i
else:
    print 'Hello' # 这里的else是可选的，在执行完for循环之后会执行一次，除非遇到break。

for i in  range(1,5):等价于 for i in [1,2,3,4]:

break语句用来终止循环。
while True:
    s=raw_input('Enter something:')
    if s=='quit':
        break
    print 'Length of the string is',len(s)
print 'Done'

continue语句用户直接进入下一次循环
while True:
    s=raw_input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        continue
    print 'Input is of sufficient length'


Python通过def定义函数，def是关键字，后面跟函数名称和括号以及括号中的参数
def sayHello():
    print 'Hello world!'

sayHello()

使用函数形参
def printMax(a,b):
    if a>b:
        print a,'is maximum'
    else:
        print b,'is maximum'

printMax(3,4)

###使用局部变量
def func(x):
    print 'x is ',x
    x=2 # 这里的x就是局部变量
    print 'Changed local x to ',x

x=50
func(x)
print 'x is still',x

###global定义一个函数外的变量赋值，告诉python这个不是局部变量而是全局的，使用global完成

def func():
    global x
    print 'x is',x
    x=2 # 这里访问的x实际上是func函数外的函数，这里赋值将会修改func之外的x的值
    print 'changed local x to',x

x=50
func()
print 'Value of x is',x

global语句可以指定多个全局变量global x,y,z

###默认参数值
def say(message,times=1):
    print message* times    # 这种写法会导致message字符串重复times次。

say('Hello')
say('World',5)


### Python的默认参数值只能用于函数列表最后的一个参数

### Python中如果指定某些参数必须设置，这种叫关键参数，我们使用名字而不是位置
def func(a,b=5,c=10):
    print 'a is',a,'and b is',b,'and c is',c

func(3,7)
func(25,c=24)
func(c=50,a=100)

这里我们可以使用k=value的方式对关键字进行赋值

return从函数返回，可以带有返回值，没有返回值的return等价于return None,如果你不在函数末尾增加return，每个函数结尾默认都有return None
def someFunction():
    pass
### pass语句在Python中表示一个空的语句块

### Python有和java一样的文档字符串
def printMax(x,y):
    ''' Prints the maximum of two numbers.
    The two values must be integers.'''
    x=int(x)
    y=int(y)
    if x > y:
        print x,'is maximum'
    else:
        print y,'is maximum'


打印文档字符串的方法
print printMax.__doc__

DocStrings文档字符串也适用于模块和类
__doc__
Python的help()函数实际上就是抓取DocStrings

## Python模块必须使用.py为扩展名
使用sys模块
import sys
sys模块中的argv变量sys.argv变量是一个字符串列表。

import sys仅仅把sys模块引入到程序汇总，使用时还是需要sys.argv这种方式，简化
from sys import argv这样把sys的argv直接引入到程序中，这样程序中直接可以是哦那个argv进行访问。
from sys import *把sys模块下的所有名称都导入到程序中。不推荐这样操作。

模块的__name__，每个模块都有一个名字，
if __name__ == '__main__':  # 这样只有我们的程序是主模块时才会执行，否则不会执行。

每个Python模块都有它的__name__，如果__name__是__main__说明模块被用户单独执行了。

### Python模块十分简单，每个py程序就是一个模块，只要确保有.py扩展名。

#文件命名问mymodule
def sayhi():
    print 'Hi,this is mymodule'
version='0.1'

import mymodule
mymodule.sayhi()
print 'Version', mymodule.version

### Python中模块的名字是文件名决定的。


from mymodule import sayhi,version
sayhi()
print 'Version',version

这里我们把mymodule模块中的sayhi和version直接导入到我们程序的名字空间，就可以直接使用了。

## dir函数，我们可以使用内建的dir函数列出模块定义的标示符（函数、类、变量）
import sys
dir(sys)

import sys
a=sys
del a
dir(a)


### Python数据结构
a)列表list-是一组有序的数据结构，项目之间采用逗号分割。
    方法append添加项目在list尾部
    shoplist=['apple','mango','carrot','banana']
    len(shoplist)
    for item in shoplist:
        print item,
    shoplist.sort() # 排序
    shoplist[1] # 使用下标访问，从0开始
    del shoplist[0] # 删除第一个
b)元组-元组和列表十分类似，但元组的字符串是不能修改的，元组通过圆括号分割，例如print的参数
    zoo=('wolf','elephant','penguin')
    单个元组必须使用如下的表达式，否则python会认为是一个函数调用singleton=(2,)
    元组最常用的方式是打印语句
    age=22
    name='swaroop'
    print '%s is %d years old' %(name,age)
    %这里的是字符串的定制功能。
c)字典-我们把键值联系起来，键必须是唯一的。
    d={key1:value1,key2:value2}
    字典中的键值是没有顺序的，如果要特定顺序你需要自己排序，字典是dict类的实例对象。
    ab={'larry':'larry@wall.org','spammer':'spammer@hotmail.com'}
    for name,address in ab.items():
        print 'Contact %s at %s' % (name,address)
    字典的for循环使用items获取所有的item
    字典也可以使用下标的方式进行访问
    判断字典键值是否存在使用dict的has_key方法

d)序列-元组、列表、字符串都是序列，序列的特点是索引操作符和切片操作符。
    shoplist=['apple','mango','carrot','banana']
    print shoplist[0]
    print shoplist[1:3]
    print shoplist[1:-1]    # 负数表示从末尾开始计算,-1表示会返回除了最后一个项目之外的所有项目切片
    print shoplist[:]   # [:]返回整个序列的拷贝


e)参考

### Python中内建三种数据结构(列表、元组、字典)

### 字符串的操作
help(str)

name='Swaroop'
if name.startswitch('Swar'):
    print 'YES'

delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print delimiter.join(mylist)

if 'a' in name:
    # 检测a是否是name中的一部分

if name.find('war')!=-1:    # 在name中查找war是否存在
    print 'war'

import os
import time

print time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="zip -qr '%s' %s" %(target,' '.join(source))
if os.system(zip_command)==0:
    print 'Successful'
else:
    print 'Backup fail'


if not os.path.exists(today):
    os.mkdir(today)


### tar命令
-c 创建一个归档
-v 交互
-z 表示使用gzip进行压缩或解压
-f 强迫归档，如果存在同名文件替换之
-X 后跟一个文件，这个文件中的文件会被排除不进行归档打包。



### 面向对象的编程
Python的类使用关键字class进行创建
类与普通函数的区别是它的第一个参数永远都是self，这个值会在Python对象创建时提供。
当然你可以可以取名不叫self。

## 创建一个类
class Person:
    pass

p=Person()
print p

## 我们定义一个类，任何成员函数的第一个参数都是self，这个不管你用不用都必须写到函数声明中。


### __init__方法
Python中有很多方法的名字具有特殊意义，例如__init__
__init__方法会在类的一个对象创建时马上运行，你可以用来做一些初始化工作，就如C++的类的构造函数。

class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print 'Hello,my name is',self.name

p=Person('Swaroop') # 构造函数可以带有参数，呵呵！
p.sayHi()


### 类变量有所有类的实例共享使用。
### 对象的变量每个实例有其自己身的拷贝

class Person:
    population=0    # 这个就是类变量，所有实例共享

    def __init__(self,name):
        self.name=name  # 这个就是类变量，每个实例都有其自己的拷贝
        Person.population+=1

    def __del__(self):  # 这个就是析构函数了，每个类被del时会调用。
        print "%s says bye." % self.name
        Person.population-=1

### Python的对象释放是由gc决定的，垃圾回收器.gc释放对象时实际上就是调用__del__这个方法。但你无法控制gc何时来调用，如果要手工释放请使用del p


### 继承，代码重用

class SchoolMember:
    def __init__(self,name,age)
        self.name=name
        self.age=age

    def tell(self):
        print 'Name %s Age:%s' %(self.name,self.age),

class Teacher(SchoolMember):    # 这里表示Teacher继承自SchoolMember
    def __init__(self,name,age,salary): 
        SchoolMember.__init__(self,name,age) # 显示自己调用父类的构造函数
        self.salary=salary

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: %d' % self.salary




### Python文件访问
f=file('poem.txt','w')
f.write('hello')
f.close()

f=file('poem.txt')
while True:
    line=f.raedline()
    if len(line)==0:
        break
    print line,
f.close()


### Python对象的持久化，内置一个标注模块pickle，可以在文件中存储任何Python对象并可以完整无缺的取出来，持久化存储对象
另外还有一个模块cPickle，功能和pickle一样，不过是使用C语言写的，效率比pickle快1000倍。

import cPickle as p  # as的方式是重命名模块，防止名字空间冲突
shoplistfile='shoplist.data'
shoplist=['apple','mango','carrot']

f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

del shoplist

f=file(shoplistfile)
storedlist=p.load(f)
print storedlist



### Python异常处理
try .. except
try .. finally


import sys
try:
    s=raw_input('Enter something --> ')
except EOFError:
    sys.exit()
except: # 如果错误没有被之前的except捕获，那么这里会处理所有的异常
    print 'exception occurred.'

print 'Done'



class ShortInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast


try:
    s=raw_input('Enter something-->')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print 'Why did you do an EOF on me?'
except ShortInputException,x:
    print '%d %d' % (x.length,x.atleast)

else:
    print 'No exception was raised.'

# 自己捕捉自定义的异常


### try..finally无论是否异常都执行某些操作
impor time
try:
    f=file('oem.txt')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()

# 上述程序我们Ctrl-C，我们能看到KeyboardInterrupt异常被触发，但f.close()一样会被调用。

### os模块
os.name 操作系统类型例如nt,posix
os.getcwd 当前工作目录，即Python脚本工作的目录
os.getenv()和os.putenv()设置和读取环境变量
os.listdir() 返回指定目录下的所有文件目录名
os.remove()删除一个文件
os.system()运行系统shell命令
os.linesep() 返回当前平台的行终止符Windows='\r\n',Linux='\n',Mac='\r'
os.path.split()返回一个路径的目录和文件名os.path.split('/home/pi/git.md')[0]是门路究竟,[1]是文件名
os.path.isfile()
os.path.isdir()
os.path.exists()



## Python特殊方法
__init__(self,...)
__del__(self)
__str__(self)
__lt__(self,other)  # 用于排序<操作符调用
__getitem__(self,key)   # 被索引附调用x[key]
__len__(self)   # 内建的len()函数调用

## 单行语句
if flag: print 'YES'

## 列表
listone=[2,3,4]
listtwo=[2*i for i in listone if i >2]  # 递归listone中的所有元素，并如果大于2则进行计算，并复制到新的list中
print listtwo


## 可变变数,当要接收函数接收元组或字典形式是，分别使用*和**前缀
def powersum(power,*args):
由于在args变量前有*前缀，所有多余的函数参数都会被作为一个元组存储在args中，如果使用的是**前缀，则多余的参数被认为是字典的键值对
*args表示所有多余的参数当做一个元组
**args表示多余的参数当做一个字典key:value



## lambda形式
lambda语句被用来创建新的函数对象，并运行时返回他们

def make_repeater(n):   # 运行时创建新的函数对象并返回它
    return lambda s:s*n

twice=make_repeater(2)  # 通过变量条件创造函数，并存储
bigtwice=make_repeater(3) # 再创造一个

print twice('word') # 输出 wordword
print twice(5) # 输出 10

print bigtwice('word')
print bigtwice(6)





lambda语句用来创建函数对象，lambda需要一个参数，后面仅跟单个表达式作为函数体，而表达式的值被这个新建的函数返回。
lambda只能用于表达式，因此print也不能用于lambda中。






