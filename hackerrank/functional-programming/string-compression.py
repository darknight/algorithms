def compress(string):
    if len(string) <= 1:
        return string
    queue = [[string[0], 1]]
    for ch in string[1:]:
        if queue[-1][0] == ch:
            queue[-1][1] += 1
        else:
            queue.append([ch, 1])
    data = ["%s%s" % (t[0], t[1]) if t[1] > 1 else "%s" % t[0] for t in queue]
    return "".join(data)

def compress2(string):
    if len(string) <= 1:
        return string
    data = []
    curr = string[0]
    occur = 0
    for ch in string:
        if curr == ch:
            occur += 1
        else:
            buffer = "%s%s" % (curr, occur) if occur > 1 else "%s" % curr
            data.append(buffer)
            curr = ch
            occur = 1
    buffer = "%s%s" % (curr, occur) if occur > 1 else "%s" % curr
    data.append(buffer)
    return "".join(data)

if __name__ == "__main__":
    print(compress2("abcaaabbb") == "abca3b3")
    print(compress2("abcd") == "abcd")
    print(compress2("aaabaaaaccaaaaba") == "a3ba4c2a4ba")
    print(compress2("") == "")
