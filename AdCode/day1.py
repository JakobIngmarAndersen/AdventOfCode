def main():
    file = open("input_day1.txt", "r")
    elflist = []
    tmpval = 0
    for line in file:
        print("doin line: ", line)
        if (line == "\n"):
            x = Elf(tmpval)
            elflist.append(x)
            tmpval = 0
            print(x.carrying)
        else:
            tmpval += int(line)
    topelf = 0
    for y in elflist: 
        if (y.carrying > topelf):
            topelf = y.carrying
    
    print(topelf)

    print(topthree(elflist))
    







def topthree(elflist):
    top1 = 0
    top2 = 0
    top3 = 0
    for elf in elflist: 
        if elf.carrying > top1:
            x = top2
            top2 = top1
            top3 = x
            top1 = elf.carrying
        elif elf.carrying > top2:
            top3 = top2
            top2 = elf.carrying
        elif elf.carrying > top3:
            top3 = elf.carrying
    print("summed", top1 + top2 + top3)
    return [top1, top2, top3]
        








class Elf:
    def __init__(self, weight):
        self.carrying = weight




main()