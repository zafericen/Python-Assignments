import sys


def finding_neighbors(row, collum):
    list_of_neighbors = []
    dict_of_map = {(i3, c): list_matrix[i3][c] for i3 in range(len(list_matrix)) for c in range(len(list_matrix[-1]))}
    for i2 in [(row, collum+1), (row+1, collum), (row-1, collum), (row, collum-1)]:
        if i2 in dict_of_map.keys():
            list_of_neighbors.append(i2)
    return list_of_neighbors


def error_catcher(input_coordinates):
    try:
        a, b = int(input_coordinates[0]), int(input_coordinates[1])
        c = list_matrix[a][b]
        assert list_matrix[a][b] != " "
    except:
        return True
    return False


def same_neighbors(location):
    location_list = [location]
    remove_list, location_list_control = location_list.copy(), location_list.copy()
    wanted_color = list_matrix[location[0]][location[1]]
    while True:
        for i in remove_list:
            temp_list_neighbors = finding_neighbors(i[0], i[1])
            for i2 in temp_list_neighbors:
                if list_matrix[i2[0]][i2[1]] == wanted_color:
                    location_list.append(i2)
        for i in location_list:
            if i not in remove_list:
                remove_list.append(tuple(i))
        if location_list_control == location_list:
            return remove_list
        location_list_control = location_list.copy()
        location_list = []


def score_calculator(remove_list):
    score_dict = {"B": 9, "G": 8, "W": 7, "Y": 6, "R": 5, "P": 4, "O": 3, "D": 2, "F": 1, "X*": 0, " ": 0}
    score = 0
    for i in remove_list:
        score += score_dict[list_matrix[i[0]][i[1]]]
    return score


def bomb(location):
    remove_list = []
    list_matrix[location[0]][location[1]] = "X*"
    for i in range(len(list_matrix[location[0]])):
        remove_list.append((location[0], i))
    for i in range(len(list_matrix)):
        remove_list.append((i, location[1]))
    for i in remove_list:
        if list_matrix[i[0]][i[1]] == "X":
            remove_list = remove_list + bomb(i)
    remove_list = list(set(remove_list))
    remove_list.sort()
    return remove_list


def space_adder(remove_list):
    for i in remove_list:
        list_matrix[i[0]][i[1]] = " "


def deleter():
    number_of_lines = 0
    for i in range(len(list_matrix)):
        if list_matrix[i].count(" ") == len(list_matrix[i]):
            number_of_lines += 1
    for i in [0]*number_of_lines:
        list_matrix.pop(0)


def fall_calculator():
    for i in range(len(list_matrix)-1):
        for y in range(len(list_matrix)-1):
            for x in range(len(list_matrix[y])):
                if list_matrix[y+1][x] == " ":
                    list_matrix[y+1][x] = list_matrix[y][x]
                    list_matrix[y][x] = " "
    for i in range(len(list_matrix[-1])-1):
        for x in range(1, len(list_matrix[-1]))[::-1]:
            flag = 0
            for y in range(len(list_matrix))[::-1]:
                if list_matrix[y][x-1] == " ":
                    flag += 1
            if flag == len(list_matrix):
                for y in range(len(list_matrix))[::-1]:
                    list_matrix[y][x-1] = list_matrix[y][x]
                    list_matrix[y][x] = " "


def view():

    for r in list_matrix:
        print(" ".join(r), end="\n")


def game_over():
    control_value = True
    for y in range(len(list_matrix)):
        for x in range(len(list_matrix[0])):
            if list_matrix[y][x] != " ":
                control_list = same_neighbors((y, x))
                if len(control_list) > 1 or list_matrix[y][x] == "X":
                    control_value = False
                    return control_value
    return control_value


with open(sys.argv[1], "r") as file:
    list_matrix = file.readlines()
    for i in range(len(list_matrix)):
        list_matrix[i] = list_matrix[i].split()
score_value = 0
view()
print("\nYour score is:{}".format(score_value))
while not game_over():
    user_input = input("\nPlease enter a row and collum number: ")
    user_input = user_input.split()
    if error_catcher(user_input):
        print("\nPlease enter a valid size!")
        continue
    coordinates = tuple(map(lambda x: int(x), user_input))
    if list_matrix[coordinates[0]][coordinates[1]] == "X":
        remove_color_list = bomb(coordinates)

    elif len(same_neighbors(coordinates)) == 1:
        print()
        view()
        continue
    else:
        remove_color_list = same_neighbors(coordinates)
    score_value += score_calculator(remove_color_list)
    space_adder(remove_color_list)
    fall_calculator()
    deleter()
    print()
    view()
    print("\nYour score is:{}".format(score_value))
print("\nGame over!")
