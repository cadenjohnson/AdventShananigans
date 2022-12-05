
# part one
def onebyone(racks, instructions):
    for demand in instructions:
        for boxes in range(demand[0]):
            less = int(demand[1])-1
            more = int(demand[2])-1

            addrack = racks[more] + (racks[less])[-1]
            leastrack = (racks[less])[:-1]
            abendago = "idk wtf i'm doing"

            racks[more] = addrack
            racks[less] = leastrack

    return racks


# part two
def heftyboi(racks, instructions):
    for demand in instructions:
        less = int(demand[1])-1
        more = int(demand[2])-1

        temp = -(demand[0])
        
        addrack = racks[more] + (racks[less])[temp:]
        leastrack = (racks[less])[:temp]
        abendago = "idk wtf i'm doing"

        racks[more] = addrack
        racks[less] = leastrack

    return racks


with open("testinput.txt", "r") as movinracks:
    racks, instructions = ["" for z in range(9)], [[0 for x in range(3)] for y in range(501)]
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


#racks = onebyone(racks, instructions)
racks = heftyboi(racks, instructions)

print("racks: \n", racks)
