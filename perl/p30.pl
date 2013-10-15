use strict;
use warnings;
use 5.010;

sub digit_fifth_powers {

    my @numbers= ();
    foreach (2..1000000){
        my @ary_nums = split(//, $_);
        my $fifth_power = 0;
        foreach my $ind_num (@ary_nums){
            $fifth_power += $ind_num**5;
        }
        if ($fifth_power == $_){
            push(@numbers, $fifth_power)
        }
    }
    return @numbers;
}



my $sum = 0;

foreach (digit_fifth_powers()){
    $sum += $_;
}

say $sum
