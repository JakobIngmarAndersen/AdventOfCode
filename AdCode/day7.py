
def main():
    file = open("input_day7.txt")
    comp = Directory("GOD", None)
    myComputer = Directory("/", comp)
    file.readline()
    activedir = myComputer
    for line in file:
        activedir = recurser(line.strip().split(" "), activedir)
    fullsize = downlow(myComputer)
    print(fullsize)

    resultlist = biglister(myComputer)
    result = 0
    print()
    print()
    for k in resultlist:
        print(k)
        result += k[1]
    print(result)

    print()
    print(myComputer.accsize)
    print()
    thisguy = Holderboy()
    downlow2(myComputer, thisguy)
    kuk = 9999999999
    for x in thisguy.hold:
        if x[1] < kuk:
            kuk = x[1]
    print(kuk)
    
    print(thisguy.hold)
    
def biglister(directory):
    resultlist = []
    if directory.dirs:
        for dict in directory.dirs:
            if directory.dirs[dict].accsize <= 100000 and directory.dirs[dict].accsize != 0:
                resultlist.append([directory.dirs[dict].tag, directory.dirs[dict].accsize])
            if directory.dirs[dict].dirs:
                x = biglister(directory.dirs[dict])
                for y in x:
                    resultlist.append(y)
        return resultlist

def recurser(line, directory):
    if line[0] != "$":
        directory.handler(line)
        return directory
    return directory.command(line[1:])


def downlow(directory):
    for dict in directory.dirs:
        newval = downlow(directory.dirs[dict])
        directory.accsize += newval
    return directory.accsize   

def downlow2(directory, holder):
    if directory.accsize >= 2558312:
        q = []
        for x in directory.dirs.keys():
            q.append([directory.dirs[x].tag, directory.dirs[x].accsize])
        holder.hold.append([directory.tag, directory.accsize])
        for x in directory.dirs.keys():
            downlow2(directory.dirs[x], holder)


class Holderboy:
    def __init__(self):
        self.hold = []

class Directory:
    def __init__(self, ini, parent):
        self.tag = ini
        self.files = []
        self.dirs = {}
        self.parent = parent
        self.accsize = 0

    def handler(self, listy):
        if listy[0] == "dir":
            if listy[1] not in self.dirs.keys():
                self.dirs[listy[1]] = Directory(listy[1], self)
        else:
            self.addfile(listy)

    def command(self, list):
        if list[0] == "cd":
            if list[1] == "..":
                return self.parent
            else:
                return self.dirs[list[1]]
        else: 
            return self

    def addfile(self, list):
        self.files.append(list[1])
        self.accsize += int(list[0])
        


main()


'''
ble downlow heller enn uptop
def uptop(directory):
    print("toppin", directory.tag)
    if directory.tag == "/":
        print("/ is now", directory.accsize)
    else: 
        directory.parent.accsize += directory.accsize
        uptop(directory.parent)
'''
