#!/usr/bin/python

# find the best rational approximation n/d where d <= l to the given
# target number t. here the best means the one with the smallest
# absolute error between t and n/d.

# this code uses the exhaustive search for each potential denominator
# up to and including l.
 
# author: ali dasdan

import sys
import getopt
from math import *

def show_usage():
    print sys.argv[0] + " -h/--help [-e/--error=float>=0] -l/--limit=int=>1 -t/--target=float or quoted math expr returning float"

def at_exit(msg):
    if msg != "" and msg != None:
        print "Error:", msg
    show_usage()
    sys.exit(0)

# this function takes in an int limit l and the target fraction to
# approximate t and returns err, n, d, niter where n/d is the
# approximate rational for t with d<=l, err is the absolute error, and
# niter is the number of iterations of the loop.
def find_best_rat(l, t):
    assert l >= 1 and t <= 1

    # handle the odd case
    if t <= 0:
        return 0, t, 1, 0

    best_err = t
    best_n, best_d = 0, 1
    niter = 0
    for d in range(1, l + 1):
        for n in range(1, l + 1):
            niter += 1

            err = abs(t - float(n) / d)
            if err < best_err:
                best_err = err
                best_n, best_d = n, d
    
    return best_err, best_n, best_d, niter
        
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
    t_frac, t_int = modf(t)
    if eps == None:
        err, n, d, niter = find_best_rat(l, t_frac)
    else:
        err, n, d, niter = find_best_rat_with_err_bound(eps, l, t_frac)
    n += t_int * d
    err = (t - float(n) / d)
    if eps == None:
        print("target= %f best_rat= %d / %d max_denom= %d err= %g abs_err= %g niter= %d" % (t, n, d, l, err, abs(err), niter))
    else:
        print("target= %f best_rat= %d / %d max_denom= %d err= %g abs_err= %g abs_err/error= %g niter= %d" % (t, n, d, l, err, abs(err), float(abs(err)) / eps, niter))
    
if __name__ == '__main__':
    main()

# EOF

