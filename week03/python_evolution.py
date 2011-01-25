# -*- coding: utf-8 -*-
"""Profiling The Evolution of the Python Programmer

Based on the code offered in good humor at
<http://metaleks.net/programming/the-evolution-of-a-python-programmer>.

I thought it would be fun to profile the various approaches to a
factorial implementation offered by Aleks. My attempt below.

I couldn't profile the EXPERT PROGRAMMERS or the Unix Programmer, as I
am missing their external implementations. ;)

According to my results, the first-year Pascal student wins by a thin
margin over the first-year C student.
"""
import sys

import hotshot
import hotshot, hotshot.stats

from cStringIO import StringIO


to_profile = []

profile_times = 100000


def profile(func):
    buffer = StringIO()
    def profile_func():
        stdout = sys.stdout
        stderr = sys.stderr
        sys.stdout = buffer
        sys.stderr = buffer
        for x in xrange(profile_times):
            func()
        sys.stdout = stdout
        sys.stderr = stderr
    to_profile.append((func.__name__, profile_func))
    return func


n = 10


def tailcall(g):
    '''
    Version of tail_recursion decorator using stack-frame inspection.    

    from:
    http://code.activestate.com/recipes/496691-new-tail-recursion-decorator/
    '''
    loc_vars ={"in_loop":False,"cnt":0}
    
    def result(*args, **kwd):
        if not loc_vars["in_loop"]:
            loc_vars["in_loop"] = True
            while 1:            
                tc = g(*args,**kwd)
                try:                    
                    qual, args, kwd = tc
                    if qual == 'continue':
                        continue
                except TypeError:                    
                    loc_vars["in_loop"] = False
                    return tc                                    
        else:
            f = sys._getframe()
            if f.f_back and f.f_back.f_back and \
                  f.f_back.f_back.f_code == f.f_code:
                return ('continue',args, kwd)
            return g(*args,**kwd)
    return result

import math
@profile
def modern():
    print math.factorial(n) 

@profile
def newbie():
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)
    print factorial(n)


@profile
def first_year_pascal():
    def factorial(x):
        result = 1
        i = 2
        while i <= x:
            result = result * i
            i = i + 1
        return result
    print factorial(n)


@profile
def first_year_c():
    def fact(x): #{
        result = i = 1;
        while (i <= x): #{
            result *= i;
            i += 1;
        #}
        return result;
    #}
    print(fact(n))

@profile
def first_year_sicp():
    @tailcall
    def fact(x, acc=1):
        if (x > 1): return (fact((x - 1), (acc * x)))
        else:       return acc
    print(fact(n))

@profile
def first_year_python():
    def Factorial(x):
        res = 1
        for i in xrange(2, x + 1):
            res *= i
        return res
    print Factorial(n)


@profile
def lazy_python_programmer():
    def fact(x):
        return x > 1 and x * fact(x - 1) or 1
    print fact(n)


@profile
def lazier_python_programmer():
    def fact(x):
        return x > 1 and x * fact(x - 1) or 1
    print fact(n)


@profile
def python_expert_programmer():
    fact = lambda x: reduce(int.__mul__, xrange(2, x + 1), 1)
    print fact(n)


@profile
def python_hacker():
    import sys
    @tailcall
    def fact(x, acc=1):
        if x: return fact(x.__sub__(1), acc.__mul__(x))
        return acc
    sys.stdout.write(str(fact(n)) + '\n')


### No c_math implementation!
# @profile
# def expert_programmer():
#     from c_math import fact
#     print fact(n)


### No c_maths implementation!
# @profile
# def british_expert_programmer():
#     from c_maths import fact
#     print fact(n)


@profile
def web_designer():
    def factorial(x):
        #-------------------------------------------------
        #--- Code snippet from The Math Vault          ---
        #--- Calculate factorial (C) Arthur Smith 1999 ---
        #-------------------------------------------------
        result = str(1)
        i = 1 #Thanks Adam
        while i <= x:
            #result = result * i  #It's faster to use *=
            #result = str(result * result + i)
               #result = int(result *= i) #??????
            result = str(int(result) * i)
            #result = int(str(result) * i)
            i = i + 1
        return result
    print factorial(n)


    
### No factorial implementation!
# @profile
# def unix_programmer():
#     import os
#     def fact(x):
#         os.system('factorial ' + str(x))
#     fact(n)


@profile
def windows_programmer():
    NULL = None
    def CalculateAndPrintFactorialEx(dwNumber,
                                     hOutputDevice,
                                     lpLparam,
                                     lpWparam,
                                     lpsscSecurity,
                                     *dwReserved):
        if lpsscSecurity != NULL:
            return NULL #Not implemented
        dwResult = dwCounter = 1
        while dwCounter <= dwNumber:
            dwResult *= dwCounter
            dwCounter += 1
        hOutputDevice.write(str(dwResult))
        hOutputDevice.write('\n')
        return 1
    import sys
    CalculateAndPrintFactorialEx(6, sys.stdout, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)


@profile
def enterprise_programmer():
    def new(cls, *args, **kwargs):
        return cls(*args, **kwargs)
     
    class Number(object):
        pass
     
    class IntegralNumber(int, Number):
        def toInt(self):
            return new (int, self)
     
    class InternalBase(object):
        def __init__(self, base):
            self.base = base.toInt()
     
        def getBase(self):
            return new (IntegralNumber, self.base)
     
    class MathematicsSystem(object):
        def __init__(self, ibase):
            Abstract
     
        @classmethod
        def getInstance(cls, ibase):
            try:
                cls.__instance
            except AttributeError:
                cls.__instance = new (cls, ibase)
            return cls.__instance
     
    class StandardMathematicsSystem(MathematicsSystem):
        def __init__(self, ibase):
            if ibase.getBase() != new (IntegralNumber, 2):
                raise NotImplementedError
            self.base = ibase.getBase()
     
        def calculateFactorial(self, target):
            result = new (IntegralNumber, 1)
            i = new (IntegralNumber, 2)
            while i <= target:
                result = result * i
                i = i + new (IntegralNumber, 1)
            return result
     
    print StandardMathematicsSystem.getInstance(new (InternalBase, new (IntegralNumber, 2))).calculateFactorial(new (IntegralNumber, 6))


if __name__ == "__main__":
    for name, func in to_profile:
        print '=' * 20, name
        prof = hotshot.Profile("quick_%s.prof" % name)
        prof.runcall(func)
        prof.close()
        stats = hotshot.stats.load("quick_%s.prof" % name)
        stats.strip_dirs()
        stats.sort_stats('time', 'calls')
        stats.print_stats(20)
