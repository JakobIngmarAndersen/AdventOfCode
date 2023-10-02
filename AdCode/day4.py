def main():
    file = open("input_day4.txt")
    x = 0
    checksum = 0
    q = 0
    for line in file:
        checksum += 1
        y = line.strip().split(",")
        if contains2(y[0], y[1]):
            x += 1
        else: 
            q += 1
    print(x)
    print("checksum: ", checksum)
    print(x, " ", q)

def contains(x, y):
    a = x.split("-")
    b = y.split("-")
    if (int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])):
        return True
    elif (int(b[0]) <= int(a[0]) and int(b[1]) >= int(a[1])):
        return True
    else: 
        return False

def contains2(x, y):
    a = x.split("-")
    b = y.split("-")
    a1 = list(range(int(a[0]), (int(a[1]) + 1)))
    a2 = list(range(int(b[0]), (int(b[1]) + 1)))
    for f in a1: 
        if f in a2:
            return True
    return False

main()