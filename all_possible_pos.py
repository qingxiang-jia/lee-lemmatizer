corpse = open('corpse.txt', 'r')

corpseWriter = open('all_possible_pos', 'w+')

corpseList = []

counter = 0
for line in corpse:
    if line.strip():
        if line.split()[2] not in corpseList:
            thisLine = line.split()[2]
            corpseList.append(thisLine)     # You can't do list.append(line.split()[2]).
            counter += 1
            print "Discovering pos " + str(counter)

corpseList.sort()

for pos in corpseList:
    corpseWriter.write(pos + '\n')