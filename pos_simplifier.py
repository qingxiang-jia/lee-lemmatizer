# Uses simplified_pos to loop through the word_and_pos and simplifies the pos of it.

# Generating simplified_dict

simplified_pos = open('simplified_pos', 'r')

simplified_dict = {}

for line in simplified_pos:
    simplified_dict.update({line.split()[0]:line.split()[1]})

print "Dictionary loading finished"

simplified_pos.close()

# Simplifying pos

words_and_pos = open('word_and_pos', 'r')

words_and_pos_simplified_writer = open('words_and_pos_simplified', 'w+')

for line in words_and_pos:
    word = line.split()[0]
    print "working on " + word
    pos = simplified_dict[line.split()[1]]
    words_and_pos_simplified_writer.write(word + '\t\t' + pos + '\n')

words_and_pos.close()