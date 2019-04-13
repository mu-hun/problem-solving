def UCPC(_str=input()):
    i = 0
    for c in _str:
        if i == 0 and c == 'U':
            i += 1
        elif (i == 1 or i == 3) and c == 'C':
            i += 1
        elif i == 2 and c == 'P':
            i += 1
    print(f"I {({4: 'love'}.get(i, 'hate'))} UCPC")


if __name__ == '__main__':
    UCPC()
