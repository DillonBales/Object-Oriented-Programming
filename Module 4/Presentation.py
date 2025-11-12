class Electronic:
    def turn_on(self):
        print("Powering on")

    def turn_off(self):
        print("Powering off")

class Television(Electronic):
    def change_channel(self):
        print("Changing channel")

class Mp3_player(Electronic):
    def next_song(self):
        print("Skipping song")

Tv = Television()
iPod = Mp3_player()


Tv.turn_on()
Tv.change_channel()

iPod.turn_on()
iPod.next_song()

Tv.turn_off()
iPod.turn_off()
