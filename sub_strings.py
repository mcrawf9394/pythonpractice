def sub_strings(str, dictionary):
    str = str.lower()
    countPerWord = dict({})
    for word in dictionary:
        if len(word) > len(str):
            continue
        else:
            copy = str
            count = 0
            while copy.find(word) != -1:
                copy = copy.replace(word, "", 1)
                count = count + 1
            if count > 0:
                countPerWord[word] = count
    return countPerWord
dictionary = ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]
print(sub_strings("below", dictionary))
print(sub_strings("Howdy partner, sit down! How's it going?", dictionary))