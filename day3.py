from typing import List

def read_banks(filename: str) -> List:

    with open(filename, 'r') as f:
        banks = [list(bank.strip()) for bank in f]

    return banks

def get_bank_joltage(bank: List, n_batteries=2) -> int:

    activated_batteries = []

    n_bank = len(bank)

    start_ind = 0

    for n_remaining in range(n_batteries,0,-1):

        end_ind = n_bank - n_remaining + 1

        subbank = bank[start_ind:end_ind]

        maxbattery = max(subbank)
        maxind = subbank.index(maxbattery)

        activated_batteries.append(maxbattery)

        start_ind += maxind+1

    joltage = ''
    for battery in activated_batteries:
        joltage += battery


    return int(joltage)

    '''
    og, non-general solution
    max_battery = max(bank)
    if max_battery == '1':
        return 11

    max_index = bank.index(max_battery)

    if max_index == len(bank)-1:
        second_battery = max_battery
        first_battery = max(bank[:-1])
    else:
        first_battery = max_battery
        second_battery = max(bank[max_index+1:])

    return int(first_battery + second_battery)
    '''

def get_max_joltage(banks: List, n_batteries=2) -> int:

    max_joltage = 0
    for bank in banks:
        max_joltage += get_bank_joltage(bank, n_batteries=n_batteries)

    return max_joltage


def run_test():

    banks = read_banks('data/day3_test.txt')
    max_joltage_2 = get_max_joltage(banks, n_batteries=2)
    max_joltage_12 = get_max_joltage(banks, n_batteries=12)
    assert max_joltage_2 == 357
    assert max_joltage_12 == 3121910778619
    print('Tests passed!')


def main():


    run_test()

    banks = read_banks('data/day3_input.txt')
    max_joltage_2 = get_max_joltage(banks, n_batteries = 2)
    max_joltage_12 = get_max_joltage(banks, n_batteries = 12)
    print(f'Maximum joltage for 2 batteries is {max_joltage_2}.')
    print(f'Maximum joltage for 12 batteries is {max_joltage_12}.')


if __name__ == '__main__':
    main()
