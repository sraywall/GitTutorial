#!/usr/bin/perl

for (1..999){
    if ($_ % 3 == 0 or $_ % 5 == 0){
        $total += $_;
    }
}
print $total;
