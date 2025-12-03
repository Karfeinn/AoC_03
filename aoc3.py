def battery_input():
    with open("test.txt", mode="r", encoding="utf-8") as file:
        batteries = file.read().split("\n")
    return batteries

def find_largest_joltage(battery):
    battery_list = list(battery)
    dict_activate = {}
    i = "9"
    while len(dict_activate) != 12:
        b = False
        for index, x in enumerate(reversed(battery_list)) :
            true_index = len(battery_list) - 1 - index
            if x == i :
                if dict_activate.get(true_index, 0) != 0 :
                    continue
                if dict_activate :
                    if dict_activate[min(dict_activate)] > i and len(battery_list)-1 - min(dict_activate) > 12 - len(dict_activate) and min(dict_activate) > true_index:
                        continue
                dict_activate[true_index] = x
                b = True
                break
        if b :
            continue
        i = str(int(i) - 1)
    return dict_activate

def get_largest_joltage(battery):
    list_activate = sorted(find_largest_joltage(battery).items())
    voltage = ""
    for values in list_activate:
        voltage = voltage + values[1]
    print(voltage)
    return int(voltage)

def function():
    batteries = battery_input()
    joltage_list = []
    for battery in batteries:
        joltage_list.append(get_largest_joltage(battery))
    print(sum(joltage_list))

function()