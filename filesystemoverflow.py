
terminal =  open("testinput.txt", "r")


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.subs = []

    def add_file(self, file):
        self.files.append(file)

    def add_sub(self, sub):
        self.subs.append(sub)
    
    def get_files(self):
        return self.files

    def get_subs(self):
        return self.subs

    def get_sub(self, target_name):
        for i in self.subs:
            if i.name == target_name:
                return i
        return 0


class File:
    def __init__(self, name, directory, size):
        self.name = name
        self.directory = directory
        self.size = size
    
    def get_filesize(self):
        return self.size


def get_size(current_directory, free_up=0, candidate=['a',0]):
    my_size, children_size = 0,0
    small_size = []
    for i in current_directory.files:
        my_size += i.size

    for dir in current_directory.subs:
        child_size, small_sizes, test_candidate = get_size(dir, free_up, candidate)
        if test_candidate[1] < candidate[1]:
            candidate = test_candidate
        children_size += child_size
        for i in small_sizes:
            small_size.append(i)
    total_size = my_size + children_size

    if total_size <= 100000:
        small_size.append(total_size)

    if candidate[1]:
        if total_size > free_up and total_size < candidate[1]:
            candidate = [current_directory.name, total_size]

    return total_size, small_size, candidate


def cd_into(current_directory, target_directory):
    test = current_directory.get_sub(target_directory)
    if test:
        return test
    else:
        return current_directory


def cd_outof(current_directory):
    if current_directory.parent != None:
        return current_directory.parent
    else:
        return current_directory


# read input and build file system tree
root_directory = Directory('/')
current_directory = root_directory
for line in terminal:
    line = line.strip()
    line_details = line.split(' ')
    # command
    if line_details[1] == "cd":
        if line_details[1] == 'cd':
            if line_details[2] == '..':
                current_directory = cd_outof(current_directory)
            else:
                current_directory = cd_into(current_directory, line_details[2])
    elif line_details[1] == "ls":
        continue
    # directory
    elif line_details[0] == "dir":
        sub = Directory(line_details[1], current_directory)
        current_directory.add_sub(sub)
    # file
    else:
        file = File(line_details[1], current_directory, int(line_details[0]))
        current_directory.add_file(file)


total, small_sizes, candidate = get_size(root_directory)
free_up = 30000000 - (70000000 - total)
candidate = ['itchyanus',70000000]
total, small_sizes, target_directory = get_size(root_directory, free_up, candidate)

#print(sum(small_sizes))
print(total, sum(small_sizes), target_directory)
