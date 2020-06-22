import random


def typoglycemia(string):
    words = string.split()
    res = []
    for word in words:
        if len(word) > 4:
            mid = random.sample(word[1: -1], len(word) - 2)
            new_word = word[0] + ''.join(mid) + word[-1]
            res.append(new_word)
        else:
            res.append(word)
    return res


s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(*typoglycemia(s))
