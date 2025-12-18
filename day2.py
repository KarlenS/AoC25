from typing import List

def read_ids(filename: str) -> List:

    with open(filename, 'r') as f:
        ranges_txt = f.read()

    return [id_range.split('-') for id_range in ranges_txt.split(',')]


def is_invalid_id_simple(id: int) -> bool:

    id_str = str(id)
    n = len(id_str)

    if n%2 != 0:
        return False
    elif id_str[:n//2] == id_str[n//2:]:
        return True
    else:
        return False

def is_invalid_id_complex(id: int) -> bool:

    id_str = str(id)
    n = len(id_str)

    divisors = [i for i in range(1,n//2+1) if n%i == 0]

    for div in divisors:
        subs = [id_str[i:i+div] for i in range(0,n,div)]
        # new favorite way of checking of all elements are the same
        if subs.count(subs[0]) == len(subs):
            return True
    return False


def detect_invalid_ids(id_ranges: List,
                       is_invalid_id  = is_invalid_id_simple) -> List:

    invalid_ids = []
    for id_range_start, id_range_end in id_ranges:
        for candidate_id in range(int(id_range_start),int(id_range_end)+1):
            if is_invalid_id(candidate_id):
                invalid_ids.append(candidate_id)

    return invalid_ids

def run_tests():

    id_list = read_ids('data/day2_test.txt')

    invalid_ids_1 = detect_invalid_ids(id_list)
    assert sum(invalid_ids_1) == 1227775554

    invalid_ids_2 = detect_invalid_ids(id_list, is_invalid_id = is_invalid_id_complex)
    assert sum(invalid_ids_2) == 4174379265

def main():

    run_tests()

    id_list = read_ids('data/day2_input.txt')

    invalid_ids_1 = detect_invalid_ids(id_list)
    sum_of_ids_1 = sum(invalid_ids_1)

    print(f'Part1: The invalid IDs sum to {sum_of_ids_1}')

    invalid_ids_2 = detect_invalid_ids(id_list, is_invalid_id = is_invalid_id_complex)
    sum_of_ids_2 = sum(invalid_ids_2)

    print(f'Part2: The invalid IDs sum to {sum_of_ids_2}')


if __name__ == '__main__':
    main()
