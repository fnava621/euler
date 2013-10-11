use 5.010;
use strict;
use bigint;

=begin comment

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

=cut 


sub p16 {
    my $y = 2**1000;
    my $sum = 0;
    foreach (split(//, $y)){
        $sum += $_;
    }

    return $sum;
}
        

say p16();
