def mostCommonWord(paragraph, banned):
    for c in "!?',;.":
        paragraph = paragraph.replace(c, '')

        d, res, count = {}, "", 0

    for word in paragraph.lower().split():
        if word in banned:
            continue
        elif word in d:
            print('elif')
            d[word] += 1
        else:
            print('else')
            d[word] = 1

        if d[word] > count:
            print('if')
            count = d[word]
            res = word
        print(d)
    return res


n = "Bob hit a ball, the hit BALL flew far after it was hit."
b = 'hit'
print(mostCommonWord(n, b))
