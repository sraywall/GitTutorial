#!/usr/bin/perl
# met.pl, Mission Elapsed Time clock
# Ron Hale-Evans, rwhe@ludism.org

use Time::HiRes qw(gettimeofday tv_interval);

$t0 = [gettimeofday];
$minute = 60;
$hour = 60 * $minute;
$day = 24 * $hour;

$in_file = $ARGV[0];
open (IN_FILE, "< ./$in_file")
    or die "Couldn't open input file: $!\n";

$i = 0;

while (<IN_FILE>) 
{
    chomp;
    s/(\d\d\d)\/(\d\d)\:(\d\d)\:(\d\d)\,(.*)/{$fdays = $1; $fhours = $2; $fminutes = $3; $fseconds = $4; $objective = $5}/sie;
    $fraw = $fdays * $day + $fhours * $hour + $fminutes * $minute + $fseconds;
    #print "d=$fdays, h=$fhours, m=$fminutes, s=$fseconds, objective = $objective, raw = $fraw\n";

    $rawtimes[$i] = $fraw;
    $objectives[$i] = $objective;
    $i++;
}

$maxraw = $rawtimes[$i-1];

# Clean up.
close IN_FILE;

$objective = "";
$i = 0;

while (true)
{
    $curtime = [gettimeofday];
    $met = tv_interval($t0, $curtime);
    $raw = int($met);

    $met_days = int ($met / $day);
    $met = $met - $met_days * $day;

    $met_hours = int($met / $hour);
    $met = $met - $met_hours * $hour;

    $met_minutes = int($met / $minute);
    $met = $met - $met_minutes * $minute;

    $met_seconds = int($met);
    $met = 0;

    if ($raw >= $rawtimes[$i])
    {
	$objective = $objectives[$i];
	$i++;
    }

    # Clear screen
    system("clear");

    print "MET: ";
    printf ("%03s/%02s:%02s:%02s\n",$met_days, $met_hours, $met_minutes, $met_seconds);
    print "$objective\n";

    if ($raw >= $maxraw)
    {
	exit;
    }
    else
    {
	sleep 1;
    }
}
