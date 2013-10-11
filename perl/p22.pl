use strict;
use warnings;


=begin comment

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

=cut 

open(NAMES, '<', 'names.txt');

my $names = <NAMES>;

sub zip2 { @_[map { $_, $_ + @_/2 } 0..(@_/2 - 1)] }

my @alphabet = ("A".."Z");

my %hsh = ();

foreach (0..25){
    $hsh{$alphabet[$_]} = (1+$_);
}

my @lst_names = sort(split(/,/, $names));
my $total = 0;

foreach (0..$#lst_names){
    my $sname = 0;
    my @name = split(//, $lst_names[$_]);

    foreach my $letter (@name){
        if ($letter ne '"' and $hsh{$letter}){
            $sname += $hsh{$letter};
        }
    }

    $total += $sname*(1+$_);
}


print "The point total of names.txt is: ", $total, "\n";
    
    
