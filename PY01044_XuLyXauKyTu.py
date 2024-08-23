def process_words(line):
    return set(word.lower() for word in line.split())


line1 = input()
line2 = input()

set1 = process_words(line1)
set2 = process_words(line2)

union = sorted(set1 | set2)
intersection = sorted(set1 & set2)

print(' '.join(union))
print(' '.join(intersection))
