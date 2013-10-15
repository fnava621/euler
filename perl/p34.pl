use strict;
use warnings;
use 5.010;


sub df {
    sub factorial {
        my $sum = 1;
        my $val = shift;
        while ($val >= 1){
            $sum *= $val;
            $val -= 1;
        }
        return $sum;
    }

    my @fac_sums = ();
    foreach (3..1000000){
        my @nums = split(//, $_);
        my $sum_fact = 0;
        foreach my $ind (@nums){
            $sum_fact += factorial($ind);
        }
        if ($sum_fact == $_){
            push(@fac_sums, $_);
        }
    }
    return @fac_sums;
}

my $result = 0;
foreach (df()){
    $result += $_;
}
    

print "The answer is: ", $result, "\n";
