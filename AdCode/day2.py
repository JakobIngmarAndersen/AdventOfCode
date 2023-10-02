def main():
    file = open("input_day2.txt", "r")
    playerlist = [Player(), Player(), Player()]
    for line in file:
        x = line.split()
        y = [Movemaker(x[0]), Movemaker(x[1])]
        battle(y[0], y[1], playerlist)
    print(playerlist[0].points, playerlist[1].points, playerlist[2].points)

def battle(p0m, p1m, players):
    if p1m.tag == "X":
        players[2].lose(Movemaker(p0m.beats))
    elif p1m.tag == "Y":
        players[2].draw(p0m)
    else:
        players[2].win(Movemaker(p0m.loses))

    if p0m.tag == p1m.tag:
        players[0].draw(p0m)
        players[1].draw(p1m)
    else: 
        if p0m.beats == p1m.tag:
            players[0].win(p0m)
            players[1].lose(p1m)
        else:
            players[0].lose(p0m)
            players[1].win(p1m)


class Player: 
    def __init__(self):
        self.points = 0
    
    def lose(self, move):
        self.points += move.points

    def draw(self, move):
        self.points += 3
        self.points += move.points

    def win(self, move):
        self.points += 6
        self.points += move.points

def Movemaker(letter):
    if letter == "A" or letter == "X":
        return Rock()
    elif letter == "B" or letter == "Y":
        return Paper()
    else: 
        return Scissor()



class Rock:
    def __init__(self):
        self.points = 1
        self.tag = "X"
        self.beats = "Z"
        self.loses = "Y"

class Paper: 
    def __init__(self):
        self.points = 2
        self.tag = "Y"
        self.beats = "X"
        self.loses = "Z"

class Scissor:
    def __init__(self):
        self.points = 3
        self.tag = "Z"
        self.beats = "Y"
        self.loses = "X"

main()