class Stack:
    def __init__(self):
        self.elements = []
        self.key = {'pop': self.pop, 'size': self.size,
                    'empty': self.is_empty, 'top': self.top, 'push': self.push}

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        if self.is_empty():
            return -1
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def is_empty(self):
        if self.size() is 0:
            return 1
        return 0

    def top(self):
        if not self.is_empty():
            return self.elements[-1]
        return -1


if __name__ == '__main__':
    s = Stack()
    from sys import stdin
    for __ in range(int(stdin.readline().rstrip())):
        _in = stdin.readline().rstrip().split()
        if _in[0] == 'push':
            s.push(int(_in[1]))
            continue
        print(s.key[_in[0]]())
