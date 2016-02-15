# -*- coding: utf-8 -*-
# !/usr/bin/python
################################### PART0 DESCRIPTION #################################
# Filename: test_gevent.py
# Description:
#


# Author: Shuai Yuan
# E-mail: ysh329@sina.com
# Create: 22016-02-15 20:54:00
# Last:
__author__ = 'yuens'

################################### PART1 IMPORT ######################################


################################### PART2 CLASS && FUNCTION ###########################
from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()