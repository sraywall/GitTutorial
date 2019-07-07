class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

killing_in_the_name_of = Song(["Fuck you, I won't do what you tell me\n"*16,"Motherfucker!"])

killing_in_the_name_of.sing_me_a_song()

lyrics = ["I'm free to speak my mind anywhere","And I'll redefine anywhere"]

wherever_I_may_roam = Song(lyrics)

wherever_I_may_roam.sing_me_a_song()
