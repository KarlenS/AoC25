from typing import List

def read_combinations(filename: str) -> List:
    '''
    Read the input data for turning dials and convert them into integers.
    For example, L42 should be read as -42 and R42 should be read as 42.
    '''

    with open(filename, 'r') as f:

        combinations = []
        for combo in f:
            direction, value = combo.strip()[0], combo.strip()[1:]
            if direction == 'L':
                combinations.append(int(value)*-1)
            elif direction == 'R':
                combinations.append(int(value))
            else:
                print(f'Invalid entry {combo}!')
                pass

    return combinations

def crack_password_method1(combinations: List, start_pos: int = 50) -> int:
    '''
    Use the list of combinations to decypher the password, which is the
    number of times the dial reads exactly 0. The dial goes from 0 to 99.
    '''

    password = 0
    # stepping through combinations to get new dial positions and check for 0s
    for combo in combinations:

        new_pos = start_pos + combo

        # if the new position goes beyond 0-99, adjust the position by
        # getting the remnant via mod 100
        new_pos = new_pos%100

        # increments the password value if the dial is exactly at 0
        if new_pos == 0:
            password +=1

        # updates the dial position after applying the current combo
        start_pos = new_pos

    return password

def crack_password_method2(combinations: List, start_pos: int = 50) -> int:
    '''
    Use the list of combinations to decypher the password, which is the
    number of times the dial crosses 0. The dial goes from 0 to 99.
    '''

    password = 0
    # stepping through combinations to get new dial positions and check for 0s
    for combo in combinations:

        new_pos = start_pos + combo

        # if the new position lands exactly at 0, 0 is crossed and it's counted
        if new_pos == 0 and combo != 0:
            password += 1

        # if the new position is >99, 0 will be crossed //100 times
        if new_pos > 99:
            n_cycles = new_pos//100
            password += n_cycles

        # if the new position is < 0, 0 will be crossed //-100 + 1 times, unless
        # we start at 0, which doesn't count as a crossing so //-100
        if new_pos < 0:
            n_cycles = new_pos//-100 if start_pos == 0 else new_pos//-100 + 1
            password += n_cycles

        start_pos = new_pos%100

    return password

def run_tests(start_pos: int = 50) -> None:

    combos = read_combinations('data/day1_test.txt')

    password1 = crack_password_method1(combos, start_pos)
    password2 = crack_password_method2(combos, start_pos)

    assert password1 == 3
    assert password2 == 6

def main():

    run_tests()

    combos = read_combinations('data/day1_input.txt')

    password1 = crack_password_method1(combos, start_pos = 50)
    password2 = crack_password_method2(combos, start_pos = 50)

    print(f'The password to open the door with initial method is {password1}.')
    print(f'The actual password to open the door is {password2}.')

if __name__ == '__main__':
    main()
