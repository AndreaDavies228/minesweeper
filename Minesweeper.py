import random

#☑
#☒
#■
#⬤
#☐
print("Welcome to Minesweeper.")
playing = True
while playing == True:
    def mine_test(position):
        count = 0
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
        if position + movement_value -1 < len(positions) and current_position % movement_value != 0:
            test6 = position + movement_value - 1
            if test6 in mines:
                count += 1
        if current_position % movement_value != 0:
            test7 = position - 1
            if test7 in mines:
                count += 1
        if position - movement_value - 1 >= 0 and current_position % movement_value != 0:
            test8 = position - movement_value - 1
            if test8 in mines:
                count += 1
        return count

    size = False
    values = {"A1": "☐ ", "B1": "☐ ", "C1": "☐ ", "D1": "☐ ", "E1": "☐ ", "F1": "☐ ", "G1": "☐ ", "H1": "☐ ", "I1": "☐ ", "J1": "☐ ", "K1": "☐ ", "L1": "☐ ",
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
        board_size = input("Please select your game size: Small, Medium, or Large")
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
                "A10", "B10", "C10", "D10", "E10", "F10","G10", "H10", "I0", "J10", "K10", "L10",
                "A11", "B11", "C11", "D11", "E11", "F11","G11", "H11", "I11", "J11", "K11", "L11",
                "A12", "B12", "C12", "D12", "E12", "F12","G12", "H12", "I12", "J12", "K12", "L12",
                ]
    current_position = 0
    print(size.format(**values))
    board = size
    print("The ⬤ symbol represents your cursor. Press the WASD keys to move. Press 'f' to place a flag. Press 'e' to examine. If you examine a tile with a mine, you lose the game. Press 'q' to quit.")
    if size == small:
        mines_remaining = random.randint(7,9)
        movement_value = 8
    if size == medium:
        mines_remaining = random.randint(9,11)
        movement_value = 10
    if size == large:
        mines_remaining = random.randint(11,13)
        movement_value = 12
    print(str(mines_remaining) + " mines to be found!")
    mines = random.sample(range(0, len(positions)), mines_remaining)
    print(mines)
    is_flag = False
    while mines_remaining > 0:
        action = input("What would you like to do?")
        if action == "w" or action == "w" or action == "a" or action == "s" or action == "d" or action == "f" or action == "e" or action == "q":
            if action == "w":
                if is_flag == True:
                    values[positions[current_position]] = "☑ "
                else:
                    if values[positions[current_position]] == "⬤ ":
                        values[positions[current_position]] = "☐ "
                if current_position - movement_value >= 0:
                    current_position -= movement_value
                else:
                    current_position = (current_position + len(positions) - movement_value)
                if values[positions[current_position]] == "☑ ":
                    is_flag = True
                    values[positions[current_position]] = "⬤ "
                else:
                    is_flag = False
                    values[positions[current_position]] = "⬤ "
                print(board.format(**values))
                print(current_position)
            if action == "a":
                if is_flag == True:
                    values[positions[current_position]] = "☑ "
                else:
                    if values[positions[current_position]] == "⬤ ":
                        values[positions[current_position]] = "☐ "
                if current_position % movement_value == 0:
                    current_position += (movement_value -1)
                else:
                    current_position -= 1
                if values[positions[current_position]] == "☑ ":
                    is_flag = True
                    values[positions[current_position]] = "⬤ "
                else:
                    is_flag = False
                    values[positions[current_position]] = "⬤ "
                print(board.format(**values))
                print(current_position)
            if action == "s":
                if is_flag == True:
                    values[positions[current_position]] = "☑ "
                else:
                    if values[positions[current_position]] == "⬤ ":
                        values[positions[current_position]] = "☐ "
                if current_position + movement_value < len(positions):
                    current_position += movement_value
                else:
                    current_position = current_position % movement_value
                if values[positions[current_position]] == "☑ ":
                    is_flag = True
                    values[positions[current_position]] = "⬤ "
                else:
                    is_flag = False
                    values[positions[current_position]] = "⬤ "
                print(board.format(**values))
                print(current_position)
            if action == "d":
                if is_flag == True:
                    values[positions[current_position]] = "☑ "
                else:
                    if values[positions[current_position]] == "⬤ ":
                        values[positions[current_position]] = "☐ "
                if current_position % movement_value == (movement_value -1):
                    current_position -= (movement_value - 1)
                else:
                    current_position += 1
                if values[positions[current_position]] == "☑ ":
                    is_flag = True
                    values[positions[current_position]] = "⬤ "
                else:
                    is_flag = False
                    values[positions[current_position]] = "⬤ "
                print(board.format(**values))
                print(current_position)
            if action == "f":
                values[positions[current_position]] = "☑ "
                print(board.format(**values))
            if action == "e":
                if current_position in mines:
                    print("That's a mine! You lost!")
                    again = input("Do you want to play again?")
                    if again == "y":
                        break
                    if again == "n":
                        print("Thank you for playing!")
                        exit()
                count = mine_test(current_position)
                values[positions[current_position]] = count
                print(board.format(**values))
                print(str(count) + "  ")
            if action == "q":
                print("Are you sure you want to quit?")
                quit = input("Press 'y' or 'n'.")
                if quit == "y":
                    exit()
                if quit == "n":
                    print("Okay, you can keep playing.")
                else:
                    print("Invalid input.")
        else:
            print("Invalid input. Please press 'w', 'a', 's', 'd', 'f','e' or 'q'.")      
        