def main():
    grid = gridmaker("input_day8.txt")  #reads file, sets up grid
    compass(grid)                       #sets neighbors NSEW
    flashlight(grid)                    #sets seen trees to visible
    resulter(grid)                      #reads grid and prints result

def gridmaker(filename):
    file = open(filename)
    grid = []
    for line in file:
        tmp = []
        for char in line.strip(): 
            tmp.append(Tree(int(char)))
        tmp[0].setedge()
        tmp[-1].setedge()
        grid.append(tmp)
    for x in grid[0]:
        x.setedge()
    for y in grid[-1]:
        y.setedge()
    return grid

def compass(grid):
    for i in range(1, (len(grid) - 1)): 
        for q in range(1, (len(grid[i]) - 1)):
            grid[i][q].nsew = [grid[i - 1][q], grid[i + 1][q], grid[i][q + 1], grid[i][q - 1]]    

def flashlight(grid):
    for x in grid:
        for y in x: 
            if not y.edge:
                for i in range(4):
                    if y.getout(i):
                        y.visible = True

def resulter(grid):
    result = 0
    seemost = 0
    for line in grid:
        for tree in line:
            if tree.visible:
                result += 1
            if not tree.edge:
                seedistance = (tree.see[0] * tree.see[1] * tree.see[2] * tree.see[3])
                if seedistance > seemost:
                    seemost = seedistance
    print("Part1: ", result)
    print("Part2: ", seemost)


class Tree:
    def __init__(self, height):
        self.height = height
        self.edge = False
        self.visible = False
        self.nsew = []
        self.see = []
    
    def getout(self, direction):
        tmp = self.nsew[direction]
        x = 1
        while tmp.height < self.height:
            if tmp.edge == True:
                self.see.append(x)
                return True
            else:
                x += 1
                tmp = tmp.nsew[direction]
        self.see.append(x)
        return False
       
    def setedge(self):
        self.edge = True
        self.visible = True
    
    def __repr__(self):
        return str(self.height)

    def __str__(self):
        return str(self.height)

main()

