
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


with open("testinput2.txt", "r") as file:
    for line in file:
        opponent, player = switcharoo[line[0]], line[2]

        if player == "X":
            player = chickendinner[opponent]
        elif player == "Y":
            player = opponent
        else:
            player = pumpkineater[opponent]

        if chickendinner[player] == opponent:
            score+=6
        elif opponent == player:
            score+=3

        score+=points[player]


print(score)

