def main():
    file = open("input_day5.txt")
    rawlist = []

    for q in range(8):
        active = file.readline()
        counter = 2
        explist = []
        for char in active:
            if counter == 3:
                explist.append(char)
                counter = 0
            else: 
                counter += 1
        rawlist.append(explist)
    
    dicline = file.readline().strip().split("  ")
    booky = {}
    for y in dicline:
        y = int(y)
        booky[y] = []
        for z in rawlist:
            if z[y-1] != " ":
                booky[y].append(z[y-1])

    file.readline()
    '''
    del1:
    for line in file: 
        f = line.strip().split(" ")
        for i in range(int(f[1])):
            mover(booky[int(f[3])], booky[int(f[5])])
    '''
    for line in file: 
        f = line.strip().split(" ")
        mover2(booky[int(f[3])], booky[int(f[5])], int(f[1]))
    result = []
    for listy in booky:
        result.append(booky[listy][0])
    print(result)



def mover(list1, list2):
    x = list1.pop(0)
    list2.insert(0, x)

def mover2(list1, list2, amount):
    moveable = []
    for i in range(amount):
        mover(list1, moveable)
    for i in range(len(moveable)):
        mover(moveable, list2)



'''
x = [1, 2, 3]
y = [4, 5, 6]
mover2(x, y, 2)
print(x)
print(y)
'''
main()