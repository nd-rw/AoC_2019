from pathlib import Path

def read_puzzle_input(file_path):
    text = Path(file_path).read_text()
    filtered_input_list = list(map(int, list(filter(lambda x: x != '', text.split("\n")))))
    return filtered_input_list

def fuel_calc(mass):
    fuel_req = int(mass/3) -2
    return fuel_req

def calculate_fuel(puzzle_input):
    req_fuel_list = list()
    for mass in puzzle_input:
        req_fuel_list.append(fuel_calc(mass))
    total_fuel_req = sum(req_fuel_list)
    return total_fuel_req

puzzle_input = read_puzzle_input('input.txt')
total_fuel_req = calculate_fuel(puzzle_input)
print('total fuel required: ' + str(total_fuel_req))