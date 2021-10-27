import owariBoard, util, math, random

def main ():
    game = owariBoard.owariBoard()     

    #get the beginning input for the game to begin, allow players to select who goes first    
    print ("Welcome to the Owari game, below is the starting board:")
    game.display(game.board)
    first = input("Who would you like to go first, North or South?\nEnter 'n' for North or 's' for South: ")
    first = first.lower()
    while first != "n" and first != "s":        
        print ("Sorry, you must use 'n' for north or 's' for South")
        first = input("Who would you like to go first, North or South?\nEnter 'n' for North or 's' for South: ")        
        print ("You entered: ", first)
        first = first.lower()
    turn = first
    turn_count = 1
    #This loop handles game play, continues until a winner is decided
    #All input is handled by user input
    while True:
        n_depth = 3
        s_depth = 3
        #first, check if it's norths turn
        if turn == "n":
            while True:

                try:                    
                    north_move = util.minimax(game, game.board, n_depth, -math.inf, math.inf, True, None, turn, "s", first)
                    print ("North should move: ", north_move)
                    #get a valid move for North, must not be an empty reference and must be 7-12 inclusive
                    move_index = north_move
                    if move_index < 7 or move_index > 12:
                        print ("This is North's turn, input must be 7-12 inclusive")
                    elif game.board[move_index] == 0:
                        print ("This is not a valid move, the dish you selected is empty...")
                    else: break
                except ValueError:
                    print ("The input must be an integer...")
            turn = "s"

        #otherwise, it's south's turn
        else:
            while True:
                try:
                    move_index = util.minimax(game, game.board, s_depth, -math.inf, math.inf, False, None, turn, "n", first)
                    #  print ("South should choose move: ", move_index)
                    move_index = int(input())
                    if move_index < 0 or move_index > 5:
                        print ("This is South's turn, input must be 0-5 inclusive")
                    elif game.board[move_index] == 0:
                        print ("This is not a valid move, the dish you selected is empty...")
                    else: break
                except ValueError:
                    print ("The input must be an integer...")
            turn = "n"
            turn_count += 1

        #make the move on the board and display the new game state
        game.move(move_index, game.board)
        game.display(game.board)
        #check to see if gameover conditions have been met
        if game.gameOver(game.board): break

    game.displayFinalScore(game.board)


if __name__ == '__main__':
    main()