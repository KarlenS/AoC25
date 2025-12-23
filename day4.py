from typing import List
import copy

def read_diagram(filename: str) -> List[List]:

    diagram = []

    with open(filename, 'r') as f:
        for row in f:
            diagram.append(list(row.strip()))

    return diagram

def is_accessible(subdiagram: List[List]):

    n_rolls = subdiagram.count('@')

    if n_rolls - 1 < 4:
        return True
    else:
        return False

def solve_diagram(diagram: List[List], mark = 'x') -> List:

    ref_diagram = copy.deepcopy(diagram)

    n_rows, n_cols = len(diagram),  len(diagram[0])

    n_accessible = 0

    for i, row in enumerate(ref_diagram):
        for j, col in enumerate(row):
            row_start = 0 if i == 0 else i-1
            col_start = 0 if j == 0 else j-1
            if col == '@':
                subdiagram = [elem for line in ref_diagram[row_start:i+2] for elem in line[col_start:j+2]]
                if is_accessible(subdiagram):
                    n_accessible+=1
                    diagram[i][j] = mark

    return diagram, n_accessible

def remove_rolls(diagram: List[List]) -> List:

    n_removed = 0
    n_remove = 999

    while n_remove > 0:

        #diagram = ['.' if elem == 'x' else elem for row in diagram for elem in row]
        diagram, n_remove = solve_diagram(diagram, mark = '.')
        n_removed += n_remove

    return diagram, n_removed


def run_tests() -> None:
    diagram = read_diagram('data/day4_test.txt')
    solved_diagram, n_accessible = solve_diagram(copy.deepcopy(diagram))
    solved_diagram2, n_removed = remove_rolls(diagram)

    solved_diagram_ref = read_diagram('data/day4_test_result.txt')
    solved_diagram_ref2 = read_diagram('data/day4_test2_result.txt')

    assert solved_diagram == solved_diagram_ref
    assert n_accessible == 13

    assert solved_diagram2 == solved_diagram_ref2
    assert n_removed == 43

def main():

    run_tests()

    diagram = read_diagram('data/day4_input.txt')
    solved_diagram, n_accessible = solve_diagram(copy.deepcopy(diagram))

    solved_diagram2, n_removed = remove_rolls(diagram)

    print(f'There are {n_accessible} accessible rolls.')
    print(f'There are {n_removed} removed rolls.')


if __name__ == '__main__':
    main()
