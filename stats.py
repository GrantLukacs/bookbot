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