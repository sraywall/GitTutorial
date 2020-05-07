The bonus script in this folder, wakeme, is a "poor coder's Chumby" Internet alarm clock. The Chumby itself is described in Mindhacker Hack 52, "Metabehave Yourself."

Since we wrote Hack 52, our Chumby died, and rather than rely on our spare older model, we decided on a new, more customizable system that runs on Ron's netbook.

You will need to download and install the media player vlc (http://www.videolan.org/vlc/) before you run this script, or else edit the script to use a different player. You'll also need an annoying sound to play in an endless loop if you fail to get up; we use "Reveille".

On a system with a Perl interpreter, typing

  perl wakeme mix 60

will play your personal wake-up music mix on shuffle for 60 minutes before sounding reveille in an endless loop.

Similarly,

  perl wakeme rp 30

will play Radio Paradise (www.radioparadise.com) for half an hour, then a reveille loop. 

We also have a setting for our local public radio station, KUOW. You can customize the script as you see fit, to point to your MP3 hoard and your favorite web radio stations, your favorite wake-up loop, and so on. You could also make it control a LEGO robot or something, but adding URLs is especially easy.

To time and trigger the wakeme script under Linux, we use the excellent KAlarm program (www.astrojar.org.uk/kalarm/). This program enables us to specify the time to wake up. The wakeme script does the rest, playing our music mix or web radio, cutting off our chosen audio after the specified time, and playing the wake-up-for-real! loop.

KAlarm also enables us to listen to music as we go to sleep. We start vlc playing very softly, and reset a standing "command alarm" in KAlarm to about two hours. The command is "killall vlc", and it kills vlc after the specified time. 

You may also need to "killall vlc" if you turn off the alarm before reveille in the morning, or else it will suddenly start blaring while you're checking email and eating your King Vitaman. We have a button on the menu bar that kills vlc with one click.

The final touch is the Linux shell command "xclock -digital -fg green -bg black -brief -face Courier:size=250", which creates a nice big green, glowing clock face on the netbook that's two or three times bigger than a clock radio's. We have a button for this too.

For help, e-mail mindhacker@ludism.org.
