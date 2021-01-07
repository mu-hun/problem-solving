from typing import List, Tuple, Dict


def make_graph(lines: List[Tuple[int, int]]):
    paths: dict[int, set] = {}
    for line in lines:
        A, B = line
        if (paths.get(A)):
            paths[A].add(B)
        else:
            paths[A] = {B}
        if (paths.get(B)):
            paths[B].add(A)
        else:
            paths[B] = {A}
    return paths


def parse_tree_paths(paths: Dict[int, set]):
    tree_nodes, cycle_nodes = [], []
    for key in paths:
        if len(paths[key]) == 1:
            tree_nodes.append(key)
        else:
            cycle_nodes.append(key)

    border_nodes = tuple(
        filter(lambda a: len(list(filter(lambda b: b in tree_nodes, paths[a]))) > 0, cycle_nodes))

    def tree_recorder(b: int):
        recording = []
        next_node = b
        while next_node in tree_nodes:
            if len(paths[next_node]) != 1:
                raise ValueError('It is not Tree')
            recording.append(next_node)
            next_node = tuple(paths[next_node])[0]
        return recording

    tree_paths = []

    for border_node in border_nodes:
        for b in filter(lambda node: node in tree_nodes, paths[border_node]):
            tree_paths.append((border_node, *tree_recorder(b)))

    return tuple(tree_paths)


def is_in_same_tree(paths: Tuple[tuple], a: int, b: int):
    for path in paths:
        if (a in path) and (b in path):
            return True
    return False


sample_paths = {
    1: {2, 3}, 2: {1, 4, 5, 3}, 3: {1, 6, 7, 2}, 4: {2}, 5: {2}, 6: {3}, 7: {3}}
parsed_tree_paths = ((2, 4), (2, 5), (3, 6), (3, 7))


def test_make_graph():
    assert make_graph([(1, 2), (1, 3), (2, 4), (2, 5),
                       (3, 6), (3, 7), (2, 3)]) == sample_paths


def test_parse_tree_paths():
    assert parse_tree_paths(sample_paths) == parsed_tree_paths


def test_is_in_same_tree():
    assert is_in_same_tree(parsed_tree_paths, 2, 4) == True
    assert is_in_same_tree(parsed_tree_paths, 2, 5) == True


if __name__ == "__main__":
    def split_line_input(): return map(int, input().split())

    N, Q = split_line_input()
    paths = [tuple(split_line_input()) for __ in range(N)]
    queries = [tuple(split_line_input()) for __ in range(Q)]

    for query in queries:
        if is_in_same_tree(parse_tree_paths(make_graph(paths)), *query):
            print(1)
        else:
            print(2)
