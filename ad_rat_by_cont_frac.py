#!/usr/bin/python

# find the best rational approximation n/d where d <= l to the given
# target number t. here the best means the one with the smallest
# absolute error between t and n/d.

# (based on the original comment by d. eppstein) based on the theory
# of continued fractions, if x = a1 + 1/(a2 + 1/(a3 + 1/(a4 + ...)))
# then the best approximation is found by truncating this series, with
# some adjustments due to l. the fraction can be recovered by the 1st
# column of the matrix:
#   (1 0) (a1 1) (a2 1) (a3 1) ...
#   (0 1) (1  0) (1  0) (1  0)
# instead of keeping the sequence of continuted fraction terms, we
# just keep the last partial product of these matrics.

# author: ali dasdan (based on the C code by d. eppstein)

import sys
import getopt
from math import *

def show_usage():
    print sys.argv[0] + " -h/--help [-e/--error=float>=0] -l/--limit=int>1 -t/--target=float or quoted math expr returning float"

def at_exit(msg):
    if msg != "" and msg != None:
        print "Error:", msg
    show_usage()
    sys.exit(0)

# this function takes in an int limit l and the target fraction to
# approximate t and returns err, n, d, niter where n/d is the
# approximate rational for t, err is the absolute error, and niter is
# the number of iterations of the loop.
def find_best_rat(l, t):
    assert l >= 1

    # handle the odd case
    if t <= 0:
        return 0, t, 1, 0

    # initialize the matrix
    m00, m01 = 1, 0
    m10, m11 = 0, 1
    
    # loop finding terms until denom gets too big
    x = t
    ai = int(x)
    niter = 0
    while (m10 * ai + m11) <= l:
        niter += 1

        # multiply these two matrices:
        #    (m00 m10) and (ai 1)
        #    (m10 m11)     (1  0)
        tmp = m00 * ai + m01
        m01 = m00
        m00 = tmp
        tmp = m10 * ai + m11
        m11 = m10
        m10 = tmp
        if (x == float(ai)): break
        x = float(1.0) / (x - float(ai))
        ai = int(x)

    # now remaining x is between 0 and 1/ai. approx as either o or 1/m
    # where m is max that will fit in l.
    
    # first try zero
    n1 = m00
    d1 = m10
    err1 = abs(t - float(n1) / d1)

    # try the other possibility
    ai = int(float(l - m11) / m10)
    n2 = m00 * ai + m01
    d2 = m10 * ai + m11
    err2 = abs(t - float(n2) / d2)

    if err1 <= err2:
        return err1, n1, d1, niter
    else:
        return err2, n2, d2, niter

# this function takes in an error bound err_in, an int limit l, and
# the target fraction to approximate t and returns err_out, n, d,
# niter where n/d is the approximate rational for t with d<=l, err_out
# is the absolute error that is at most err_in, and niter is the
# number of iterations of the loop. The idea for this function is to
# find the smallest d such that err_out<=err_in.
def find_best_rat_with_err_bound(err_in, l, t):
    l_curr = 1
    sum_niter = 0
    err_out, n, d, niter = find_best_rat(l_curr, t)
    while (err_out > err_in) and (l_curr < l):
        l_curr *= 10
        sum_niter += niter
        err_out, n, d, niter = find_best_rat(l_curr, t)
    return err_out, n, d, sum_niter

def main():
    eps = None
    l = None
    t = None

    # get the arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   'he:l:t:',
                                   ['help', 'error=', 'limit=', 'target='])
    except getopt.GetoptError, msg:
        at_exit(msg)

    for o, a in opts:
        try:
            if o in ('-h', '--help'):
                raise Exception()
            elif o in ('-e', '--error'):
                eps = float(a)
                if eps <= 0: raise Exception()
            elif o in ('-l', '--limit'):
                l = int(a)
                if l < 1: raise Exception()
            elif o in ('-t', '--target'):
                try:
                    t = float(eval(a))
                except Exception, msg:
                    at_exit(msg)
                if t <= 0: raise Exception()
            else:
                raise Exception()
        except Exception, msg:
            at_exit(msg)

    if t == None or l==None:
        at_exit("Target and limit args are required")

    # find the best rational approximation n/d with d<=l and with
    # the min err or the err at most eps.
    if eps == None:
        err, n, d, niter = find_best_rat(l, t)
    else:
        err, n, d, niter = find_best_rat_with_err_bound(eps, l, t)
    err = (t - float(n) / d)
    if eps == None:
        print("target= %f best_rat= %d / %d max_denom= %d err= %g abs_err= %g niter= %d" % (t, n, d, l, err, abs(err), niter))
    else:
        print("target= %f best_rat= %d / %d max_denom= %d err= %g abs_err= %g abs_err/error= %g niter= %d" % (t, n, d, l, err, abs(err), float(abs(err)) / eps, niter))
   
if __name__ == '__main__':
    main()

# EOF
