
forest = open("testinput.txt", "r")
trees = []

for line in forest:
    trees.append(line.strip())

width, height = len(trees[0]), len(trees)


def check_North(tree,y,x,trees):
    if y == 0:
        return 0
    count = 0
    test = y-1
    while test != -1:
        if int(trees[test][x]) < tree:
            count += 1
        elif int(trees[test][x]) >= tree:
            count += 1
            return count
        test -= 1
    return count
    

def check_West(tree,y,x,trees):
    if x == 0:
        return 0
    count = 0
    test = x-1
    while test != -1:
        if int(trees[y][test]) < tree:
            count += 1
        elif int(trees[y][test]) >= tree:
            count += 1
            return count
        test -= 1
    return count


def check_South(tree,y,x,trees, height):
    if y == height-1:
        return 0
    count = 0
    test = y+1
    while test != height:
        if int(trees[test][x]) < tree:
            count += 1
        elif int(trees[test][x]) >= tree:
            count += 1
            return count
        test += 1
    return count


def check_East(tree,y,x,trees, width):
    if x == width-1:
        return 0
    count = 0
    test = x+1
    while test != width:
        if int(trees[y][test]) < tree:
            count += 1
        elif int(trees[y][test]) >= tree:
            count += 1
            return count
        test += 1
    return count

#trees[y][x]
max = 0
y=0
for col in trees:
    x=0
    for row in col:
        row = int(row)
        t1 = check_North(row,y,x,trees)
        t2 = check_West(row,y,x,trees)
        t3 = check_South(row,y,x,trees, height)
        t4 = check_East(row,y,x,trees, width)
        score = t1*t2*t3*t4
        if score > max:
            max = score
        
        x+=1
    y+=1

print(max)
