def main():
    file = open("input_day6.txt")
    seq = []
    for line in file:
        for char in line:
            seq.append(char)
    result = whenboy(seq)
    print("result: ", result)

def whenboy(listy):
    for i in range(13, len(listy)):
        x = [listy[i-13], listy[i-12], listy[i-11], listy[i-10],
        listy[i-9], listy[i-8], listy[i-7], listy[i-6],
        listy[i-5], listy[i-4], listy[i-3], listy[i-2], listy[i-1], listy[i]]
        if unique(x):
            return i + 1

def unique(listy):
    setboy = set()
    for x in listy:
        if x not in setboy:
            setboy.add(x)
        else: 
            return False
    return True



main()