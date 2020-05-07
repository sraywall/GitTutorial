#!/usr/bin/perl

use v5.10;

my @names = qw (fred barney betty dino wilma pebbles bamm-bamm);
my $result = &which_element_is("dino", @names);
say "\$result is: $result";

sub which_element_is{
    my($what, @array) = @_;
    foreach (0 ..$#array){
        if ($what eq $array[$_]){
            return $_; # return early once found
        }
    }
    -1;
}

print "Enter a word to search for: ";
chomp(my $input = <STDIN>);

say "$input is located at ",which_element_is($input,@names);

