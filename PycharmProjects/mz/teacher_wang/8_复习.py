#coding=utf-8

# 数据类型
# 可变：列表和字典 、set    不可变：int str float tuple
# 无序：set   字典的key
# type  isinstance():true   false

# 列表的方法
# 增加：insert  append  extend  +
# 删除：pop  del remove clear
# 排序：sort  sort(reverse=True)   reverser()
# 其它方法：count  len   index  max   min

# 字典
# get setdefault   update keys  values items
# pop  popitems  del

# 字符串：
# startswich()  endswich()  find() rfind()  replace() index()
# split()  join() isdigit() isalpha() isalnum() isspace() format() center()
a = {"aa","b","kk"}
print("*".join(a))

# 运算符
# 算术运算符
# + - * / // %

# 逻辑运算符
# not and or

# 比较运算符
# >  >=  < <=

# 成员运算符
# in  not in

# 身份运算符
# is is not
# 整数：[-5,256]
# is = 和==的区别：
# is:比较两个对象是否一致

# ==============================================

# 条件：
# if .. elif .. else

# 循环：
# while  for

# break：结束循环  continue：结束本次循环,继续执行下一次循环 return：结束函数,并将表达式返回给调用方  pass：占位符
# yield：暂停函数，使用next/for循环拿到返回值 的区别
# ("大于" if (a>b) else "小于" )

# 函数：
# 参数：
# 必须参数：
# 关键字参数：
# 默认参数：
# 不定长参数：*:元组类型    **:字典类型


# 模块：
"""
# 1.import 文件名  as  别名   调用：文件名.函数名()
# 2.from 文件名 import *   调用：函数名()
# 3.from 文件名 import 函数名 as 别名  调用：函数名()

global     locals()的区别：
global 变量名:修改作用域     globals()["变量名"]=值：就是修改全局变量的值的
locals():以字典的形式输出


def func(a,b):
	print(locals())

c = 100
globals()["c"]="200"
print(c)
func(99,12)
print(c)

__name__=="__main__":不让第三方看见调用结果
"""

# 文件
r"""
1.f=open("文件名","模式",encoding="utf8")
3.关闭文件：f.close()
# 写：write()
# 读：read(num):默认读全部,也可以根据字节读取内容    
	readline():一行一行读
	readlines():以列表的方式读取内容，以\n作为一个字符串读取内容
# tell():定位     seek():  0:从头开始    1：当前   2:文件末尾进行偏移
# os模块里的方法：rename()  mkdir():文件夹  rmdir():删除文件夹  remove():删除文件  listdir()  getcwd()  getchdir()

# 2.批量修改文件名:
# 3.拷贝文件并命名：

# 升级版写法：
with open("文件名","模式",endcoding="utf8") as file:
	pass

例子：with open(r"C:\Users\wsy\Desktop\123.txt","r",encoding="utf8") as file:
		a = file.readlines()
		print(a)
"""


# 异常：
"""
try:
	会发生异常的代码
	# 自定义异常
	raise Exception("一组信息")
except Exception as e:
	print(e)
else:
	没有异常时
finally:
	无论是否有错,都会执行
	
	
举例5种错误的异常：
下去整理。。。。。


# 自定义一个异常类(Exception)====下去重点看看
"""

# 面向对象：
"""
1.面向对象和面向过程
2.面向对象的三大组成：
类 属性 方法
3.对象分为：类对象和实例对象
4.属性：
公有和私有属性：
公有：      私有：只能在方法内访问
类属性：调用：在三种方法都能调用：                        实例属性：只能通过实例对象调用

5.方法的区别：
(1).内置方法：__init__():构造器方法,创建对象默认调用  
            __del__():析构方法 ,手动调用：del 实例对象；对象.__del__()    2.通过垃圾回收机制,程序结束前最后默认调用析构方法
            __new__():分配空间,返回引用    重写__new__方法，使用return super().__new__(cls)  
(2).自定义方法：
# 从写法====调用类属性====在类外放调用方法
1.实例方法：必须参数self 调用。。。
2.类方法：装饰器@classmethod() ,调用。。。
3.静态方法：装饰器@staticmethod()  调用。。。

6.继承：
继承分为单继承和多继承：
# 1.调用父类方法：
(1).self.方法名()
(2).父类.方法名(self,)
(3).super().方法吗名()

2.就近原则和重载

# 创建类属性和实例属性：
在类外创建：
类名.age = 18     =====age就是类属性
实例对象.sex = "男"    ====sex:实例属性
"""

"""
列表推导式：
深浅拷贝：导模块copy    
深拷贝：deepcopy():可变类型进行嵌套，无论修改父/子，都拷贝的是原对象
浅拷贝：copy()；可变类型进行嵌套，修改父元素和深拷贝一样，修改子元素，进行更改

# 进程、线程
1.导包：线程：threading
	   进程：multiprocessing
	   
2.生命周期一样，使用start():开启进/线程  ，程序结束之后就死亡
3.join()阻塞
4.语法格式：target=进程/线程函数 ,参数


"""

"""
可迭代对象：(1)有__iter__()方法的对象：/能被for循环遍历的对象，
迭代器：(2)既__next__()和__iter__()，for循环就是一个迭代器
生成器：(3):在程序中有关键yield，暂停程序,通过next()方法返回表达式
"""






