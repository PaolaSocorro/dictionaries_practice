

word_file = open("test.txt")
dict_value = {}
for line in word_file:
    line = line.strip()
    word_list = line.split(" ")
    
    #print my_data
    for word in word_list:

        if word not in dict_value.keys():
            dict_value[word] = 1
        else:
            dict_value[word] += 1
        

for tup in dict_value.items():
    print "%s: %d" % (tup[0], tup[1])


