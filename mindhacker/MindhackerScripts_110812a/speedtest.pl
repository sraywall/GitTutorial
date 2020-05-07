#!/usr/bin/perl
use v5.10;

open FILE ,"+<", shift @ARGV;
while(<FILE>){
    /(.*)\t(.*)\t(.*)\t(.*)\t(.*)/;
    print $_;
    if (!$5){
        print "$1: ";
        $starttime = `date +%s%N`;
        chop($a = <STDIN>);
        $endtime = `date +%s%N`;
        $time = (($endtime - $starttime)/1_000_000_000)."s";
        if ($a == $2){
            say "Correct!";
            my $temp = $3 + 1;
            s/(.*)\t(.*)\t(.*)\t(.*)\t(.*)/$1\t$2\t$temp\t$4\t$5/g;
        }else {
            print "Wrong! ";
            say "$2";
            <STDIN>;
        }
    }
    system("clear");
}
