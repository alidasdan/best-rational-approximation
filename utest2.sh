#!/bin/bash

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
