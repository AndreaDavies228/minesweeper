import random

#☑
#☒
#■
#⬤
#☐
print("Welcome to Minesweeper.")
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
print("The ⬤ symbol represents your cursor. Press the WASD keys to move. Press 'f' to place a flag. Press 'e' to examine. If you examine a tile with a mine, you lose the game.")
if size == small:
    mines_remaining = random.randint(7,9)
mines = random.sample(range(0, len(positions)), mines_remaining)
print(mines)
is_flag = False
while mines_remaining > 0:
    action = input("What would you like to do?")
    if action == "w":
        if is_flag == True:
            values[positions[current_position]] = "☑ "
        else:
            if values[positions[current_position]] == "⬤ ":
                values[positions[current_position]] = "☐ "
        if current_position - 8 >= 0:
            current_position -= 8
        else:
            current_position = current_position + len(positions) - 8
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
        if current_position % 8 == 0:
            current_position += 7
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
        if current_position + 8 < len(positions):
            current_position += 8
        else:
            current_position = current_position % 8
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
        if current_position % 8 == 7:
            current_position -= 7
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
    else:
        print("Invalid input. Please press 'w', 'a', 's', 'd', 'f' or 'e'")      
    