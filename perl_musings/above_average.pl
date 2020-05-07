#!/usr/bin/perl

use v5.26;

sub avg{
    my $total;
    foreach (@_){
        $total += $_;
    }
    $total / @_;
}

sub above_average{
    my $avg = &avg(@_);
    say "the average is $avg";
    grep {$_ >= $avg } @_;
}
my @fred = above_average(1..10);
say "\@fred is @fred";
say "(Should be 6 7 8 9 10)";
my @barney = above_average(100, 1..10);
