# -*- coding: utf-8 -*-
# !/usr/bin/python

# This an example of  decorator by Yuens.
# Author: Yuens
# E-mail: ysh329@sina.com
# Date: 2016-02-14 17:09:46

# 下面这是一个壳子（即装饰器）的声明
# 其本质上是函数嵌套
# 只是传入的函数其实就是被装饰的函数
# 我们不关心被装饰的函数，只关心这个壳子
# 即，如何装饰，装饰的方法
def log_decorator(undecorated_function):
    def decorate_with_log(args, **kw):
        print "function start."
        # 因为调用的函数
        # 其输入参数形式是不同的
        # 而且我们这里指明了接收所有的输入参数(args, **kw)
        # 所以在被装饰的函数掉用时，我们无法写成下面这样
        # output(n = 123456)
        # 否则会报错

        # 但如果要被装饰的函数其输入参数的形式（个数）都一样或我们的装饰器只用于装饰一个函数
        # 在调用时，我们可以写下面这样的形式
        # output6(n = 123456)
        # 但在这里，下面这行代码也应该改为
        #undecorated_function(n)
        undecorated_function(args, **kw)
        print "function end."
    return decorate_with_log

# 下面这是装饰器对函数 output6 进行装饰
# 通过这个@符号，其下面默认为被装饰的函数
# 就这么简单，当前这个函数 output6 就被装饰了
# 其调用时，就会打印出我们上面实现的功能
@log_decorator
def output6(n):
    print "n is", n
    #return n

# 上面是壳子（即装饰器）和函数的定义
# 我们现在来调用函数 output6
# 观察输出和我们预想的是否符合
output6(123456)

# python test.py
# 输出如下：
# function start.
# n is 123456
# function end.
