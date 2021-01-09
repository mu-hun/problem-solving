from typing import List, Tuple, Dict

from itertools import chain

Path = Tuple[int, int]
Query = Path


def make_graph(lines: List[Path]):
    paths: dict[int, set] = {}
    for line in lines:
        A, B = line
        if paths.get(A):
            paths[A].add(B)
        else:
            paths[A] = {B}
        if paths.get(B):
            paths[B].add(A)
        else:
            paths[B] = {A}
    return paths


def query(paths: Dict[int, set], queries: List[Query]):
    tree_nodes, cycle_nodes = {}, {}
    for key in paths:
        if len(paths[key]) == 1:
            tree_nodes[key] = True
        else:
            cycle_nodes[key] = True

    border_nodes = tuple(
        filter(lambda a: len(list(filter(lambda b: tree_nodes.get(b), paths[a]))) > 0, cycle_nodes.keys()))

    def tree_recorder(b: int):
        recording = []
        next_node = b
        while tree_nodes.get(next_node):
            recording.append(next_node)
            next_node = tuple(paths[next_node])[0]
        return recording

    branchs = {}
    for border_node in border_nodes:
        branchs[border_node] = tuple(chain.from_iterable(map(tree_recorder, filter(
            lambda node: tree_nodes.get(node), paths[border_node]))))

    def go(query: Query):
        node, goal = query
        if node == goal:
            return True

        if len(paths[node]) == 1:
            return go((tuple(paths[node])[0], goal))

        if not branchs.get(node):
            return False

        return goal in branchs[node]

    return tuple(map(go, queries))


sample_paths = {
    1: {2, 3}, 2: {1, 4, 5, 3}, 3: {1, 6, 7, 2}, 4: {2}, 5: {2}, 6: {3}, 7: {3}}
parsed_tree_paths = ((2, 4), (2, 5), (3, 6), (3, 7))


def test_make_graph():
    assert make_graph([(1, 2), (1, 3), (2, 4), (2, 5),
                       (3, 6), (3, 7), (2, 3)]) == sample_paths


def test_query():
    assert query(sample_paths, [(2, 4), (4, 5), (1, 4)]) == (True, True, False)


if __name__ == "__main__":
    from sys import stdin
    def split_line_input(): return map(int, stdin.readline().split())

    N, Q = split_line_input()
    paths = [tuple(split_line_input()) for __ in range(N)]
    queries = [tuple(split_line_input()) for __ in range(Q)]

    results = query(make_graph(paths), queries)

    for result in results:
        print({True: 1, False: 2}[result])
