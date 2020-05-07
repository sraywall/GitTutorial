#!/usr/bin/perl
use v5.10;

sub greet{
    state @previous;
    my $current;
    $current = shift @_;
    print "Hi $current! ";
    if (@previous){
        say "I've seen: @previous";
    } else {
        say "You are the first one here!";
    }
    push @previous, $current;
}

greet ("Fred");
greet ("Barney");
greet ("Wilma");
greet ("Betty");
