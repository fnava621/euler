use 5.010;
use strict;
use Math::Prime::XS qw(is_prime);

=begin comment

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

=cut 

sub prime_factorial {
    my $arg = shift;
    my @result = ();
    my $i = 2;

    while ($i <= $arg){
        if ($arg % $i == 0){
            $arg /= $i;
            if (is_prime($i)) {
                push(@result, $i);
            }
        }
        $i++;
    }
    return @result[-1];
}


say "ANSWER = " . prime_factorial(600851475143);
