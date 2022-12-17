
def cnv_ltr(letter):
    return ord(letter)-96


def check_surroundings(c_loc, map, past):
    # return the viable options
    viable_moves = []
    # check up
    if c_loc[0] != 0 and (c_loc[0]-1, c_loc[1]) not in past:
        if cnv_ltr(map[c_loc[0]-1][c_loc[1]]) <= cnv_ltr(map[c_loc[0]][c_loc[1]])+1:
            viable_moves.append((c_loc[0]-1, c_loc[1]))
    # check right
    if c_loc[1] != len(map[0])-1 and (c_loc[0], c_loc[1]+1) not in past:
        if cnv_ltr(map[c_loc[0]][c_loc[1]+1]) <= cnv_ltr(map[c_loc[0]][c_loc[1]])+1:
            viable_moves.append((c_loc[0], c_loc[1]+1))
    # check down
    if c_loc[0] != len(map)-1 and (c_loc[0]+1, c_loc[1]) not in past:
        if cnv_ltr(map[c_loc[0]+1][c_loc[1]]) <= cnv_ltr(map[c_loc[0]][c_loc[1]])+1:
            viable_moves.append((c_loc[0]+1, c_loc[1]))
    # check left
    if c_loc[1] != 0 and (c_loc[0], c_loc[1]-1) not in past:
        if cnv_ltr(map[c_loc[0]][c_loc[1]-1]) <= cnv_ltr(map[c_loc[0]][c_loc[1]])+1:
            viable_moves.append((c_loc[0], c_loc[1]-1))
    return viable_moves


def chart_course(c_loc, map, end, route=[]):
    # get viable moves
    route.append(c_loc)
    viable_moves = check_surroundings(c_loc, map, route)

    if len(viable_moves) == 0 or end in route:
        return route
    
    # check different routes (recursive)
    child_routes = []
    for loc in viable_moves:
        test = chart_course(loc, map, end, route)
        if end in test:
            child_routes.append(test)

    # test for shortest option
    if len(child_routes) >= 1:
        min_route = child_routes[0]
        for i in child_routes:
            if len(i) < min_route:
                min_route = i
        # update route with shortest solution
        for i in min_route:
            route.append(i)
        return route
    else:
        return []




# import data into a 2d array "map"
file = open("testinput.txt", "r")
map = []
start, end = None, None

ct = 0
for line in file:
    map.append([])
    ct2 = 0
    for j in range(len(line.strip())):
        if line[j] == "S":
            map[ct].append('a')
            start = (ct, ct2)
        elif line[j] == "E":
            map[ct].append('z')
            end = (ct, ct2)
        else:
            map[ct].append(line[j])
        ct2+=1
    ct+=1

print(chart_course(start, map, end))

# visualization of map
#for i in map:
#    test=''
#    for j in i:
#        test+=j
#    print(test)

