#!/usr/bin/perl
# kprobs.pl, calculate exact probabilities for Kilodeck
# Ron Hale-Evans, rwhe@ludism.org

for ($c = 2; $c <= 20; $c++)
{
  $base = (2/(2**$c));

  $expected = $base*10;

  $probability = 1 - (1 - $base)**10;

  $score = 1/$probability;

  $probability*= 100;

  print "$c cards:\n";
  print "  Expected number of common attributes = $expected\n";
  print "  Probability of at least 1 common attribute = $probability%\n";
  print "  Recommended score = $score\n";
}
