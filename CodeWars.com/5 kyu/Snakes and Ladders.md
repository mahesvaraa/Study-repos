# Snakes and Ladders

https://www.codewars.com/kata/587136ba2eefcb92a9000027

**Introduction**

Snakes and Ladders is an ancient Indian board game regarded today as a worldwide classic. It is played between two or
more players on a gameboard having numbered, gridded squares. A number of "ladders" and "snakes" are pictured on the
board, each connecting two specific board squares. (Source Wikipedia)

![](https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/snakesandladders.jpg)
**Task**

Your task is to make a simple class called SnakesLadders. The test cases will call the method play(die1, die2)
independantly of the state of the game or the player turn. The variables die1 and die2 are the die thrown in a turn and
are both integers between 1 and 6. The player will move the sum of die1 and die2.

**The Board**
![](https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/snakesandladdersboard.jpg)

**Rules**

1. There are two players and both start off the board on square 0.

2. Player 1 starts and alternates with player 2.

3. You follow the numbers up the board in order 1=>100

4. If the value of both die are the same then that player will have another go.

5. Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster. If you land exactly
   on a square that shows an image of the bottom of a ladder, then you may move the player all the way up to the square
   at the top of the ladder. (even if you roll a double).

6. Slide down snakes. Snakes move you back on the board because you have to slide down them. If you land exactly at the
   top of a snake, slide move the player all the way to the square at the bottom of the snake or chute. (even if you
   roll a double).

7. Land exactly on the last square to win. The first person to reach the highest square on the board wins. But there's a
   twist! If you roll too high, your player "bounces" off the last square and moves back. You can only win by rolling
   the exact number needed to land on the last square. For example, if you are on square 98 and roll a five, move your
   game piece to 100 (two moves), then "bounce" back to 99, 98, 97 (three, four then five moves.)

8. If the Player rolled a double and lands on the finish square “100” without any remaining moves then the Player wins
   the game and does not have to roll again.

**Returns**

Return `Player n Wins!`. Where n is winning player that has landed on square 100 without any remainding moves left.

Return `Game over!` if a player has won and another player tries to play.

Otherwise return `Player n is on square x`. Where n is the current player and x is the sqaure they are currently on.
Good luck and enjoy!

# Solution

```python
class SnakesLadders():

    def __init__(self):
        self.field = [[1, 1], [2, 38], [3, 3], [4, 4], [5, 5], [6, 6], [7, 14], [8, 31], [9, 9], [10, 10],
                      [11, 11], [12, 12], [13, 13], [14, 14], [15, 26], [16, 6], [17, 17], [18, 18], [19, 19],
                      [20, 20], [21, 42], [22, 22], [23, 23], [24, 24], [25, 25], [26, 26], [27, 27], [28, 84],
                      [29, 29], [30, 30], [31, 31], [32, 32], [33, 33], [34, 34], [35, 35], [36, 44], [37, 37],
                      [38, 38], [39, 39], [40, 40], [41, 41], [42, 42], [43, 43], [44, 44], [45, 45], [46, 25],
                      [47, 47], [48, 48], [49, 11], [50, 50], [51, 67], [52, 52], [53, 53], [54, 54], [55, 55],
                      [56, 56], [57, 57], [58, 58], [59, 59], [60, 60], [61, 61], [62, 19], [63, 63], [64, 60],
                      [65, 65], [66, 66], [67, 67], [68, 68], [69, 69], [70, 70], [71, 91], [72, 72], [73, 73],
                      [74, 53], [75, 75], [76, 76], [77, 77], [78, 98], [79, 79], [80, 80], [81, 81], [82, 82],
                      [83, 83], [84, 84], [85, 85], [86, 86], [87, 94], [88, 88], [89, 68], [90, 90], [91, 91],
                      [92, 88], [93, 93], [94, 94], [95, 75], [96, 96], [97, 97], [98, 98], [99, 80], [100, 100]]
        self.player1_pos, self.player2_pos = 0, 0
        self.PLAYER1 = True

    def play(self, die1, die2):
        if self.PLAYER1 and self.player1_pos != 100 and self.player2_pos != 100:

            try:
                self.player1_pos = self.field[self.player1_pos + die1 + die2 - 1][1]
            except IndexError:
                self.player1_pos = self.field[100 - (self.player1_pos + die1 + die2) % 100 - 1][1]
            if die1 != die2:
                self.PLAYER1 = False
            return f'Player 1 is on square {self.player1_pos}' if self.player1_pos != 100 else 'Player 1 Wins!'

        elif not self.PLAYER1 and self.player1_pos != 100 and self.player2_pos != 100:
            try:
                self.player2_pos = self.field[self.player2_pos + die1 + die2 - 1][1]
            except IndexError:
                self.player2_pos = self.field[100 - (self.player2_pos + die1 + die2) % 100 - 1][1]
            if die1 != die2:
                self.PLAYER1 = True
            return f'Player 2 is on square {self.player2_pos}' if self.player2_pos != 100 else 'Player 2 Wins!'
        else:
            return 'Game over!'

```