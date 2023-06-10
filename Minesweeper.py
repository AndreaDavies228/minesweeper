#!/usr/bin/env python3

import random
import time

def play_again():
    waiting_input = True
    while waiting_input == True:
        again = input("Do you want to play again?")
        if again == "y":
            waiting_input = False
            break
        if again == "n":
            print("Thank you for playing!")
            print("You can donate here to support real life mine clearing operations: https://donorbox.org/halo_trust_ukraine_appeal ")
            exit()
        else:
            print("Invalid input.")

def mine_test(position):
    count = 0
    test1 = False
    test2 = False
    test3 = False
    test4 = False
    test5 = False
    test6 = False
    test7 = False
    test8 = False
    
    if position - movement_value >= 0:
        test1 = position - movement_value
        if test1 in mines:
            count += 1
    if position - movement_value + 1 >= 0 and position % movement_value != (movement_value -1):
        test2 = position - movement_value + 1
        if test2 in mines:
            count += 1
    if position % movement_value != (movement_value -1):
        test3 = position + 1
        if test3 in mines:
            count += 1
    if position + movement_value + 1 < len(positions) and position % movement_value != (movement_value -1):
        test4 = position + movement_value + 1
        if test4 in mines:
            count += 1
    if position + movement_value < len(positions):
        test5 = position + movement_value
        if test5 in mines:
            count += 1
    if position + movement_value -1 < len(positions) and position % movement_value != 0:
        test6 = (position + movement_value - 1)
        if test6 in mines:
            count += 1
    if position % movement_value != 0 and position >= 0:
        test7 = (position - 1)
        if test7 in mines:
            count += 1
    if position - movement_value - 1 >= 0 and position % movement_value != 0:
        test8 = (position - movement_value - 1)
        if test8 in mines:
            count += 1
    values[positions[position]] = str(count) + " "
    if count > 0:
        return    

    else:
        if test1 is not False:
            if values[positions[test1]] == "☐ ":
                mine_test(test1)
                
        if test2 is not False:
            if values[positions[test2]] == "☐ ":
                mine_test(test2)
                
        if test3 is not False:
            if values[positions[test3]] == "☐ ":
                mine_test(test3)
                
        if test4 is not False:
            if values[positions[test4]] == "☐ ":
                mine_test(test4)
                
        if test5 is not False:
            if values[positions[test5]] == "☐ ":
                mine_test(test5)
                
        if test6 is not False:
            if values[positions[test6]] == "☐ ":
                mine_test(test6)
                
        if test7:
            if values[positions[test7]] == "☐ ":
                mine_test(test7)
                
        if test8 is not False:
            if values[positions[test8]] == "☐ ":
                mine_test(test8)
                
    return


def movement(input):
    global is_flag
    global is_number
    global current_position
    if is_flag == True:
        values[positions[current_position]] = "☑ "
    if is_number == True:
        mine_test(current_position)
    else:
        if values[positions[current_position]] == "⬤ ":
            values[positions[current_position]] = "☐ "
    if input == "w":
        if current_position - movement_value >= 0:
            current_position -= movement_value
        else:
            current_position = (current_position + len(positions) - movement_value)
    if input:
        if input == "a":
            if current_position % movement_value == 0:
                current_position += (movement_value -1)
            else:
                current_position -= 1
        if input == "s":
            if current_position + movement_value < len(positions):
                current_position += movement_value
            else:
                current_position = current_position % movement_value
        if input == "d":
            if current_position % movement_value == (movement_value -1):
                current_position -= (movement_value - 1)
            else:
                current_position += 1
    if values[positions[current_position]] == "☑ ":
        is_flag = True
        is_number = False
        values[positions[current_position]] = "⬤ "
        return
    if values[positions[current_position]] == "☐ ":
        is_flag = False
        is_number = False
        values[positions[current_position]] = "⬤ "
        return
    else:
        is_flag = False
        is_number = True
        values[positions[current_position]] = "⬤ "
    return

#☑
#☒
#■
#⬤
#☐
print("Welcome to Minesweeper.")
playing = True
while playing == True:
    size = False
    default_values = {"A1": "☐ ", "B1": "☐ ", "C1": "☐ ", "D1": "☐ ", "E1": "☐ ", "F1": "☐ ", "G1": "☐ ", "H1": "☐ ", "I1": "☐ ", "J1": "☐ ", "K1": "☐ ", "L1": "☐ ",
            "A2": "☐ ", "B2": "☐ ", "C2": "☐ ", "D2": "☐ ", "E2": "☐ ", "F2": "☐ ", "G2": "☐ ", "H2": "☐ ", "I2": "☐ ", "J2": "☐ ", "K2": "☐ ", "L2": "☐ ",
            "A3": "☐ ", "B3": "☐ ", "C3": "☐ ", "D3": "☐ ", "E3": "☐ ", "F3": "☐ ", "G3": "☐ ", "H3": "☐ ", "I3": "☐ ", "J3": "☐ ", "K3": "☐ ", "L3": "☐ ",
            "A4": "☐ ", "B4": "☐ ", "C4": "☐ ", "D4": "☐ ", "E4": "☐ ", "F4": "☐ ", "G4": "☐ ", "H4": "☐ ", "I4": "☐ ", "J4": "☐ ", "K4": "☐ ", "L4": "☐ ",
            "A5": "☐ ", "B5": "☐ ", "C5": "☐ ", "D5": "☐ ", "E5": "☐ ", "F5": "☐ ", "G5": "☐ ", "H5": "☐ ", "I5": "☐ ", "J5": "☐ ", "K5": "☐ ", "L5": "☐ ",
            "A6": "☐ ", "B6": "☐ ", "C6": "☐ ", "D6": "☐ ", "E6": "☐ ", "F6": "☐ ", "G6": "☐ ", "H6": "☐ ", "I6": "☐ ", "J6": "☐ ", "K6": "☐ ", "L6": "☐ ",
            "A7": "☐ ", "B7": "☐ ", "C7": "☐ ", "D7": "☐ ", "E7": "☐ ", "F7": "☐ ", "G7": "☐ ", "H7": "☐ ", "I7": "☐ ", "J7": "☐ ", "K7": "☐ ", "L7": "☐ ",
            "A8": "☐ ", "B8": "☐ ", "C8": "☐ ", "D8": "☐ ", "E8": "☐ ", "F8": "☐ ", "G8": "☐ ", "H8": "☐ ", "I8": "☐ ", "J8": "☐ ", "K8": "☐ ", "L8": "☐ ",
            "A9": "☐ ", "B9": "☐ ", "C9": "☐ ", "D9": "☐ ", "E9": "☐ ", "F9": "☐ ", "G9": "☐ ", "H9": "☐ ", "I9": "☐ ", "J9": "☐ ", "K9": "☐ ", "L9": "☐ ",
            "A10": "☐ ", "B10": "☐ ", "C10": "☐ ", "D10": "☐ ", "E10": "☐ ", "F10": "☐ ", "G10": "☐ ", "H10": "☐ ", "I10": "☐ ", "J10": "☐ ", "K10": "☐ ", "L10": "☐ ",
            "A11": "☐ ", "B11": "☐ ", "C11": "☐ ", "D11": "☐ ", "E11": "☐ ", "F11": "☐ ", "G11": "☐ ", "H11": "☐ ", "I11": "☐ ", "J11": "☐ ", "K11": "☐ ", "L11": "☐ ",
            "A12": "☐ ", "B12": "☐ ", "C12": "☐ ", "D12": "☐ ", "E12": "☐ ", "F12": "☐ ", "G12": "☐ ", "H12": "☐ ", "I12": "☐ ", "J12": "☐ ", "K12": "☐ ", "L12": "☐ "}
    values = default_values
    small = """
    {A1} {B1} {C1} {D1} {E1} {F1} {G1} {H1}
    {A2} {B2} {C2} {D2} {E2} {F2} {G2} {H2}
    {A3} {B3} {C3} {D3} {E3} {F3} {G3} {H3}
    {A4} {B4} {C4} {D4} {E4} {F4} {G4} {H4}
    {A5} {B5} {C5} {D5} {E5} {F5} {G5} {H5}
    {A6} {B6} {C6} {D6} {E6} {F6} {G6} {H6}
    {A7} {B7} {C7} {D7} {E7} {F7} {G7} {H7}
    {A8} {B8} {C8} {D8} {E8} {F8} {G8} {H8}"""
    medium = """
    {A1} {B1} {C1} {D1} {E1} {F1} {G1} {H1} {I1} {J1}
    {A2} {B2} {C2} {D2} {E2} {F2} {G2} {H2} {I2} {J2}
    {A3} {B3} {C3} {D3} {E3} {F3} {G3} {H3} {I3} {J3}
    {A4} {B4} {C4} {D4} {E4} {F4} {G4} {H4} {I4} {J4}
    {A5} {B5} {C5} {D5} {E5} {F5} {G5} {H5} {I5} {J5}
    {A6} {B6} {C6} {D6} {E6} {F6} {G6} {H6} {I6} {J6}
    {A7} {B7} {C7} {D7} {E7} {F7} {G7} {H7} {I7} {J7} 
    {A8} {B8} {C8} {D8} {E8} {F8} {G8} {H8} {I8} {J8}
    {A9} {B9} {C9} {D9} {E9} {F9} {G9} {H9} {I9} {J9}
    {A10} {B10} {C10} {D10} {E10} {F10} {G10} {H10} {I10} {J10}"""
    large = """
    {A1} {B1} {C1} {D1} {E1} {F1} {G1} {H1} {I1} {J1} {K1} {L1}
    {A2} {B2} {C2} {D2} {E2} {F2} {G2} {H2} {I2} {J2} {K2} {L2}
    {A3} {B3} {C3} {D3} {E3} {F3} {G3} {H3} {I3} {J3} {K3} {L3}
    {A4} {B4} {C4} {D4} {E4} {F4} {G4} {H4} {I4} {J4} {K4} {L4}
    {A5} {B5} {C5} {D5} {E5} {F5} {G5} {H5} {I5} {J5} {K5} {L5}
    {A6} {B6} {C6} {D6} {E6} {F6} {G6} {H6} {I6} {J6} {K6} {L6}
    {A7} {B7} {C7} {D7} {E7} {F7} {G7} {H7} {I7} {J7} {K7} {L7}
    {A8} {B8} {C8} {D8} {E8} {F8} {G8} {H8} {I8} {J8} {K8} {L8}
    {A9} {B9} {C9} {D9} {E9} {F9} {G9} {H9} {I9} {J9} {K9} {L9}
    {A10} {B10} {C10} {D10} {E10} {F10} {G10} {H10} {I10} {J10} {K10} {L10}
    {A11} {B11} {C11} {D11} {E11} {F11} {G11} {H11} {I11} {J11} {K11} {L11}
    {A12} {B12} {C12} {D12} {E12} {F12} {G12} {H12} {I12} {J12} {K12} {L12}"""
    while size == False:
        board_size = input("Please press 's', 'm' or 'l' to select your game size: Small, Medium, or Large ")
        if board_size == "Small" or board_size == "small" or board_size == "S" or board_size == "s":
            size = small
            print("Small board size set.")
        elif board_size == "Medium" or board_size == "medium" or board_size == "M" or board_size == "m":
            size = medium
            print("Medium board size set.")
        elif board_size == "Large" or board_size =="large" or board_size =="L" or board_size =="l":
            size = large
            print("Large board size set.")
        else:
            print("Invalid input")
    values["A1"] = "⬤ "
    if size == small:
        positions = ["A1", "B1", "C1", "D1", "E1", "F1","G1", "H1",
                "A2", "B2", "C2", "D2", "E2", "F2","G2", "H2",
                "A3", "B3", "C3", "D3", "E3", "F3","G3", "H3",
                "A4", "B4", "C4", "D4", "E4", "F4","G4", "H4",
                "A5", "B5", "C5", "D5", "E5", "F5","G5", "H5",
                "A6", "B6", "C6", "D6", "E6", "F6","G6", "H6",
                "A7", "B7", "C7", "D7", "E7", "F7","G7", "H7",
                "A8", "B8", "C8", "D8", "E8", "F8","G8", "H8",
                ]
    if size == medium:
            positions = ["A1", "B1", "C1", "D1", "E1", "F1","G1", "H1", "I1", "J1",
                "A2", "B2", "C2", "D2", "E2", "F2","G2", "H2", "I2", "J2",
                "A3", "B3", "C3", "D3", "E3", "F3","G3", "H3", "I3", "J3",
                "A4", "B4", "C4", "D4", "E4", "F4","G4", "H4", "I4", "J4",
                "A5", "B5", "C5", "D5", "E5", "F5","G5", "H5", "I5", "J5",
                "A6", "B6", "C6", "D6", "E6", "F6","G6", "H6", "I6", "J6",
                "A7", "B7", "C7", "D7", "E7", "F7","G7", "H7", "I7", "J7",
                "A8", "B8", "C8", "D8", "E8", "F8","G8", "H8", "I8", "J8",
                "A9", "B9", "C9", "D9", "E9", "F9","G9", "H9", "I9", "J9",
                "A10", "B10", "C10", "D10", "E10", "F10","G10", "H10", "I10", "J10",
                ]
    if size == large:
            positions =  ["A1", "B1", "C1", "D1", "E1", "F1","G1", "H1", "I1", "J1", "K1", "L1",
                "A2", "B2", "C2", "D2", "E2", "F2","G2", "H2", "I2", "J2", "K2", "L2",
                "A3", "B3", "C3", "D3", "E3", "F3","G3", "H3", "I3", "J3", "K3", "L3",
                "A4", "B4", "C4", "D4", "E4", "F4","G4", "H4", "I4", "J4", "K4", "L4",
                "A5", "B5", "C5", "D5", "E5", "F5","G5", "H5", "I5", "J5", "K5", "L5",
                "A6", "B6", "C6", "D6", "E6", "F6","G6", "H6", "I6", "J6", "K6", "L6",
                "A7", "B7", "C7", "D7", "E7", "F7","G7", "H7", "I7", "J7", "K7", "L7",
                "A8", "B8", "C8", "D8", "E8", "F8","G8", "H8", "I8", "J8", "K8", "L8",
                "A9", "B9", "C9", "D9", "E9", "F9","G9", "H9", "I9", "J9", "K9", "L9",
                "A10", "B10", "C10", "D10", "E10", "F10","G10", "H10", "I10", "J10", "K10", "L10",
                "A11", "B11", "C11", "D11", "E11", "F11","G11", "H11", "I11", "J11", "K11", "L11",
                "A12", "B12", "C12", "D12", "E12", "F12","G12", "H12", "I12", "J12", "K12", "L12",
                ]
    current_position = 0
    print(size.format(**values))
    board = size
    print("The ⬤  symbol represents your cursor. Press the WASD keys to move. Press 'f' to place or remove a flag. Press 'e' to examine. If you examine a tile with a mine, you lose the game. Press 'q' to quit. Your timer starts now.")
    start_time = time.time()
    if size == small:
        initial_mines = random.randint(9,11)
        movement_value = 8
    if size == medium:
        initial_mines = random.randint(12,15)
        movement_value = 10
    if size == large:
        initial_mines = random.randint(16,20)
        movement_value = 12
    mines_remaining = initial_mines
    print(str(mines_remaining) + " mines to be found!")
    mines = random.sample(range(0, len(positions)), mines_remaining)
    
    is_flag = False
    is_number = False
    flag_count = 0
    reset = False

    while reset == False:
        while flag_count != initial_mines or mines_remaining > 0:
            
            action = input("What would you like to do?")
            if action == "w" or action == "w" or action == "a" or action == "s" or action == "d" or action == "f" or action == "e" or action == "q":
                if action == "w":
                    movement("w")
                    print(board.format(**values))
                    
                if action == "a":
                    movement("a")
                    print(board.format(**values))
                    
                if action == "s":
                    movement("s")
                    print(board.format(**values))
                    
                if action == "d":
                    movement("d")
                    print(board.format(**values))
                    
            
                if action == "f":
                    if is_flag == True:
                        if current_position in mines:
                            mines_remaining += 1
                        flag_count -= 1
                        is_flag = False
                        print(board.format(**values))
                    elif is_number == False:
                        values[positions[current_position]] = "☑ "
                        if current_position in mines:
                            mines_remaining -= 1
                        flag_count += 1
                        is_number = False
                        is_flag = True
                        print(board.format(**values))
                    else:
                        print("Already examined. Please select a different tile.")
                    
                
                if action == "e":
                    if is_flag == True:
                        print("This tile has been flagged. Please remove the flag before examining.")
                    elif is_number == True:
                        print("Already examined. Please select a different tile.")
                    elif current_position in mines:
                        values[positions[current_position]] = "☒ "
                        end_time = time.time()
                        time_lapsed = end_time - start_time
                        print(board.format(**values))
                        print("That's a mine! You lost!")
                        print("You took {0} seconds.".format(int(time_lapsed)))
                        play_again()
                        reset = True
                        break
                    else:
                        is_number = True
                        mine_test(current_position)
                        print(board.format(**values))
                    
                if action == "q":
                    print("Are you sure you want to quit?")
                    waiting_input = True
                    while waiting_input == True:
                        quit = input("Press 'y' or 'n'.")
                        if quit == "y":
                            print("Thank you for playing!")
                            exit()
                        if quit == "n":
                            print("Okay, you can keep playing.")
                            waiting_input = False
                        else:
                            print("Invalid input.")
            else:
                print("Invalid input. Please press 'w', 'a', 's', 'd', 'f','e' or 'q'.") 
        if reset == False:
            print("Congratulations, you cleared the board!")
            end_time = time.time()
            time_lapsed = end_time - start_time
            print("You took {0} seconds.".format(int(time_lapsed)))
            size = False
            reset = True
            play_again()

        