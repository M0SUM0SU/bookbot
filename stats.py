def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_counts = {}
    for char in text:
        lchar = char.lower()
        if lchar in char_counts:
            char_counts[lchar] += 1
        else:
            char_counts[lchar] = 1
    return char_counts

def beautify(text):
    chlist = []
    for char, count in text.items():
        char_dict = {"char": char, "num": count}
        chlist.append(char_dict)  
    
    def sort_on(item):  
        return item["num"]
    
    chlist.sort(reverse=True, key=sort_on)
    return chlist