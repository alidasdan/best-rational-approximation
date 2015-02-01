#!/bin/bash

for i in ad_rat_*.py;
do
    # test the best rational approximations to pi
    ./$i -l 1 -t pi | grep best_rat | awk -v p=$i -v n=3 -v d=1 -f utest.awk
    ./$i -l 10 -t pi | grep best_rat | awk -v p=$i -v n=22 -v d=7 -f utest.awk
    ./$i -l 100 -t pi | grep best_rat | awk -v p=$i -v n=311 -v d=99 -f utest.awk
    ./$i -l 1000 -t pi | grep best_rat | awk -v p=$i -v n=355 -v d=113 -f utest.awk
    ./$i -l 10000 -t pi | grep best_rat | awk -v p=$i -v n=355 -v d=113 -f utest.awk
    ./$i -l 100000 -t pi | grep best_rat | awk -v p=$i -v n=312689 -v d=99532 -f utest.awk
    ./$i -l 1000000 -t pi | grep best_rat | awk -v p=$i -v n=3126535 -v d=995207 -f utest.awk

    # test the best rational approximations to e
    ./$i -l 1 -t e | grep best_rat | awk -v p=$i -v n=3 -v d=1 -f utest.awk
    ./$i -l 10 -t e | grep best_rat | awk -v p=$i -v n=19 -v d=7 -f utest.awk
    ./$i -l 100 -t e | grep best_rat | awk -v p=$i -v n=193 -v d=71 -f utest.awk
    ./$i -l 1000 -t e | grep best_rat | awk -v p=$i -v n=1457 -v d=536 -f utest.awk
    ./$i -l 10000 -t e | grep best_rat | awk -v p=$i -v n=25946 -v d=9545 -f utest.awk
    ./$i -l 100000 -t e | grep best_rat | awk -v p=$i -v n=271801 -v d=99990 -f utest.awk
    ./$i -l 1000000 -t e | grep best_rat | awk -v p=$i -v n=1084483 -v d=398959 -f utest.awk

    # test the best rational approximations to the golden ratio
    ./$i -l 1 -t '(1+sqrt(5))/2' | grep best_rat | awk -v p=$i -v n=2 -v d=1 -f utest.awk
    ./$i -l 10 -t '(1+sqrt(5))/2' | grep best_rat | awk -v p=$i -v n=13 -v d=8 -f utest.awk
    ./$i -l 100 -t '(1+sqrt(5))/2' | grep best_rat | awk -v p=$i -v n=144 -v d=89 -f utest.awk
    ./$i -l 1000 -t '(1+sqrt(5))/2' | grep best_rat | awk -v p=$i -v n=1597 -v d=987 -f utest.awk
    ./$i -l 10000 -t '(1+sqrt(5))/2' | grep best_rat | awk -v p=$i -v n=10946 -v d=6765 -f utest.awk
    ./$i -l 100000 -t '(1+sqrt(5))/2' | grep best_rat | awk -v p=$i -v n=121393 -v d=75025 -f utest.awk
    ./$i -l 1000000 -t '(1+sqrt(5))/2' | grep best_rat | awk -v p=$i -v n=1346269 -v d=832040 -f utest.awk
done

# test gcd and lcm computations for a list of floating point numbers
p="ad_gcd_lcm.py"
ad_gcd_lcm.py -l 1000 -n '2 4 6 8' | grep 'gcd:' | awk -v p=$p -v n=2 -v d=1 -f utest2.awk
ad_gcd_lcm.py -l 1000 -n 'pi 2*pi 3*pi 4*pi' | grep 'gcd:' | awk -v p=$p -v n=355 -v d=113 -f utest2.awk
ad_gcd_lcm.py -l 1000 -n '2.4 1.2 3.6' | grep 'gcd:' | awk -v p=$p -v n=6 -v d=5 -f utest2.awk
ad_gcd_lcm.py -l 1000 -n 'pi e (1+sqrt(5))/2' | grep 'gcd:' | awk -v p=$p -v n=1 -v d=59780616 -f utest2.awk

p="ad_gcd_lcm.py"
ad_gcd_lcm.py -l 1000 -n '2 4 6 8' | grep 'lcm:' | awk -v p=$p -v n=24 -v d=1 -f utest2.awk
ad_gcd_lcm.py -l 1000 -n 'pi 2*pi 3*pi 4*pi' | grep 'lcm:' | awk -v p=$p -v n=4260 -v d=113 -f utest2.awk
ad_gcd_lcm.py -l 1000 -n '2.4 1.2 3.6' | grep 'lcm:' | awk -v p=$p -v n=36 -v d=5 -f utest2.awk
ad_gcd_lcm.py -l 1000 -n 'pi e (1+sqrt(5))/2' | grep 'lcm:' | awk -v p=$p -v n=826024295 -v d=1 -f utest2.awk

# EOF
