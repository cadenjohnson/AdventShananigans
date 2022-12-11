

def convert_to_one(num):
    if num<0:
        return -1
    elif num>0:
        return 1
    else:
        return 0


class Knot:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.location = (0,0)
        self.past = (0,0)
        self.history = []
    
    def update_history(self):
        self.past = self.location
        if self.location not in self.history:
            self.history.append(self.location)

    def lead_or_follow(self, direction=None, distance=None):
        # move to new location
        if self.head == None:
            new_location = self.location
            if direction == 'R':
                new_location = (new_location[0] + distance, new_location[1])
            elif direction == 'L':
                new_location = (new_location[0] - distance, new_location[1])
            elif direction == 'U':
                new_location = (new_location[0], new_location[1] + distance)
            else:
                new_location = (new_location[0], new_location[1] - distance)
            self.lead(new_location)
        else:
            self.follow()
    
    def lead(self, new_location):
        self.update_history()
        self.location = new_location

    def follow(self):
        distance_x = abs(self.head.location[0] - self.location[0])
        distance_y = abs(self.head.location[1] - self.location[1])
        # diagonal move -- wow, so much effort put into this...
        if distance_x + distance_y == 3:
            x = convert_to_one(self.head.location[0] - self.location[0])
            y = convert_to_one(self.head.location[1] - self.location[1])
            self.update_history()
            self.location = (self.location[0] + x, self.location[1] + y)

        # non-gay move
        elif distance_x > 1 or distance_y > 1:
            self.update_history()
            x = convert_to_one(self.head.location[0] - self.location[0])
            y = convert_to_one(self.head.location[1] - self.location[1])
            self.location = (self.location[0]+x, self.location[1]+y)



instructions = open("testinput.txt", "r")

# create knots in rope
Knots = []
Head = Knot()
Knots = [Head]
for i in range(9):
    middle = Knot(head=Knots[-1:][0])
    Knots[-1:][0].tail = middle
    Knots.append(middle)

# move
for move in instructions:
    direction, distance = move.strip().split(' ')
    for i in range(int(distance)):
        for knot in Knots:
            knot.lead_or_follow(direction, 1)


# update their last and final positions
for i in Knots:
        i.update_history()

print(len(Knots[-1:][0].history))

