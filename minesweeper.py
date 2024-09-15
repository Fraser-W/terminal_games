import random
import sys

#Global Variables
array2d = []
hidden_array2d = []
game_end = False
# -1 = MINE, 0 = EMPTY, 1 = NUMBER
symbols = {"MINE": 0, "HIDDEN": ".", "EMPTY": " ", "FLAG": "F", "UNKNOWN": "?"}
mines_to_find = 0



def main():
    global game_end
    global mines_to_find

    game_end = False
    gridSize = grid_size()
    create2dArray(gridSize)
    if gridSize == 8:
        mines_to_find = 10
    else:
        mines_to_find = 40

    #first input here
    #pass 'first input' into spawn mines and ensure that spot is skipped of being a mine
    spawn_mines(gridSize)
    #print(hidden_array2d)
    while game_end == False:
        print_grid(gridSize)
        grid_pos = player_input()
        choose_action(grid_pos[0],grid_pos[1],gridSize)

def win_check(gridSize):
    number_count_hidden = 0
    number_count_visible = 0
    for i in range(gridSize):
        for j in range(gridSize):
            if hidden_array2d[j][i] > 0:
                number_count_hidden += 1
            if isinstance(array2d[j][i], int):
                number_count_visible += 1
    if number_count_hidden == number_count_visible:
        print("Victory!")
        retry()


def player_input():
    tile = []
    correct_grid = False
    while correct_grid == False:
        choice = input("Choose a tile (yx):")
        if choice.isalpha() == False and len(choice) == 2:
            for i in choice:
                tile.append(int(i))
            correct_grid = True
        elif choice.isalpha() == False and len(choice) == 4:
            tile.append(int(choice[0]) + (int(choice[1]) + 9))
            tile.append(int(choice[2]) + (int(choice[3]) + 9))
            correct_grid = True
    return tile

def retry():
    global array2d
    global hidden_array2d
    retry = input("Retry? (y/n): ")
    if retry == "y":
        array2d.clear()
        hidden_array2d.clear()
        main()
    elif retry == "n":
        sys.exit()


def check_grid(y,x,gridSize):
    global game_end
    # If mine, show all mines
    if hidden_array2d[y][x] == -1:
        for i in range(gridSize):
            for j in range(gridSize):
                if hidden_array2d[j][i] == -1:
                    array2d[j][i] = '0'
        print_grid(gridSize)
        print("Defeat :(")
        game_end = True
        retry()
    elif hidden_array2d[y][x] == 0:
        array2d[y][x] = symbols["EMPTY"]
        check_blanks(gridSize)
    elif hidden_array2d[y][x] > 0:
        array2d[y][x] = hidden_array2d[y][x]


def check_blanks(gridSize):
    for i in range(gridSize):
        for j in range(gridSize):
            if array2d[i][j] == symbols["EMPTY"]:
                reveal_surrounding(i,j,gridSize)

    for i in reversed(range(gridSize)):
        for j in reversed(range(gridSize)):
            if array2d[i][j] == symbols["EMPTY"]:
                reveal_surrounding(i,j,gridSize)



def reveal_surrounding(y,x,gridSize):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (0 <= (y+i) <= (gridSize-1)) and (0 <= (x+j) <= (gridSize-1)) and array2d[y+i][x+j] is not None:
                if hidden_array2d[y+i][x+j] == 0:
                    array2d[y+i][x+j] = symbols["EMPTY"]
                else:
                    array2d[y+i][x+j] = hidden_array2d[y+i][x+j]

def choose_action(y,x,gridSize):
    global mines_to_find
    choice = False
    while choice == False:
        action = input("Would you like to 'click' (C), 'flag' (F)', or mark unsure (?):")
        if action.upper() == symbols["FLAG"]:
            if array2d[y][x] == symbols["FLAG"]:
                array2d[y][x] = symbols["HIDDEN"]
                mines_to_find += 1
                choice = True
            elif array2d[y][x] == symbols["HIDDEN"]:
                array2d[y][x] = symbols["FLAG"]
                mines_to_find -= 1
                choice = True
            else:
                choice = False
                continue

        elif action.upper() == 'C':
            check_grid(y,x,gridSize)
            win_check(gridSize)
            choice = True

        elif action == symbols["UNKNOWN"]:
            if array2d[y][x] == symbols["UNKNOWN"]:
                array2d[y][x] = symbols["HIDDEN"]
                choice = True
            elif array2d[y][x] == symbols["HIDDEN"]:
                array2d[y][x] = symbols["UNKNOWN"]
                choice = True
            else:
                choice = False
                continue


def grid_size():
    accurate_grid_size = False
    while accurate_grid_size == False:
        grid_size = input("8x8 Grid with 10 Mines or 16x16 with 40 mines? (8/16):")
        if grid_size.isalpha() == False:
            grid_size = int(grid_size)
        if grid_size == 8 or grid_size == 16:
            accurate_grid_size = True
    return grid_size


def create2dArray(size):
    #Grid sizes

    x, y = size, size
    global array2d
    global hidden_array2d
    # Creates visible array
    for i in range(x):
        array = []
        for j in range(y):
            array.append(symbols["HIDDEN"])
        array2d.append(array)

    # Fills hidden array with 0's
    for i in range(x):
        array = []
        for j in range(y):
            array.append(0)
        hidden_array2d.append(array)

def spawn_mines(gridSize):
    global numbers_array
    global hidden_array2d

    # Set Mine Count
    mine_count = 10
    if gridSize != 8:
        mine_count = 40

    temp_mine_count = mine_count
    # Fill with mines
    while temp_mine_count > 0:
        y = random.randint(0, gridSize - 1)
        x = random.randint(0, gridSize - 1)
        if hidden_array2d[y][x] != -1:
            hidden_array2d[y][x] = -1
            temp_mine_count -= 1


    # Fill with numbers
    for i in range(gridSize):
        for j in range(gridSize):
            if hidden_array2d[j][i] == -1:
                # Up, down, left, right
                if j-1 >= 0 and hidden_array2d[j-1][i] is not None and hidden_array2d[j-1][i] != -1:
                    hidden_array2d[j-1][i] = 1
                if j+1 < gridSize and hidden_array2d[j+1][i] is not None and hidden_array2d[j+1][i] != -1:
                    hidden_array2d[j+1][i] = 1
                if i-1 >= 0 and hidden_array2d[j][i-1] is not None and hidden_array2d[j][i-1] != -1:
                    hidden_array2d[j][i-1] = 1
                if i+1 < gridSize and hidden_array2d[j][i+1] is not None and hidden_array2d[j][i+1] != -1:
                    hidden_array2d[j][i+1] = 1
                # Diagonals
                if j-1 >= 0 and i-1 >= 0 and hidden_array2d[j-1][i-1] is not None and hidden_array2d[j-1][i-1] != -1:
                    hidden_array2d[j-1][i-1] = 1
                if j+1 < gridSize and i+1 < gridSize and hidden_array2d[j+1][i+1] is not None and hidden_array2d[j+1][i+1] != -1:
                    hidden_array2d[j+1][i+1] = 1
                if j+1 < gridSize and i-1 >= 0 and hidden_array2d[j+1][i-1] is not None and hidden_array2d[j+1][i-1] != -1:
                    hidden_array2d[j+1][i-1] = 1
                if j-1 >= 0 and i+1 < gridSize and hidden_array2d[j-1][i+1] is not None and hidden_array2d[j-1][i+1] != -1:
                    hidden_array2d[j-1][i+1] = 1
            else:
                continue

    # Fill numbers and changes count to correctly include amount of mines touching
    for i in range(gridSize):
        for j in range(gridSize):
            counter = 0
            if hidden_array2d[j][i] == 1:
                # Up, down, left, right
                if (j-1 >= 0 and hidden_array2d[j-1][i] is not None and hidden_array2d[j-1][i] == -1):
                    counter += 1
                if (j+1 < gridSize and hidden_array2d[j+1][i] is not None and hidden_array2d[j+1][i] == -1):
                    counter += 1
                if (i-1 >= 0 and hidden_array2d[j][i-1] is not None and hidden_array2d[j][i-1] == -1):
                    counter += 1
                if (i+1 < gridSize and hidden_array2d[j][i+1] is not None and hidden_array2d[j][i+1] == -1):
                    counter += 1
                if (j-1 >= 0 and i-1 >= 0 and hidden_array2d[j-1][i-1] is not None and hidden_array2d[j-1][i-1] == -1):
                    counter += 1
                if (j+1 < gridSize and i+1 < gridSize and hidden_array2d[j+1][i+1] and hidden_array2d[j+1][i+1] == -1):
                    counter += 1
                if (j+1 < gridSize and i-1 >= 0 and hidden_array2d[j+1][i-1] is not None and hidden_array2d[j+1][i-1] == -1):
                    counter += 1
                if (j-1 >= 0 and i+1 < gridSize and hidden_array2d[j-1][i+1] is not None and hidden_array2d[j-1][i+1] == -1):
                    counter += 1
                hidden_array2d[j][i] = counter




def print_grid(size):

    if size == 8:
        print(f"""

    yx--  0   1   2   3   4   5   6   7
    |     |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+
   0 -- | {array2d[0][0]} | {array2d[0][1]} | {array2d[0][2]} | {array2d[0][3]} | {array2d[0][4]} | {array2d[0][5]} | {array2d[0][6]} | {array2d[0][7]} |   MINES: {mines_to_find}
        +---+---+---+---+---+---+---+---+
   1 -- | {array2d[1][0]} | {array2d[1][1]} | {array2d[1][2]} | {array2d[1][3]} | {array2d[1][4]} | {array2d[1][5]} | {array2d[1][6]} | {array2d[1][7]} |
        +---+---+---+---+---+---+---+---+
   2 -- | {array2d[2][0]} | {array2d[2][1]} | {array2d[2][2]} | {array2d[2][3]} | {array2d[2][4]} | {array2d[2][5]} | {array2d[2][6]} | {array2d[2][7]} |
        +---+---+---+---+---+---+---+---+
   3 -- | {array2d[3][0]} | {array2d[3][1]} | {array2d[3][2]} | {array2d[3][3]} | {array2d[3][4]} | {array2d[3][5]} | {array2d[3][6]} | {array2d[3][7]} |
        +---+---+---+---+---+---+---+---+
   4 -- | {array2d[4][0]} | {array2d[4][1]} | {array2d[4][2]} | {array2d[4][3]} | {array2d[4][4]} | {array2d[4][5]} | {array2d[4][6]} | {array2d[4][7]} |
        +---+---+---+---+---+---+---+---+
   5 -- | {array2d[5][0]} | {array2d[5][1]} | {array2d[5][2]} | {array2d[5][3]} | {array2d[5][4]} | {array2d[5][5]} | {array2d[5][6]} | {array2d[5][7]} |
        +---+---+---+---+---+---+---+---+
   6 -- | {array2d[6][0]} | {array2d[6][1]} | {array2d[6][2]} | {array2d[6][3]} | {array2d[6][4]} | {array2d[6][5]} | {array2d[6][6]} | {array2d[6][7]} |
        +---+---+---+---+---+---+---+---+
   7 -- | {array2d[7][0]} | {array2d[7][1]} | {array2d[7][2]} | {array2d[7][3]} | {array2d[7][4]} | {array2d[7][5]} | {array2d[7][6]} | {array2d[7][7]} |
        +---+---+---+---+---+---+---+---+

            """)

    else:
        print(f"""
    yx--  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
    |     |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   0 -- | {array2d[0][0]} | {array2d[0][1]} | {array2d[0][2]} | {array2d[0][3]} | {array2d[0][4]} | {array2d[0][5]} | {array2d[0][6]} | {array2d[0][7]} | {array2d[0][8]} | {array2d[0][9]} | {array2d[0][10]} | {array2d[0][11]} | {array2d[0][12]} | {array2d[0][13]} | {array2d[0][14]} | {array2d[0][15]} |   MINES: {mines_to_find}
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   1 -- | {array2d[1][0]} | {array2d[1][1]} | {array2d[1][2]} | {array2d[1][3]} | {array2d[1][4]} | {array2d[1][5]} | {array2d[1][6]} | {array2d[1][7]} | {array2d[1][8]} | {array2d[1][9]} | {array2d[1][10]} | {array2d[1][11]} | {array2d[1][12]} | {array2d[1][13]} | {array2d[1][14]} | {array2d[1][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   2 -- | {array2d[2][0]} | {array2d[2][1]} | {array2d[2][2]} | {array2d[2][3]} | {array2d[2][4]} | {array2d[2][5]} | {array2d[2][6]} | {array2d[2][7]} | {array2d[2][8]} | {array2d[2][9]} | {array2d[2][10]} | {array2d[2][11]} | {array2d[2][12]} | {array2d[2][13]} | {array2d[2][14]} | {array2d[2][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   3 -- | {array2d[3][0]} | {array2d[3][1]} | {array2d[3][2]} | {array2d[3][3]} | {array2d[3][4]} | {array2d[3][5]} | {array2d[3][6]} | {array2d[3][7]} | {array2d[3][8]} | {array2d[3][9]} | {array2d[3][10]} | {array2d[3][11]} | {array2d[3][12]} | {array2d[3][13]} | {array2d[3][14]} | {array2d[3][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   4 -- | {array2d[4][0]} | {array2d[4][1]} | {array2d[4][2]} | {array2d[4][3]} | {array2d[4][4]} | {array2d[4][5]} | {array2d[4][6]} | {array2d[4][7]} | {array2d[4][8]} | {array2d[4][9]} | {array2d[4][10]} | {array2d[4][11]} | {array2d[4][12]} | {array2d[4][13]} | {array2d[4][14]} | {array2d[4][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   5 -- | {array2d[5][0]} | {array2d[5][1]} | {array2d[5][2]} | {array2d[5][3]} | {array2d[5][4]} | {array2d[5][5]} | {array2d[5][6]} | {array2d[5][7]} | {array2d[5][8]} | {array2d[5][9]} | {array2d[5][10]} | {array2d[5][11]} | {array2d[5][12]} | {array2d[5][13]} | {array2d[5][14]} | {array2d[5][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   6 -- | {array2d[6][0]} | {array2d[6][1]} | {array2d[6][2]} | {array2d[6][3]} | {array2d[6][4]} | {array2d[6][5]} | {array2d[6][6]} | {array2d[6][7]} | {array2d[6][8]} | {array2d[6][9]} | {array2d[6][10]} | {array2d[6][11]} | {array2d[6][12]} | {array2d[6][13]} | {array2d[6][14]} | {array2d[6][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   7 -- | {array2d[7][0]} | {array2d[7][1]} | {array2d[7][2]} | {array2d[7][3]} | {array2d[7][4]} | {array2d[7][5]} | {array2d[7][6]} | {array2d[7][7]} | {array2d[7][8]} | {array2d[7][9]} | {array2d[7][10]} | {array2d[7][11]} | {array2d[7][12]} | {array2d[7][13]} | {array2d[7][14]} | {array2d[7][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   8 -- | {array2d[8][0]} | {array2d[8][1]} | {array2d[8][2]} | {array2d[8][3]} | {array2d[8][4]} | {array2d[8][5]} | {array2d[8][6]} | {array2d[8][7]} | {array2d[8][8]} | {array2d[8][9]} | {array2d[8][10]} | {array2d[8][11]} | {array2d[8][12]} | {array2d[8][13]} | {array2d[8][14]} | {array2d[8][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   9 -- | {array2d[9][0]} | {array2d[9][1]} | {array2d[9][2]} | {array2d[9][3]} | {array2d[9][4]} | {array2d[9][5]} | {array2d[9][6]} | {array2d[9][7]} | {array2d[9][8]} | {array2d[9][9]} | {array2d[9][10]} | {array2d[9][11]} | {array2d[9][12]} | {array2d[9][13]} | {array2d[9][14]} | {array2d[9][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  10 -- | {array2d[10][0]} | {array2d[10][1]} | {array2d[10][2]} | {array2d[10][3]} | {array2d[10][4]} | {array2d[10][5]} | {array2d[10][6]} | {array2d[10][7]} | {array2d[10][8]} | {array2d[10][9]} | {array2d[10][10]} | {array2d[10][11]} | {array2d[10][12]} | {array2d[10][13]} | {array2d[10][14]} | {array2d[10][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  11 -- | {array2d[11][0]} | {array2d[11][1]} | {array2d[11][2]} | {array2d[11][3]} | {array2d[11][4]} | {array2d[11][5]} | {array2d[11][6]} | {array2d[11][7]} | {array2d[11][8]} | {array2d[11][9]} | {array2d[11][10]} | {array2d[11][11]} | {array2d[11][12]} | {array2d[11][13]} | {array2d[11][14]} | {array2d[11][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  12 -- | {array2d[12][0]} | {array2d[12][1]} | {array2d[12][2]} | {array2d[12][3]} | {array2d[12][4]} | {array2d[12][5]} | {array2d[12][6]} | {array2d[12][7]} | {array2d[12][8]} | {array2d[12][9]} | {array2d[12][10]} | {array2d[12][11]} | {array2d[12][12]} | {array2d[12][13]} | {array2d[12][14]} | {array2d[12][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  13 -- | {array2d[13][0]} | {array2d[13][1]} | {array2d[13][2]} | {array2d[13][3]} | {array2d[13][4]} | {array2d[13][5]} | {array2d[13][6]} | {array2d[13][7]} | {array2d[13][8]} | {array2d[13][9]} | {array2d[13][10]} | {array2d[13][11]} | {array2d[13][12]} | {array2d[13][13]} | {array2d[13][14]} | {array2d[13][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  14 -- | {array2d[14][0]} | {array2d[14][1]} | {array2d[14][2]} | {array2d[14][3]} | {array2d[14][4]} | {array2d[14][5]} | {array2d[14][6]} | {array2d[14][7]} | {array2d[14][8]} | {array2d[14][9]} | {array2d[14][10]} | {array2d[14][11]} | {array2d[14][12]} | {array2d[14][13]} | {array2d[14][14]} | {array2d[14][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  15 -- | {array2d[15][0]} | {array2d[15][1]} | {array2d[15][2]} | {array2d[15][3]} | {array2d[15][4]} | {array2d[15][5]} | {array2d[15][6]} | {array2d[15][7]} | {array2d[15][8]} | {array2d[15][9]} | {array2d[15][10]} | {array2d[15][11]} | {array2d[15][12]} | {array2d[15][13]} | {array2d[15][14]} | {array2d[15][15]} |
        +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
          """)


main()
