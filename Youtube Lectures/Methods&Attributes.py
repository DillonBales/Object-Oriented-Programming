class Tennis_Player:
    
    def __init__(self, name, games, wins):
       #In python instead of calling them "Class Variables" they are called "Attributes"
        self.name = name
        self.games = games
        self.wins = wins
        self.ranking = 1000

       #In python instead of calling them "Class Functions" they are called "Methods"
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Games: {self.games}") 
        print(f"Wins: {self.wins}")
        print(f"Rank: {self.ranking} \n")

    def win(self):
        self.games += 1
        self.wins += 1
        if self.ranking > 5:
            self.ranking -= 5

    def lose(self):
        self.games += 1
        self.ranking += 3

tp1 = Tennis_Player("Andrew" , 35, 33)
tp2 = Tennis_Player("Fred" , 35, 21)

tp1.print_details() #This is a method on an object
tp2.print_details()

tp1.win()
tp2.lose()
tp1.win()
tp2.lose()

tp1.print_details()
tp2.print_details()