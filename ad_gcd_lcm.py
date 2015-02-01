#!/usr/bin/python

# find the gcd and lcm of a given list of floating-point numbers. this
# code uses a best rational approximation algorithm to solve the
# problem in two steps: find the best rational approximation to each
# number in the input list; compute the gcd and lcm of the resulting
# rational numbers.

# author: ali dasdan

import sys
import getopt
import re
from math import *
from ad_rat_by_fast_farey import *

def show_usage():
    print "Usage:  " + sys.argv[0] + " -l/--limit=int>=1 -n/--nums=quoted list of at least 2 numbers or math expression returning float (w/o spaces)"

def at_exit(msg):
    if msg != '' and msg != None:
        print "Error:", msg
    show_usage()
    sys.exit(0)

def igcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def ilcm(a, b):
    return int((a * b) / igcd(a, b))

def isimplify(a, b):
    g = igcd(a, b)
    return int(a / g), int(b / g)

def rgcd(n1, d1, n2, d2):
    # simplify n1/d1 and n2/d2
    a, b = n1, d1
    n1, d1 = isimplify(a, b)
    a, b = n2, d2
    n2, d2 = isimplify(a, b)
    # compute n/d = gcd(n1, n2) / lcm(d1, d2)
    n = igcd(n1, n2)
    d = ilcm(d1, d2)
    return n, d

def rlcm(n1, d1, n2, d2):
    # simplify n1/d1 and n2/d2
    a, b = n1, d1
    n1, d1 = isimplify(a, b)
    a, b = n2, d2
    n2, d2 = isimplify(a, b)
    # compute n/d = lcm(n1, n2) / gcd(d1, d2)
    n = ilcm(n1, n2)
    d = igcd(d1, d2)
    return n, d

def rgcd_lst(ns, ds):
    assert len(ns) == len(ds)
    n_gcd = ns[0]
    d_gcd = ds[0]
    for n, d in zip(ns[1:], ds[1:]):
        a, b = n_gcd, d_gcd
        n_gcd, d_gcd = rgcd(a, b, n, d)
    return n_gcd, d_gcd

def rlcm_lst(ns, ds):
    assert len(ns) == len(ds)
    n_lcm = ns[0]
    d_lcm = ds[0]
    for n, d in zip(ns[1:], ds[1:]):
        a, b = n_lcm, d_lcm
        n_lcm, d_lcm = rlcm(a, b, n, d)
    return n_lcm, d_lcm

def main():
    s = None
    l = None
    nums = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'l:n:', ['limit=', '--nums'])
    except getopt.GetoptError, msg:
        at_exit(msg)

    for o, a in opts:
        try:
            if o in ('-n', '--nums'):
                s = str(a)
            elif o in ('-l', '--limit'):
                l = int(a)
                if l < 1: raise Exception()
            else:
                raise Exception()
        except Exception, msg:
            at_exit(msg)

    if s == None:
        at_exit(None)

    # get the list from the input string
    lst = re.split("[\s,;|:]+", s)
    print "input:", lst
    if len(lst) <= 1 or l == None:
        at_exit("Bad args")
    
    # convert each elt of the list to a float string
    nums = []
    for x in lst:
        try:
            nums.append(eval(x))
        except Exception, msg:
            at_exit(msg)

    print "input evaluated:", nums

    # convert to best rational approximations
    ns = []
    ds = []
    for x in nums:
        ignore, n, d, ignore = find_best_rat(l, x)
        ns.append(n)
        ds.append(d)

    rats = []
    for n, d in zip(ns, ds):
        rats.append(str(n) + "/" + str(d))
    srats = ", ".join(rats)
    print "best_rats= [" + srats + "]"

    # compute gcd and lcm of the elts in the list
    n_gcd, d_gcd = rgcd_lst(ns, ds)
    n_lcm, d_lcm = rlcm_lst(ns, ds)
    
    gcd = float(n_gcd) / d_gcd
    lcm = float(n_lcm) / d_lcm

    print("gcd: rat= %d / %d val= %g" % (n_gcd, d_gcd, gcd))    
    print("lcm: rat= %d / %d val= %g lcm/gcd= %g" % (n_lcm, d_lcm, lcm, float(lcm)/gcd))

    # compute the ratios and measure error (difference from the
    # closest int)
    max_err_gcd = 0
    max_err_lcm = 0

    n_div_gcd = []
    lcm_div_n = []
    for x in nums:
        r = float(x) / gcd
        r_int = int(round(r))
        err = abs(r - r_int)
        if err > max_err_gcd:
            max_err_gcd = err
        n_div_gcd.append(r_int)
        r = float(lcm) / x
        r_int = int(round(r))
        err = abs(r - r_int)
        if err > max_err_lcm:
            max_err_lcm = err
        lcm_div_n.append(r_int)

    print "nums_div_gcd= ", n_div_gcd, "max_err= %g" % (max_err_gcd)
    print "lcm_div_nums= ", lcm_div_n, "max_err= %g" % (max_err_lcm)
    
if __name__ == "__main__":
    main()

# EOF
