# Awk program called in utest.sh
{
    n2 = $3
    d2 = $5
    s = "program=" p " target=" n "/" d " given=" n2 "/" d2;
    if (n == n2 && d == d2) {
        print "Passed:", s;
    } else {
        print "Failed:", s;
    }
}

# EOF
