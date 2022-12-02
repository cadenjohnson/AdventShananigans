with open("penis.txt", 'r+') as penisfile:
    penis, softpenis, semipenis, maxpenis = 0,0,0,0
    for i in penisfile:
        if i != '\n':
            penis += int(i)
        else:
            if penis > maxpenis:
                softpenis = semipenis
                semipenis = maxpenis
                maxpenis = penis
            elif penis > semipenis:
                softpenis = semipenis
                semipenis = penis
            elif penis > softpenis:
                softpenis = penis
            penis = 0

print("total= "+str(maxpenis+semipenis+softpenis))
