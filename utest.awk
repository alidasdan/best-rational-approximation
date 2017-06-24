# Awk program called in utest.sh
{
    n2 = $4
    d2 = $6
    s = "program=" p " target=" n "/" d " given=" n2 "/" d2;
    if (n == n2 && d == d2) {
        print "Passed:", s;
    } else {
        print "Failed:", s;
    }
}

# EOF
