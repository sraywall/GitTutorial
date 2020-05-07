#!/usr/bin/perl

use v5.26;
use Math::Complex;

sub is_prime{
    state %primes;
    $primes{2} = 1;
    state @primelist;
    push @primelist, 2;
    my $num = shift @_;
    #if known prime 
    if ($primes{$num}){
        return 1;
    }
    #if input divisible by known primes
    for my $p (@primelist) {
        if ($num % $p == 0){
            return 0;
        }
    }
    #generate unknown primes up to sqrt of input
    for my $i ($primelist[$#primelist] .. sqrt($num)){
       my $isprime = 1;
       for my $p (@primelist) {
           if ($i % $p == 0){
               $isprime = 0;
               last;
           }
       }
       if($isprime){# add it to set of primes
           push @primelist, $i;
           $primes{$i} = 1;
           if ($num % $i == 0){ #check if input is divisible
               return 0;
           }
       }
    }
    return 1;
}

sub largest_prime_factor{
    my $num = shift @_;
    if(&is_prime($num)){
        return $num;
    }
    my $max = 0;
    for my $i (2 .. sqrt($num)){
        if($num % $i == 0) {
            if(&is_prime($i)){
                $max = $i;
            }
            my $compliment = $num / $i;
            if(&is_prime($compliment)) {
                return $compliment;
            }
        }
    }
    $max;
}

#for (1..10){
#    say "$_: ",&is_prime($_);
#}
print "Enter a number: ";
chomp(my $input = <STDIN>);
say "$input: ",&largest_prime_factor($input);
#for (1 .. 100){
#    say "$_ ",&largest_prime_factor($_);
#}
