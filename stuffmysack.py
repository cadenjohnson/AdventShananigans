
from collections import Counter

def part1():
    total=0
    with open("testinput.txt", "r") as goodies:
        for line in goodies:
            longboi = len(line)
            left, right = slice(0,longboi//2), slice(longboi//2, longboi)
            items = Counter(line[left]) & Counter(line[right])

            total+= ord(list(items.keys())[0]) - (96 if list(items.keys())[0].islower() else 38)

    return total


def part2():
    total=0
    with open("testinput.txt", "r") as goodies:
        dracula = 0
        threestooges = []
        for line in goodies:
            threestooges.append(line.strip())
            dracula+=1
            if dracula >= 3:
                dracula = 0
                item = Counter(threestooges[0]) & Counter(threestooges[1]) & Counter(threestooges[2])
                total+= ord(list(item.keys())[0]) - (96 if list(item.keys())[0].islower() else 38)
                threestooges = []

    return total


#print(part1())
print(part2())
