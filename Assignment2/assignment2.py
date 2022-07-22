def brush(x):
    global brush_position, car_position_y, car_position_x
    if x == 1:
        brush_position = 1
        paint()
    elif x == 2:
        brush_position = 0


def error_catcher(x):
    a = False
    error_value = False
    try:
        for e in x:
            int(e)
    except:
        a = True

    if not a:
        y = x.copy()
        x.pop(0)
        for e in x:

            if int(y[0]) > 0 and e in ["0","1","2","3","4","6","7","8"]:

                error_value = False

            elif e[0] == "5":
                if e[1] == "_":
                    error_value = False

            else:
                error_value = True
                break
    else:
        error_value = True

    return error_value


def turn(q):
    global direction

    if q == 3:
        direction += 1
        direction %= 4
    elif q == 4:

        direction += 3
        direction %= 4


def overflow():
    global car_position_y, car_position_x

    if car_position_y <= 0:
        car_position_y += frame_length
    car_position_y %= frame_length + 1

    if car_position_x >= frame_length + 1:
        car_position_x += frame_length + 2
    car_position_x %= frame_length + 1

    if car_position_y >= frame_length + 1:
        car_position_y += frame_length + 2
    car_position_y %= frame_length + 1

    if car_position_x <= 0:
        car_position_x += frame_length
    car_position_x %= frame_length + 1


def paint():
    global car_position_x, car_position_y, brush_position
    if brush_position == 1:
        arr[car_position_y][car_position_x] = "*"


def move(o):
    global direction, car_position_y, car_position_x, brush_position
    if direction == 0:
        for i in range(o):
            car_position_y -= 1
            overflow()
            paint()
    elif direction == 1:
        for i in range(o):
            car_position_x += 1
            overflow()
            paint()
    elif direction == 2:
        for i in range(o):
            car_position_y += 1
            overflow()
            paint()
    elif direction == 3:
        for i in range(o):
            car_position_x -= 1
            overflow()
            paint()


def jump():
    global brush_position, car_position_y, car_position_x
    brush_position = 0
    move(3)


def reverse():
    global direction
    direction += 2
    direction %= 4


def view():
    global arr
    for a in range(frame_length+2):
        arr[0][a] = "+"
        arr[frame_length+1][a] = "+"
        arr[a][0] = "+"
        arr[a][frame_length+1] = "+"

    for r in range(frame_length+2):
        p = "".join(arr[r])
        print(p)


print("""<-----RULES----->
1. BRUSH DOWN
2. BRUSH UP
3. VEHICLE ROTATES RIGHT
4. VEHICLE ROTATES LEFT
5. MOVE UP TO X
6. JUMP
7. REVERSE DIRECTION
8. VIEW TE MATRIX
0. EXIT""")
print("Please enter the commands with a plus sign(+) between them.")
while True:
    user_input = input()
    l_user_input = list(user_input.split("+"))
    l_commands = l_user_input.copy()
    l_commands.pop(0)
    frame_length = int(l_user_input[0])
    rows, columns = (frame_length + 2, frame_length + 2)
    arr = []
    zero_checker = False
    car_position_x = 1
    car_position_y = 1
    direction = 1
    brush_position = 0
    for i in range(rows):
        column = []
        for c in range(columns):
            column.append(" ")
        arr.append(column)
    if error_catcher(l_user_input):
        print("You entered an incorrect command. Please try again!")
        continue
    else:
        for e in l_commands:
            if e == "0":
                print("Program has ended.")
                zero_checker = True
                break
            elif e == "1" or e == "2":
                brush(int(e))

            elif e == "3" or e == "4":
                turn(int(e))

            elif e[0] == "5" and e[1] == "_":
                move(int(e[2:]))

            elif e == "6":
                jump()

            elif e == "7":
                reverse()

            elif e == "8":
                view()
    if zero_checker:
        break
