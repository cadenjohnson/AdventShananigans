
# points
win, draw, lose = 6, 3, 0
score = 0

# not necessary, just for aesthetics, ya feel?
points = {
    "Rock":1,
    "Paper":2,
    "Scissors":3
}

switcharoo = {
    "A":"Rock", "X":"Rock",
    "B":"Paper", "Y":"Paper",
    "C":"Scissors", "Z":"Scissors"}

chickendinner = {
    "Rock":"Scissors",
    "Scissors":"Paper",
    "Paper":"Rock"
}

pumpkineater = {
    "Scissors":"Rock",
    "Paper":"Scissors",
    "Rock":"Paper"
}


with open("testinput.txt", "r") as wtf:
    for line in wtf:
        playa, bigboi = switcharoo[line[0]], line[2]

        if bigboi == "X":
            bigboi = chickendinner[playa]
        elif bigboi == "Y":
            bigboi = playa
        else:
            bigboi = pumpkineater[playa]

        if chickendinner[bigboi] == playa:
            score+=6
        elif playa == bigboi:
            score+=3

        score+=points[bigboi]


print(score)

