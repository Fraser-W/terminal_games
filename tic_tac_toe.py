import sys

print("""
        -Tic Tac Toe-
           1. x goes first
           2. use 1-9 to place token.
           3. Use a numpad as reference
               789
               456
               123
           4. Have fun


              |   |
           ---+---+---
              |   |
           ---+---+---
              |   |


""")


# Slots start empty
one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "

def main():
    # Resets pieces for new game

    # Turn
    turn = "x"
    for i in range(9):
        # Check for win before continue

        pos = get_grid_pos(turn)
        while save_moves(pos, turn) == False:
            print_grid()
            print("           Try Gain")
            pos = get_grid_pos(turn)

        print_grid()

        if check_for_win():
            retry()


        if turn == "x":
            turn = "o"
        else:
            turn = "x"

    print("Tie!")
    retry()


def get_grid_pos(turn):
    pos = input(f"           {turn}'s Turn: ")
    return pos

def retry():
    retry = input("           Retry? (y/n): ")
    if retry == "y":
        global one
        global two
        global three
        global four
        global five
        global six
        global seven
        global eight
        global nine
        one = " "
        two = " "
        three = " "
        four = " "
        five = " "
        six = " "
        seven = " "
        eight = " "
        nine = " "
        print_grid()
        main()
    elif retry == "n":
        sys.exit()

def check_for_win():

    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

    # 1,2,3
    if one == two == three == "x":
        print("           X wins")
        return True
    elif one == two == three == "o":
        print("           O wins")
        return True

    # 4,5,6
    if four == five == six == "x":
        print("           X wins")
        return True
    elif four == five == six == "o":
        print("           O wins")
        return True

    # 7,8,9
    if seven == eight == nine == "x":
        print("           X wins")
        return True
    elif seven == eight == nine == "o":
        print("           O wins")
        return True

    # 1,4,7
    if one == four == seven == "x":
        print("           X wins")
        return True
    elif one == four == seven == "o":
        print("           O wins")
        return True

    # 2,5,8
    if two == five == eight == "x":
        print("           X wins")
        return True
    elif two == five == eight == "o":
        print("           O wins")
        return True

    # 3,6,9
    if three == six == nine == "x":
        print("           X wins")
        return True
    elif three == six == nine == "o":
        print("           O wins")
        return True

    # 1,5,9
    if one == five == nine == "x":
        print("           X wins")
        return True
    elif one == five == nine == "o":
        print("           O wins")
        return True

    # 7,5,3
    if seven == five == three == "x":
        print("           X wins")
        return True
    elif seven == five == three == "o":
        print("           O wins")
        return True


def save_moves(pos, turn):
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

    if pos == "1":
        if one != " ":
            return False
        else:
            one = turn
            return True
    elif pos == "2":
        if two != " ":
            return False
        else:
            two = turn
            return True
    elif pos == "3":
        if three != " ":
            return False
        else:
            three = turn
            return True
    elif pos == "4":
        if four != " ":
            return False
        else:
            four = turn
            return True
    elif pos == "5":
        if five != " ":
            return False
        else:
            five = turn
            return True
    elif pos == "6":
        if six != " ":
            return False
        else:
            six = turn
            return True
    elif pos == "7":
        if seven != " ":
            return False
        else:
            seven = turn
            return True
    elif pos == "8":
        if eight != " ":
            return False
        else:
            eight = turn
            return True
    elif pos == "9":
        if nine != " ":
            return False
        else:
            nine = turn
            return True
    else:
        return False

def print_grid():
    print(f"""


            {seven} | {eight} | {nine}
           ---+---+---
            {four} | {five} | {six}
           ---+---+---
            {one} | {two} | {three}


        """)

main()
