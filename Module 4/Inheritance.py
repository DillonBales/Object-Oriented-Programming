#Single inheritence example
class Electronic:
    def turn_on(self):
        print("Powering on")

    def turn_off(self):
        print("Powering off")

class Television(Electronic):
    def change_channel(self):
        print("Changing channel")

Tv = Television()

Tv.turn_on()
Tv.change_channel()

#Multiple Inheritance Example
class Dad:
    def hair_color(self):
        print("I have blonde hair")

class Mom: 
    def eye_color(self):
        print("I have blue eyes")
    
    def talent(self):
        print("I can play the piano")

class Child(Mom, Dad):
    def talent(self):
        print("I can play the guitar")

kid = Child()
kid.eye_color()
kid.hair_color()
kid.talent()

#Multi-level inheritance
class Associate:
    def app_access(self):
        print("Yes")

class Team_Lead(Associate): 
    def radio_access(self):
        print("Yes")

class Coach(Team_Lead):
    def timecard_access(self):
        print("Yes")

associate1 = Associate()
team_lead1 = Team_Lead()
coach1 = Coach()

associate1.app_access()

team_lead1.app_access()
team_lead1.radio_access()

coach1.app_access()
coach1.radio_access()
coach1.timecard_access()

#Hierarchical inheritance example
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
