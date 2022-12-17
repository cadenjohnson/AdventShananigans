
# part one
def onebyone(racks, instructions):
    for demand in instructions:
        for boxes in range(demand[0]):
            less = int(demand[1])-1
            more = int(demand[2])-1

            addrack = racks[more] + (racks[less])[-1]
            leastrack = (racks[less])[:-1]

            racks[more] = addrack
            racks[less] = leastrack

    return racks


# part two
def multimove(racks, instructions):
    for demand in instructions:
        less = int(demand[1])-1
        more = int(demand[2])-1

        temp = -(demand[0])
        if temp == 0:
            continue
        
        addrack = racks[more] + (racks[less])[temp:]
        leastrack = (racks[less])[:temp]

        racks[more] = addrack
        racks[less] = leastrack

    return racks


file = open("testinput5.txt", "r")
movinracks = file.readlines()

initrackheight, instructlength, rackquant = 0, 0, 0
for i in movinracks:
    if "[" in i:
        initrackheight+=1
    elif 'm' in i:
        instructlength+=1

racks, instructions = ["" for z in range(initrackheight+1)], [[0 for x in range(3)] for y in range(instructlength)]
instcount = 0
for line in movinracks:
    # obtain instructions
    if line[0] == 'm':
        test = line.strip().split(' ')
        instructions[instcount][0], instructions[instcount][1], instructions[instcount][2] = int(test[1]), int(test[3]), int(test[5])
        instcount+=1

    # obtain racks
    elif "[" in line:
        count=0
        for j in line:
            count+=1
            if (count+2)%4==0:
                racks[int(((count+2)/4)-1)]+=j

# reverse ordering of racks for easier access
count=0
for rack in racks:
    racks[count] = rack.strip()[::-1]
    count+=1

#print("racks: \n", onebyone(racks, instructions))
print("racks: \n", multimove(racks, instructions))
