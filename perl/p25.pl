use strict;
use warnings;
use 5.010;
use bigint;

sub fib_1000 {

    my @values = (1,1,2,3,5);
    while (scalar(split(//, $values[-1])) <= 1000){
        $values[scalar(@values)] = $values[-1] + $values[-2];
    }
    return scalar(@values);

}

say fib_1000();
