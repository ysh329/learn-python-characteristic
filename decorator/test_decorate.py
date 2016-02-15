# -*- coding: utf-8 -*-
# !/usr/bin/python
################################### PART0 DESCRIPTION #################################
# Filename: test.py
# Description:
#


# Author: Shuai Yuan
# E-mail: ysh329@sina.com
# Create: 2016-02-14 23:15:46
# Last:
__author__ = 'yuens'

################################### PART1 IMPORT ######################################


################################### PART2 CLASS && FUNCTION ###########################
def log_of_function(undecorated_function):
    def record_start_and_end_log(args, **kw):
        print("Function {0} start.".format(undecorated_function.__name__))
        n = undecorated_function(args, **kw)
        print("Function {0} end.".format(undecorated_function.__name__))
        return n
    return record_start_and_end_log


@log_of_function
def fun_a(n):
    print("This is {0} from function a.".format(n))
    return n

################################### PART3 CLASS TEST ##################################

n = fun_a(11)
print n

# 输出如下：
# Function fun_a start.
# This is 11 from function a.
# Function fun_a end.
# 11