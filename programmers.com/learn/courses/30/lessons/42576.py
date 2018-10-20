from collections import Counter

solution = lambda p, v: list((Counter(p) - Counter(v)).keys())[0]
