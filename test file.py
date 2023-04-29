board_size = "L"
small = "8x8"
medium = "12x12"
large = "16x16"
print(board_size)
if board_size == "Small" or board_size == "small" or board_size == "S" or board_size == "s":
    size = small
    print("Small board size set.")
elif board_size == "Medium" or board_size == "medium" or board_size == "M" or board_size == "m":
    size = medium
    print("Medium board size set.")
elif board_size == "Large" or board_size == "large" or board_size == "L" or board_size == "l":
    size = large
    print("Large board size set.")
else:
    print("Invalid input")