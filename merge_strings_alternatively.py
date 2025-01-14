def merge_strings_alternatively(word1, word2):
    i, j = 0, 0

    res = []

    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])

        i += 1
        j += 1

    res.append(word1[i:])
    res.append(word2[j:])

    return "".join(res)

if __name__ == '__main__':
    print(merge_strings_alternatively('abc', 'def')) # EXPECTED: 'adbecf'
    print(merge_strings_alternatively("ab", "pqrs")) # EXPECTED: 'apbqrs'
    print(merge_strings_alternatively("abcd", "pq")) # EXPECTED: 'apbqcd'