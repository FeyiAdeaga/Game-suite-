
def draw_board(r,h):
    rows, height = r, h
    board = []
    for number in range(rows):
        row = []
        for number in range(height):
            row.append("_")
        board.append(row)
    return board

def print_board(array):

    for row in array:
        print(row)