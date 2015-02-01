best-rational-approximation
=============================

This package contains algorithms to find the best rational
approximation to a given floating-point number and to find the gcd and
lcm of a given list of floating-point numbers.

## BEST RATIONAL APPROXIMATION PROBLEM

A fraction n/d, where d is at most a given limit l, is the best
rational approximation to a target real number t if the absolute
difference (the absolute error) between n/d and t is the smallest
among all the fractions each of whose denominator is at most l.

Since this is a well-known problem in mathematics, I will give more
details. The best sources are already available on the Web.

## ALGORITHMS FOR BEST RATIONAL APPROXIMATION

I give the implementations of three algorithms for best rational
approximation in three different Python programs:
- 'ad_rat_by_cont_frac.py': Algorithm using continued fractions.
- 'ad_rat_by_farey.py': Algorithm using the Farey sequence.
- 'ad_rat_by_fast_farey.py': Faster algorithm using the Farey sequence.

The algorithm in 'ad_rat_by_cont_frac.py' is not difficult to design
from scratch but my implementation is based closely on an
implementation by D. Eppstein of Universite of California, Irvine.

I designed the other two algorithms: The algorithm using the Farey
sequence is simple but is definitely not trivial. For example, the
implementation in [4] (one of the top results to a google search on
'best rational approximation' and implemented by John D. Cook) does
not work correctly in all cases, e.g., it fails to find the best
rational approximation n/d to pi when d is upper-bounded by 100.

The faster algorithm using the Farey sequence reduces the number of
iterations drastically (except when running for the golden ratio as
the target) but all algorithms work fast enough for denominator limits
up to one million and potentially even beyond. Later I will implement
and post the other faster algorithms using the Farey sequence: Two are
given in [2] and [3].

One caveat to note is that real numbers are represented in computers
as floating-point numbers. Beyond the binary representation issues,
floating-point numbers are basically rational numbers. In other words,
any implementation of these or similar algorithms actually finds the
best rational approximation (i.e., as a rational number with a bounded
denominator) to a given rational number. As an example, 'bc' returns
3.14159265358979323844 as pi (computed as '4*a(1)'). As a rational
number, we can view this approximation as 314159265358979323844/1e+20
or approximate it to 22/7, which is the best rational approximation to
pi when the denominator is limited by 10.

## HOW TO RUN

Each of the three programs take the same arguments and return the
output in the same format. For 'ad_rat_by_farey.py', the usage is
shown below.

```
ad_rat_by_farey.py 
   -h/--help 
  [-e/--error=float>=0] 
   -l/--limit=int=>1 
   -t/--target=float or quoted math expr returning float
```

To find the best rational approximation n/d to a target floating-point
number t, these programs always need a limit on d. In addition, an
upper bound on the absolute error, an optional parameter, can also be
input.

Here is how the output from a typical run looks like:

```
> ad_rat_by_farey.py -l 10 -t pi
target= 3.141593 best_rat= 22 / 7 max_denom= 10 err= -0.00126449 abs_err= 0.00126449 niter= 8
```

Here we run 'ad_ray_by_farey.py' to find the best rational
approximation n/d to pi where d is at most 10. The program returns
22/7 as the best approximation in 8 iterations (of a loop that the
algorithm contains). The absolute error is close to 1e-3.

A potentially interesting part of these programs is that these
programs can also accept a math expression that returns a float. The
expression must be enclosed in single or double quores. For example,
here is how to find the best rational approximation to the golden
ratio:

```
> ad_rat_by_farey.py -l 10 -t '(1+sqrt(5))/2'
target= 1.618034 best_rat= 13 / 8 max_denom= 10 err= -0.00696601 abs_err= 0.00696601 niter= 5
```

This output states that the best rational approximation to the golden
ratio is 13/8 with an absolute error close to 1e-2.

These programs still run very fast for very large limits.

## HOW TO TEST

Type 'utest.sh'.

## HOW TO COMPUTE GCD AND LCM OF A LIST OF FLOATING-POINT NUMBERS

A related problem to the best rational approximation problem is
computing the greated common divisor (gcd) and least common multiple
(lcm) of a given list of floating-point numbers (or real numbers). A
solution to this problem can be given using the best rational
approximation algorithms. The solution has two main steps: (1) finding
the best rational approximation to each number in the input list; (2)
computing the gcd and lcm of the resulting rational numbers. Note that
the gcd and lcm of rational numbers are well-defined (as in the case
for integers).

The program 'ad_gcd_lcm.py' solves this problem. Without a proof, I
cannot claim that this is the best solution to this problem but it
works very well for all the cases I could consider and also find on
the Web.

Here is how to run 'ad_gcd_lcm.py':

```
ad_gcd_lcm.py 
   -l/--limit=int>=1 
   -n/--nums=quoted list of at least 2 numbers or math expression returning float (w/o spaces)
```

This program takes in a limit on the largest denominator of any best
rational approximation to any of the numbers in the list.

Here is a run with a verbose output:

```
> ad_gcd_lcm.py -l 10 -n 'pi 2*pi 3*pi'
input: ['pi', '2*pi', '3*pi']
input evaluated: [3.1415926535897931, 6.2831853071795862, 9.4247779607693793]
best_rats= [22/7, 44/7, 66/7]
gcd: rat= 22 / 7 val= 3.14286
lcm: rat= 132 / 7 val= 18.8571 lcm/gcd= 6
nums_div_gcd=  [1, 2, 3] max_err= 0.00120701
lcm_div_nums=  [6, 3, 2] max_err= 0.002415

```

We run 'ad_gcd_lcm.py' for the first three multiples of pi. The
expected result is that the gcd should be equal to pi and the lcm
should be equal to 6 times pi. The program correctly outputs these
expected values.

'utest.sh' tests this program too.

## REFERENCE

[1] R.L. Graham, D.E. Knuth, and O. Patashnik, Concrete Mathematics,
2nd Edition, Addison-Wesley Longman, 1994.

[2] J. Spanier and K.B. Oldham, An Atlas of Functions,
Springer-Verlag, 1987, pp. 665-7.

[3] M. Forisek, Approximating Rational Numbers by Fractions, in Fun
with Algorithms: LNCS, Springer-Verlag, v. 4475, pp. 156-165, 2007.

[4] URL:http://www.johndcook.com/blog/2010/10/20/best-rational-approximation/.


