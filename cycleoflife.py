
def check_cycle(cycle, X):
    if cycle % 20 == 0:
        signal_strengths.append(cycle*X)


def draw(cycle, X, CRT):
    row = cycle // 40
    col = cycle % 40

    if row < 6:
        diff = col-X
        if abs(diff) <= 1:
            pixel = '#'
        else:
            pixel = '.'
        CRT[row][col] = pixel
        return CRT
    else:
        return CRT


instructions = open("testinput.txt", "r")
cycle = 0
X=1
signal_strengths = []
signal_strengths.append(cycle*X)
finished = False

CRT = [['.' for i in range(40)] for j in range(6)]


for i in instructions:
    CRT = draw(cycle, X, CRT)
    cycle+=1
    check_cycle(cycle, X)
    if "noop" in i:
        continue

    else:
        CRT = draw(cycle, X, CRT)
        task, value = i.split(' ')
        cycle+=1
        check_cycle(cycle, X)
        X+=int(value)

print(sum(signal_strengths[1::2]))
for line in CRT:
    temp = ''
    for pixel in line:
        temp+=pixel
    print(temp)

