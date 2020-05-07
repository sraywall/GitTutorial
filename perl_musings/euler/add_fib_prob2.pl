#!/usr/bin/perl 
use v5.10;

sub fib{
    state $prev = 1;
    state $curr = 1;
    ($prev,$curr) = ($curr,$curr+$prev);
    $curr;
}

sub sum{
    my $curr = &fib;
    my $total = 0;
    while ($curr < 4000000){
        if ($curr % 2 == 0){
            $total += $curr;
            say $curr;
        }
        $curr = &fib;
    }
    $total
}

say "The total is:",&sum;
