def count_words(filename):
    count_words = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in count_words:
                    count_words[word] +=1
                else:
                    count_words[word] = 1
    return count_words
