def battery_input():
    with open("battery.txt", mode="r", encoding="utf-8") as file:
        batteries = file.read().split("\n")
    return batteries

def find_largest_joltage(battery):
    max_jolt = 0
    max_index = -1

    max_secondary_jolt = 0

    for i in range(0, len(battery)-1): # on ne prends pas le dernier exprès
        if int(battery[i]) > max_jolt :
            max_jolt = int(battery[i])
            max_index = i

    for j in range(max_index + 1, len(battery)):
        if int(battery[j]) > max_secondary_jolt :
            max_secondary_jolt = int(battery[j])
    
    return(int(str(max_jolt)+str(max_secondary_jolt)))

def function():
    batteries = battery_input()
    joltage_list = []
    for battery in batteries:
        joltage_list.append(find_largest_joltage(battery))
    print(sum(joltage_list))

function()