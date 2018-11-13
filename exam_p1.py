
# load in the class roster to the file, also leaving only the first name (lowercase) as a list
def load_file(file_name):
    actual_roster = []
    roster = open(file_name, 'r')
    for line in roster:
        actual_roster.append(line.split()[0].lower())
    return actual_roster
# make a dict of matching numbers to characters
def make_dict():
    score = {}
    for i in range(1,27):
        score[chr(96+i)] = i
    return score
#calculate the score
def score(word):
    dict = make_dict()
    score = 0
    for c in word:
        if c in "!@#$%^&*()-_+={}[]|\:;'<>?,./\"":
            score += 0
        else:
            score += dict[c]
    return score

def find_matches(name, list):
    jack_list = []
    for words in list:
        if score(words) == score(name):
            jack_list.append(words)
    if len(jack_list) == 0:
        return None
    else:
        return jack_list

def main():
    roster = load_file('roster.txt')
    scorec = 0
    namec = ""
    for name in roster:
        if score(name) > scorec:
            scorec = score(name)
            namec = name

    print("The most valuable person is: " + namec + ", with a score of " + str(scorec) + '.')

    positive_words = load_file('positive-words.txt')

    print("The positive words that have the same value as jack is: ")
    result = find_matches('jingyu', positive_words)
    if result == None:
        print(result)
    else:
        for i in (find_matches('jingyu', positive_words)):
            print(i)

if __name__ == '__main__':
    main()
