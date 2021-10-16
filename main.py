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
        # set depth at the start of every other turn as needed.
        if turn_count % 2 == 1:
            i_depth = int(input("\n*****\nWhat is minimax depth?\nInput must be a whole number greater than 0:"))
            while (i_depth < 0) or (i_depth % 1 != 0) :
                print ("You entered: ", i_depth)        
                print ("Sorry, you must use a whole number greater than 0. Try again:")
                i_depth = input("What is minimax depth?\nInput must be a whole number greater than 0: ")    
        #first, check if it's norths turn
        if turn == "n":
            while True:

                try:
                    while True:
                        # north_move = random.randint(7, 12)
                        # if game.board[north_move] !=0:
                        north_move = util.minimax(game, game.board, i_depth, -math.inf, math.inf, False, None, turn)
                        if game.board[north_move] != 0:
                            break
                    print ("North should move: ", north_move)
                    #get a valid move for North, must not be an empty reference and must be 7-12 inclusive
                    move_index = int(input("It is North's turn, please select a move from 7-12 (remember that north side counts up from right to left:\n"))
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
                    best_move = util.minimax(game, game.board, i_depth, -math.inf, math.inf, True, None, turn)

                    print ("We should choose move: ", best_move)
                    best_move = None
                    #get a valid move for South, must not be an empty reference and must be 0-5 inclusive
                    move_index = int(input("It is South's turn, please select a move from 0-5 (remember that south side counts up from left to right:"))


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