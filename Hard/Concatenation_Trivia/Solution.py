from collections import defaultdict
"""
    Comments:
        - At minimum for array of length n
            - Total is at least n * sum(array), representing the 2nd half of the concatentation
            - Remaining is the first halves, which can be represented as a certain number of multiplications by 10,20,etc.
"""

def array_concat_sum(input):
    n = len(input)

    sc = defaultdict(lambda: 0)
    for i in input:
        sc[len(str(i))] += 1

    total = 0
    for i in input:
        total += i * n
        for scale in sc:
            total += (10 ** scale) * i * sc[scale]

    return total

input = list(range(10000))
print(array_concat_sum(input))