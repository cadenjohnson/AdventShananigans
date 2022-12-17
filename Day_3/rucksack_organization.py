
from collections import Counter

def part1():
    total=0
    with open("testinput3.txt", "r") as file:
        for line in file:
            line_length = len(line)
            left, right = slice(0,line_length//2), slice(line_length//2, line_length)
            items = Counter(line[left]) & Counter(line[right])

            total+= ord(list(items.keys())[0]) - (96 if list(items.keys())[0].islower() else 38)

    return total


def part2():
    total=0
    with open("testinput3.txt", "r") as file:
        count = 0
        elf_triad = []
        for line in file:
            elf_triad.append(line.strip())
            count+=1
            if count >= 3:
                count = 0
                item = Counter(elf_triad[0]) & Counter(elf_triad[1]) & Counter(elf_triad[2])
                total+= ord(list(item.keys())[0]) - (96 if list(item.keys())[0].islower() else 38)
                elf_triad = []

    return total


#print(part1())
print(part2())
