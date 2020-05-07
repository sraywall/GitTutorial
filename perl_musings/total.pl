#!/usr/bin/perl
use v5.26;

sub total{
    my $sum;
    foreach my $i (@_){
        $sum += $i;
    }
    $sum;
}


my $fred_total = total(1..1000);
say "The total of 1 to 1000 is $fred_total.";
say "Enter some numbers on separate lines: ";
my $user_total = total(<STDIN>);
say "The total of those numbers is $user_total.";
