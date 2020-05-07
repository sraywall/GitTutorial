#!/usr/bin/perl

use v5.10;
use strict;

sub marine {
    state $n += 1; # Global variable $n
    say "Hello, sailor number $n";
}

my $fred = 3;
my $barney = 4;
my $wilma = &sum_of_fred_and_barney; # $wilma gets 7
say "\$wilma is $wilma";
sub sum_of_fred_and_barney{
    say "Hey, you called the sum_of_fred_and_barney subroutine!";
    $fred + $barney; # That's the return value
    say "Hey, I'm returning a value now!'"; #Oops!
}

my $betty = 3 * &sum_of_fred_and_barney; #$betty gets 21
print "\$betty is $betty.\n";

sub larger_of_fred_or_barney{
    if ($fred > $barney){
        $fred;
    } else {
        $barney;
    }
}

sub division {
    $_[0] / $_[1];
}

say division 355, 113;

sub chomp {
    say "Munch, munch!";
}
&chomp;

marine;
marine;
marine;
marine;
