def main():
    file = open("input_day3.txt")
    y = []
    x = []
    part2list = []
    helper = []
    counter = 0
    for line in file:
        counter += 1
        y.append(organiser(line.strip()))
        helper.append(line.strip())
        if counter == 3:
            part2list.append(helper)
            helper = []
            counter = 0
    charlist = yikes()
    sum = 0
    for l in y:
        sum += find(l, charlist)
    print(sum)
    sum2 = 0
    for list in part2list:
        common = part2(list)
        sum2 += find(common, charlist)
    print(sum2)

def organiser(instring):
    x = int(len(instring)/2)
    y = []
    for letter in instring:
        y.append(letter)
    half1 = y[:x]
    half2 = y[x:]
    for q in half1:
        if q in half2:
            return q


def yikes():
    x = list(map(chr, range(97, 123)))
    y = x.copy()
    for char in x: 
        y.append(char.upper())
    return y

def find(x, list):
    y = 0
    for q in list:
        y += 1
        if q == x:
            return y


def part2(party):
    a = []
    b = []
    c = []

    for char in party[0]:
        a.append(char)
        
    for char in party[1]:
        b.append(char)
    
    for char in party[2]:
        c.append(char)


    for x in a:
        if x in b:
            if x in c:
                return x

main()
