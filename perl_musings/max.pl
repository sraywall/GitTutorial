#!/usr/bin/perl

use v5.10;
sub max {
    my(@input) = @_; # the first one is the largest yet seen
    foreach (@input){
        if ($_ > $max_so_far){
            $max_so_far = $_;
        }
    }
    $max_so_far;
}

say "Enter some numbers:";

chomp(@nums = <STDIN>);

@nums = sort {$a < $b} @nums;
say "Numbers are: ", join (" ", @nums);

say "max: ",max(@nums);
