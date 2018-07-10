__author__ = 'acer'
#-*- coding: utf-8 -*-
#!/usr/bin/
import time

def deco(func):
    print "starttime: %s" % time.time()
    func()
    print "endtime:%s" % time.time()

def deco1(func):
    def wrapper():
        print "starttime: %s" % time.time()
        func()
        print "endtime:%s" % time.time()
    return wrapper

@deco1
def myfunc():
    print "start myfunc"
    print "Test myfunc"
    print "end my func"

def deco2(func):
    def wrapper(a, b, c):
        print "starttime: %s" % time.time()
        func(a, b, c)
        print "endtime:%s" % time.time()
    return wrapper

def deco3(func):
    def wrapper(*args, **kargs):
        print "starttime: %s" % time.time()
        func(*args, **kargs)
        print "endtime:%s" % time.time()
    return wrapper

def deco4(*args0, **kargs0):
    def _deco4(func):
        def wrapper(*args, **kargs):
            print args0[0]
            print kargs0["b"]
            print "starttime: %s" % time.time()
            func(*args, **kargs)
            print "endtime:%s" % time.time()
        return wrapper
    return _deco4

class TestDeco():
    def __init__(self):
        print "init TestDeco"

    def info(self):
        print "Now begin to Test Deco"
    info = classmethod(info)

def deco5(cls):
    def _deco4(func):
        def wrapper(*args, **kargs):
            print "starttime: %s" % time.time()
            print cls.info()
            func(*args, **kargs)
            print "endtime:%s" % time.time()
        return wrapper
    return _deco4

@deco5(TestDeco)
def myfunc1(a, b, c=100):
    print "start myfunc1(a, b )"
    print "a is %s" % a
    print "b is %s" % b
    print "c is %s" % c
    print "end my func1(a, b )"

def main():
    myfunc1(1, 2, c=3)
    #deco(myfunc)
    #myfunc()
    pass
if __name__ == "__main__":
    main()



def use_logging(func):

    def wrapper(*args, **kwargs):
        print "%s is running" % func.__name__