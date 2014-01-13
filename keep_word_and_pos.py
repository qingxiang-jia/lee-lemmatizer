corpse = open('corpse.txt', 'r')

corpseWriter = open('word_and_pos', 'w+')

for line in corpse:
    if line.strip():    # BYU intentionally leaves empty line to id the downloaders.
        corpseWriter.write(line.split()[1] + '\t' + line.split()[2] + '\n')
        print line.split()[1] + '\t' + line.split()[2]