'''
Lab0 Taks2 Mykhailo Kuzmyn
'''


def validate_rows(board: list):
    """
    checks whether rows of the board comply to the rules of the game
    """
    for row in board:
        row = row.strip('*').replace(' ', '')
        if sorted(list(set(row))) != sorted(list(row)):
            return False
    return True


def validate_columns(board: list):
    """
    validates whether columns of the board comply ot the rules
    """
    vals = {x for x in range(1, 10)}

    for idx1 in range(9):
        chars = vals.copy()

        for idx2 in range(9):
            if board[idx2][idx1] != '*' and board[idx2][idx1] != ' ':

                try:
                    chars.remove(int(board[idx2][idx1]))
                except KeyError:
                    return False

    return True


def validate_colours(board: list):
    """
    checks whether tiles of the same colour comply to the rules
    """
    values = {x for x in range(1 , 10)}
    for idx1 in range(5):
        vals = set()
        vals.add(board[idx1][8 - idx1])

        for idx2 in range(1, 5):
            vals.add(board[idx1 + idx2][8 - idx1])
            vals.add(board[idx1][8 - idx2 - idx1])

        if ' ' in vals:
            vals.remove(' ')

        if '*' in vals:
            vals.remove('*')

        vals = {int(val) for val in vals}
        if not vals <= values:
            return False

    return True


def validate_board(board: list):
    """
    validates whether the board complies to the rules
    """
    if (validate_rows(board) == 0
       or validate_columns(board) == 0
       or validate_colours(board) == 0):
       return False
    
    return True


print(validate_board([
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]
))