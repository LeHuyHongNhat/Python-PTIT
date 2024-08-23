from math import gcd


def are_coprime(a, b):
    return gcd(a, b) == 1


def is_coprime_triple(a, b, c):
    return are_coprime(a, b) and are_coprime(b, c) and are_coprime(a, c)


def find_coprime_triples(L, R):
    triples = []
    for a in range(L, R - 1):
        for b in range(a + 1, R):
            for c in range(b + 1, R + 1):
                if is_coprime_triple(a, b, c):
                    triples.append((a, b, c))
    return triples


L, R = map(int, input().split())

triples = find_coprime_triples(L, R)
for triple in triples:
    print(f"({triple[0]}, {triple[1]}, {triple[2]})")
