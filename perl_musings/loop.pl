#!/usr/bin/perl

use v5.10;
use v5.12; # loads strict for you
use strict;

foreach my $rock (qw/ bedrock slate lava/){
    say "One rock is $rock"; # prints names of three rocks
}
