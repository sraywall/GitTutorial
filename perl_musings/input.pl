#!/usr/bin/perl
use v5.22;
use Getopt::Long;

my $data = "file.dat";
my $length = 24;
my $verbose;
GetOptions("length=i" => \$length, # numeric
    "file=s" => \$data,             # string
    "verbose" => \$verbose)         # flag
    or die ("Error in command line arguments\n");

#while(<STDIN>){
#   print "I saw $_";
#}

#while(defined($line = <STDIN>)){
#   print "I saw $line"
#}

#while(defined($line = <>)){
#    chomp($line);
#    print "It was $line that I saw!\n";
#}

#while(defined(my $line = <<>>)){
#    chomp($line);
#    print "It was $line that I saw!\n";
#}

