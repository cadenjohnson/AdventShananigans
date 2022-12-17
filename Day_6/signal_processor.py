
def find_target(indicator_length, array, success):
    if len(array) == indicator_length:
        test = sorted(array)
        y=0
        for j in test:
            y+=1
            if y < indicator_length:
                if test[y-1] == test[y]:
                    break
            else:
                if success == 0:
                    success=count
                    print(success)
                    print(array)
                    return success
    return success


with open("testinput6.txt", "r", encoding='utf-8') as signalstream:
    buffarray, messagearray=[],[]
    success, success2= 0,0
    count = 0

    line = signalstream.readlines()[0]
    for i in line:
        count+=1
        buffarray.append(i)
        messagearray.append(i)
        if len(buffarray) > 4:
            buffarray = buffarray[1:]
        if len(messagearray) > 14:
            messagearray = messagearray[1:]
        success = find_target(4, buffarray, success)
        success2 = find_target(14, messagearray, success2)
