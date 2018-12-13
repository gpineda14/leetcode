def findRepeatedDNASequences(s):
    sequences = collections.defaultdict(int)
    repeated_dna = set()
    start = 0
    end = 10
    while end < len(s) + 1:
        curr = s[start:end]
        sequences[curr] += 1
        if sequences[curr] > 1:
            repeated_dna.add(curr)
        start += 1
        end += 1

    return list(repeated_dna)
