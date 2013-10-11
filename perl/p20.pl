use strict;
use warnings;
use 5.010;
use bigint;


sub factorial_digit_sum { 

    my $val = shift;
    my $prod = 1;

    while ($val >= 1) { 
        $prod *= $val;
        $val -= 1;
    }

    my $ans = 0;
    my @arr = split(//, $prod);

    foreach (@arr){
        $ans += $_;
    }

    return $ans;
}

print "Answer is: ", factorial_digit_sum(100), "\n";
    
