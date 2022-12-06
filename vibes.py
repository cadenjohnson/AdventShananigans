
with open("testinput.txt", "r", encoding='utf-8') as signalstream:
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

        if len(buffarray) == 4:
            test = sorted(buffarray)
            
            z=0
            for i in test:
                z+=1
                if z < 4:
                    if test[z-1] == test[z]:
                        break
                else:
                    if success == 0:
                        success = count
                        print(success)
                        print(buffarray)
                        print(test)
                    break
        
        if len(messagearray) == 14:
            test2 = sorted(messagearray)
            y=0
            for j in test2:
                y+=1
                if y < 14:
                    if test2[y-1] == test2[y]:
                        break
                else:
                    if success2 == 0:
                        success2=count
                        print("m-",success2)
                        print(messagearray)
                        print(test2)
                    break
