#!/usr/bin/perl -wall
# kdeck.pl, calculate probabilities for Kilodeck with Monte Carlo simulation
# Ron Hale-Evans, rwhe@ludism.org

$deckdimensions = 10;
$decksize = 2**$deckdimensions;

$minhand = 2;
$maxhand = 20;
$testcount = 20000;

for ($handsize=$minhand; $handsize<=$maxhand; $handsize++)
{
  $commontotal = 0;
  $positives = 0;

  for ($test = 1; $test <= $testcount; $test++)
  {
    # Shuffle up a Kilodeck
    for ($i=0; $i<$decksize; $i++)
    {
      $used[$i] = 0;
    }
    for ($i=0; $i<$decksize; $i++)
    {
      do 
      {
        $r = int(rand($decksize));
        if ($used[$r] == 0)
        {
          $deck[$i] = $r;
          $used[$r] = 1;
          # Convert the Kilodeck to binary strings of attributes
          $binattribs[$i] = sprintf "%10.10b",$deck[$i];
        }
      } until ($used[$r] == 1);
    }
  

    # Sum all the bits in one dimension of the hand at a time;
    # the result is an array of sums called $attribsums
    $ncommonattribs = 0;
    for ($d = 0; $d<$deckdimensions; $d++)
    {
      $attribsums[$d] = 0;
      for ($c=0; $c<$handsize; $c++)
      {
        #print "$binattribs[$c]";
        $attribsums[$d] += substr($binattribs[$c],$d,1); 
      }

      # Check whether every card in a hand shares any attributes by
      # comparing the sums to the number of cards in the hand.
      # If they're equal, that attribute is shared by all cards.
      # Also, dimensions that are all 0 are all shared too (duh).
      if (($attribsums[$d] == $handsize) || ($attribsums[$d] == 0))
      {
        $ncommonattribs++;
      }
      #print "N=$ncommonattribs\n";
    }

    # Increment the number of common attributes in this test run by the 
    # number of common attributes in this hand
    $commontotal += $ncommonattribs;

    # If there are any common attributes among all cards, take note of the positive result
    if ($ncommonattribs > 0)
    {
      $positives++;
    }
  }

  # The average number of common attributes in this test run is
  # the number of common attributes in the entire run,
  # divided by the number of tests in this run
  $avg = $commontotal / $testcount;

  # The proportion of positive results (hands with at least some shared attributes)
  # is the number of positive results in this run divided by the number of tests
  $pospercent = 100 * $positives / $testcount;

  $suggscore = int (1 / ($positives / $testcount));

  print "Hand of $handsize cards:";
  print "  Average # of common attributes = $avg";
  print "  Probability they have at least 1 common attribute = $pospercent%";
  print "  Suggested score = $suggscore";
}
