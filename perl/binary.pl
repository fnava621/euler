use strict;
use warnings;

my $num = 37;


sub binary { 
    my ($n) = @_;
    
    return $n if $n == 0 || $n == 1;

    my $k = int($n/2);

