def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    list = []
    file = open(file_name, 'r')
    for line in file:
        temp = line.split(',')
        list.append(temp)
    return list



def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    if 1879 < int(year) < 2011:
        yearlist = process_file('babynames/yob' + str(year) + '.txt')
        sum = 0
        for item in yearlist:
            sum += int(item[2])
        return sum
    else:
        raise ValueError


def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    yearlist = process_file('babynames/yob' + str(year) + '.txt')
    for item in yearlist:
        if name == item[0] and gender == item[1]:
            return (int(item[2])/total_births(year))
    return 0.0

def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the
    proportions of the same name in different years)
    """
    highest = 0
    highyear = 0
    for i in range(1880, 2011):
        if proportion(name, gender, i) > highest:
            highest = proportion(name, gender, i)
            highyear = i
    return highyear

def main():
    pass  # delete this line and replace with your code here


if __name__ == '__main__':
    print("The year " + str(highest_year("Jack", "M")) + " has the highest proportion among all the proportions o"
                                                    "f my names in other years.")
