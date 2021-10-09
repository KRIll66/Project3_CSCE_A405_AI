# Project3_CSCE_A405_AI

CSCE A405 Programming Assignment 3
Due Thursday, October 21, 2021, at 10:00 AM

Purpose:  The goal of this assignment is to gain an understanding of game playing, the minimax algorithm, and alpha-beta pruning.

Background:  Owari is a two-player, alternating-move, zero-sum game of complete information. Each player (called SOUTH and NORTH) has six pits lined up horizontally in front of them, and a "goal" pit on the side to the player’s right. The board will be represented as a picture:
   3 3 3 3 3 3
0                   0
   3 3 3 3 3 3
Here, SOUTH’s pits are at the bottom and goal pit at the right, while NORTH’s pits are at the top and goal pit at the left. The picture above shows the starting configuration for every game: each pit has 3 stones in it, except for the goal pits which are empty.

To make a move, a player chooses one of the six pits on his or her side of the board (the chosen pit must have stones in it) and redistributes (or "sows") the stones one-by-one going counterclockwise around the board, starting with the pit following the one picked. The opponent's goal pit, if reached, is skipped. For the purposes of this implementation, the pits on SOUTH's side are numbered 0 to 5, with pit 6 being the SOUTH's goal pit, while NORTH 's pits are numbered 7 to 12 from right to left (i.e., continuing counter-clockwise) and NORTH's goal pit is pit number 13. If SOUTH moves first and chooses to move from pit number 4, the resulting position would be:
   3 3 3 3 3 4
0                   1
   3 3 3 3 0 4

Capturing: If the last stone of a player's move falls into an empty pit on the moving player's side of the board, then any stones in the pit opposite to it are captured and placed in the moving player's goal pit. For instance, if it were SOUTH’s turn in the position shown above, SOUTH could choose to move from pit number 1, and the resulting configuration would be:
   3 3 3 3 0 4
0                   4
   3 0 4 4 1 4
Note that all of the stones from pit number 8 have been captured and placed in SOUTH’s pit.

Ending the game: The game is over when either player empties all six pits on their side of the board. The other player then takes all of the remaining stones from their own side, and places them in their goal pit. Players then count the stones in their goal pits. The player with the most stones is the winner.

Requirements:  For this assignment, you are required to write a program that plays a competent game of Owari against an interactive opponent.  You may assume that the computer is always the SOUTH player and the interactive opponent is always the NORTH player. The main components of your program include the following:

1.	GetWhoMovesFirst: This routine will interactively prompt the human opponent (NORTH) to select whether they want to move first or second.
2.	GetHumanPlayerMove:  This routine will prompt the human opponent (NORTH) to specify the pit from which they want to move stones (7, 8, 9, 10, 11, or 12).  If the specified pit is empty, your program should display an appropriate error message and redisplay the prompt.  Repeat the process until the user selects a pit that is not empty, and then move the stones from that pit to other pits as described above, skipping the opponent’s goal pit if necessary.
3.	GenerateComputerPlayerMove:  Use the minimax algorithm with alpha-beta pruning to determine the optimal next move for the computer player.  The algorithm used by this routine is relatively simple:
a)	Given the current state, generate all possible successor states by trying all legal computer moves. (A maximum of six moves are possible.)
b)	Select the move that leads to the successor state that is most advantageous for the computer player.
Of course, the tricky part for the computer player comes from evaluating each possible successor state.  The computer proceeds by assuming that the human player will always pick the move that leads to a successor state that is most favorable to them.  Unfortunately, the size of the search space for Owari is large enough to make exhaustive search of the game space prohibitively costly.  For this reason, your computer move generator should keep track of the current search depth, and should stop generating new successor states when it reaches a predefined depth limit.  It should then call a static evaluation function to estimate the value of the current state, and return the estimated value to the calling routine.  

Programs should be written in the high-level language of your choice.  (Note that some languages, such as Visual Basic [version 5.0 or higher], may allow you to develop a nice user interface with minimal effort.)

You should write your program to allow the user to interactively specify a parameter (i.e., the look-ahead level) that limits the amount of time it takes for your program to make a move. If, when playing the tournament, I decide that your program is taking too long to evaluate a game configuration, I reserve the right to require you to restart the game using a parameter value that results in faster play.

On the Due Date: There will be no lecture on the due date; instead, we will play the “2021 UAA Owari Tournament”.  The computer player developed by each team will play matches against the computer players of other teams in a round-robin tournament. Each match will consist of two games, with a different player moving first in each game. Moves generated by one computer will be entered manually (in place of the human player) against the competing computer. Be sure you have translated the selected pit number correctly!  Computers will alternate moves until the game ends.  Be sure to record the final score of each game and clearly indicate the outcome (win, lose, or draw). At the end of the tournament, the best computer player will be crowned the 2021 UAA Owari Tournament Champion!  [NOTE: since we are online this semester, teams should be prepared to play each other via Zoom.]

Submit your source code and executable via blackboard.  Clearly indicate the name and preferred email address of each member of your team at the top of your source code.

