def main():
    file = open("input_day9.txt")

    grid = gridmaker()

    head = Player(grid[500][500])
    for line in file:
        line = line.strip().split()
        head.move(translator(line[0]), int(line[1]))
    
    head.tail = list(dict.fromkeys(head.tail))
    print()
    print("done")
    print("len: ", len(head.tail))
        

def gridmaker():
    grid = []
    for y in range(1000):
        row = []
        for x in range(1000):
            cell = (Cell(x, y))
            row.append(cell)
            if x > 0:
                if y > 0:
                    cell.neighborN = grid[y-1][x]
                    grid[y-1][x].neighborS = cell

                cell.neighborW = row[x-1]
                row[x-1].neighborE = cell
            else: 
                if y > 0:
                    cell.neighborN = grid[y-1][x]
                    grid[y-1][x].neighborS = cell



        grid.append(row)
    return grid

def translator(letter):
    if letter == "L":
        result = 2
    elif letter == "R":
        result = 3
    elif letter == "U":
        result = 0
    else:
        result = 1
    return result


class Cell: 
    def __init__(self, x, y):
        self.coordinate = [x, y]
        self.neighborN = ""
        self.neighborS = ""
        self.neighborE = ""
        self.neighborW = ""
    
    def __str__(self):
        return "."




class Player:
    def __init__(self, start):
        self.position = start
        self.last = None
        self.tail = [start]

    def move(self, direction, steps):
        tailcell = self.tail[-1]
        for i in range(steps):
            neighbors = [self.position.neighborN, self.position.neighborS, self.position.neighborW, self.position.neighborE]
            self.last = self.position
            self.position = neighbors[direction]
            hx = self.position.coordinate[0]
            hy = self.position.coordinate[1]
            tx = tailcell.coordinate[0]
            ty = tailcell.coordinate[1]
            if (abs(hx - tx) > 1 or abs(hy - ty) > 1):
                tailcell = self.last
                self.tail.append(tailcell)
                

main()