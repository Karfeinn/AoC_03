def battery_input():
    with open("battery.txt", mode="r", encoding="utf-8") as file:
        batteries = file.read().split("\n")
    return batteries

def find_largest_joltage(battery):
    battery = [int(character) for character in list(battery)] 
    largest_joltage = []
    nb_remaining_digits = 12
    index_max = 0
    while nb_remaining_digits > 0:
        window = len(battery) - (nb_remaining_digits -1)
        max_window_digit = max(battery[index_max:window])
        largest_joltage.append(max_window_digit)
        index_max = battery.index(max_window_digit, index_max) + 1
        nb_remaining_digits -= 1
    largest_joltage_str = list(map(str, largest_joltage))
    largest_joltage = int("".join(largest_joltage_str))
    return largest_joltage

def function():
    batteries = battery_input()
    joltage_list = []
    for battery in batteries:
        joltage_list.append(find_largest_joltage(battery))
    print(sum(joltage_list))

function()