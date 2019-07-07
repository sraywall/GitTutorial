#!/usr/bin/perl

print "Enter your age: ";

$age=<STDIN>;

chomp $age;

#make sure the user entered a proper age;

while($age < 0){
    print "You can't be that young!\n";
    print "Enter your age: ";
    $age=<STDIN>;
    chomp $age;
}

print "Thank you!\n";
