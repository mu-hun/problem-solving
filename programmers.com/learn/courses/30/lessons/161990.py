from functools import reduce

def reducer(a: str, b: str):
    length = len(a)
    reduced = []
    for index in range(length):
        if a[index] == '#' or b[index] == '#':
            reduced.append('#')
        else:
            reduced.append('.')
    
    return ''.join(reduced)

def solution(wallpaper: list[str]):
    flatten = reduce(reducer, wallpaper)
    luy, rdy = flatten.find('#'), flatten.rfind('#') + 1

    mappedRow = list(map(lambda row: '#' in row, wallpaper))

    lux, rdx = mappedRow.index(True), len(mappedRow) - mappedRow[::-1].index(True)

    return [lux, luy, rdx, rdy]

def test_reducer():
    assert reducer('.....#....', '......##..') == '.....###..'

def test_solution():
    assert solution([".#...", "..#..", "...#."]) == [0, 1, 3, 4]
    assert solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]) == [1, 3, 5, 8]
    assert solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]) == [0, 0, 7, 9]
    assert solution(["..", "#."]) == [1, 0, 2, 1]
