#!/usr/bin/perl

$name=<STDIN>;

chomp $name;

if($name eq "Tim"){
    print "Welcome, Tim!";
} elsif ($name eq "Bob"){
    print "Welcome, Bob!";
} else {
    print "Welcome, stranger!";
}
