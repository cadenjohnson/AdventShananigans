##########################################################################
# borrowed code from includehelp.com
import math
# function to calculate LCM
def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm
###########################################################################

class Monkey:
    # i like bananas and hangin around
    # dont mess w me or ill take ur stuff
    def __init__(self):
        # items
        self.items = []
        self.current_item = None
        self.inspections = 0

        # operation details
        self.operation_method = None
        self.operation_value = None

        # test value
        self.testing = 0
        self.LCM = None

        # target monkeys to toss to
        self.very_worried = 0
        self.kinda_worried = 0


    def how_worried(self, worry_value):
        if self.operation_value == "old":
            temp_operate_value = worry_value
        else:
            temp_operate_value = int(self.operation_value)

        if self.operation_method == '*':
            result =  worry_value*temp_operate_value
        elif self.operation_method == '+':
            result =  worry_value+temp_operate_value
        
        return result


    def is_he_worried(self, worry_value):
        self.inspections += 1
        if worry_value % self.testing == 0:
            return True
        else:
            return False

    
    def toss(self, monkeys):
        if len(self.items) > 0:
            for i in range(len(self.items)):
                self.current_item = self.items[:1][0]
                temp = self.how_worried(self.current_item)
                # no longer... the bastards have adapted...
                #self.current_item = temp // 3
                self.current_item = temp % self.LCM
                tested = self.is_he_worried(self.current_item)
                if tested:
                    monkeys[self.very_worried].items.append(self.current_item)
                    self.items = self.items[1:]
                elif not tested:
                    monkeys[self.kinda_worried].items.append(self.current_item)
                    self.items = self.items[1:]



def eval_input(file):
    monkeys = []
    for line in file:
        line = line.strip()
        if "Monkey" in line:
            monkey = Monkey()
        elif "Starting" in line:
            line = line.split(": ")
            items = line[1].split(", ")
            for i in items:
                monkey.items.append(int(i))
        elif "Operation" in line:
            line = line.split("old ")
            monkey.operation_method, monkey.operation_value = line[1].split(' ')
        elif "Test" in line:
            line = line.split('by ')
            monkey.testing = int(line[1])
        elif "true" in line:
            line = line.split('monkey ')
            monkey.very_worried = int(line[1])
        elif "false" in line:
            line = line.split('monkey ')
            monkey.kinda_worried = int(line[1])
        else:
            monkeys.append(monkey)
    monkeys.append(monkey)
    return monkeys


def get_inspections(monkeys):
    monkey_inspections = []
    for monkey in monkeys:
        monkey_inspections.append(monkey.inspections)
    return monkey_inspections



file = open("testinput.txt", "r")
monkeys = eval_input(file)

testers = []
for i in monkeys:
    testers.append(i.testing)
LCM = LCMofArray(testers)
for i in monkeys:
    i.LCM = LCM

round_count = 0
for round in range(10000):
    round_count+=1
    for monkey in monkeys:
        monkey.toss(monkeys)


monkey_inspections = get_inspections(monkeys)
monkey_inspections.sort(reverse=True)
monkey_business = monkey_inspections[0]*monkey_inspections[1]
print(monkey_business)

