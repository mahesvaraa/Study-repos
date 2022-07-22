# Tic-Tac-Toe Checker

https://www.codewars.com/kata/525caa5c1bf619d28c000335

If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we?
Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2
if it is an "O", like so:

```python
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
```

We want our function to return:

* -1 if the board is not yet finished AND no one has won yet (there are empty spots),
* 1 if "X" won,
* 2 if "O" won,
* 0 if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

# Solution

```python
def is_solved(board):
    board2 = list(zip(*board))
    if board[0][2] == board[1][1] == board[2][0] and board[0][0] != 0:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    else:
        for i in range(3):
            if set(board[i]) == {1} or set(board[i]) == {2}:
                return board[i][0]
            if set(board2[i]) == {1} or set(board2[i]) == {2}:
                return board2[i][0]
        if 0 in board[0] or 0 in board[1] or 0 in board[2]:
            return -1
        else:
            return 0
```