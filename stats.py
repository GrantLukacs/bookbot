def word_counter(string):
    count = string.split()
    return len(count)

def character_counter(string):
    lowercase_string = string.lower()
    final_total = {}
    starting_count = 1
    for i in lowercase_string:
        if i in final_total:
            final_total[i] += 1
        else:
            final_total[i] = 1
    return final_total

def sort_on(dict):
    return dict["num"]

def sorter(dictionary):
    list = []
    for i in dictionary:
        if i.isalpha() == True:
            list.append({"char" : i, "num" : dictionary[i]})
    list.sort(reverse=True, key=sort_on)
    return list