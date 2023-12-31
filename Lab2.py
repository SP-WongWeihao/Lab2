def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    x = input()
    numbers = x.split(",")
    number_list = list(map(float, numbers))
    return number_list

def calc_average(num_list):
    total = 0
    for x in num_list:
        total += x
    avg = total/len(num_list)
    return avg

def calc_min_max(list):
    min_num = int(min(list))
    max_num = int(max(list))

    return min_num,max_num

def calc_median_temperature(list):
    list.sort()
    if ((len(list)) % 2) != 0:
        median = list[int((len(list)-1)/2)]
        return median
    else:
        median = (list[int(len(list)/2) - 1] + list[int((len(list)/2))])/2
        return median


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Average Temperature: " + str(calc_average(num_list)))
    print("Min Temperature, Max Temperature: " + str(calc_min_max(num_list)))
    print("Median Temperature: " + str(calc_median_temperature(num_list)))

if __name__ == "__main__":
    main()
