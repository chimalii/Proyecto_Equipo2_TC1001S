"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

import turtle

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y, pos):
    """Draw X player in an empty space.
    Update board matrix.
    Return bool for if something was drawn"""
    if board[pos[1]][pos[0]] == 0:
        board[pos[1]][pos[0]] = 1       # Y position is first on a matrix
        turtle.color('blue')
        line(x + 7, y + 7, x + 126, y + 126)
        line(x + 7, y + 126, x + 126, y + 7)
        return True
    else:
        print("Space occupied, try again")
        return False


def drawo(x, y, pos):
    """Draw O player in an empty space.
    Update board matrix.
    Return bool for if something was drawn
    """
    if board[pos[1]][pos[0]] == 0:
        board[pos[1]][pos[0]] = 2       # Y position is first on a matrix
        turtle.color('green')
        turtle.up()
        turtle.goto(x + 67, y + 5)
        turtle.down()
        turtle.circle(62)
        return True
    else:
        print("Space occupied, try again")
        return False


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


def findCoords(x, y):
    """Determine the space on a matrix corresponding to a set of coordinates"""
    _x = 0
    _y = 0

    if x == 66:
        _x = 2
    elif x == -67:
        _x = 1
    elif x == -200:
        _x = 0

    if y == 66:
        _y = 0
    elif y == -67:
        _y = 1
    elif y == -200:
        _y = 2

    return (_x, _y)


state = {'player': 0}
players = [drawx, drawo]
board = [[0] * 3 for _ in range(3)]


def tap(x, y):
    """Draw X or O in tapped square.
    If square is occupied allows same player to take action
    """
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    stepTaken = draw(x, y, findCoords(x, y))
    turtle.update()
    if stepTaken:
        state['player'] = not player


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.pensize(5)

turtle.update()
turtle.onscreenclick(tap)
turtle.done()
