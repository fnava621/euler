use strict;
use warnings;
use Math::Prime::XS qw(primes);

=begin comment

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

=cut 


sub p7 { 
    
    my $val = 10_001;
    my @prime_nums = primes($val);

    foreach (@prime_nums){
        print "The following is a prime number: $_ \n";
    }
    
    print "The 10,001 prime number is $prime_nums[-1].\n";
}

p7();
