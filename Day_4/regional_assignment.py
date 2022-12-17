
def completelyoverlap(range1, range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    elif range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    return False

def overlap(range1, range2):
    if range1[1] >= range2[0] and range1[0] <= range2[1]:
        return True
    elif range1[0] <= range2[1] and range1[1] >= range2[0]:
        return True
    return False


with open("testinput4.txt", "r") as jobranges:
    inefficientteams = 0
    range1, range2 = [0,0], [0,0]
    for line in jobranges:
        elf1, elf2 = line.strip().split(",")
        range1 = list(map(int, elf1.split("-")))
        range2 = list(map(int, elf2.split("-")))
        #if completelyoverlap(range1, range2):
        if overlap(range1, range2):
            inefficientteams+=1

print(inefficientteams)

