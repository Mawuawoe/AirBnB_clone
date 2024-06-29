#!/usr/bin/python3

"""def my_func(*args):
    print ("hello world {} & {} ".format(args[0], args[1]))

my_func("Desmond", "Dzakago")"""

def my_func(**kwargs):
    for k,v in kwargs.items():
        print ("hello world {}".format(v))

my_func(fristName="Desmond", lastName="Dzakago")