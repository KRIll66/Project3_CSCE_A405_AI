###################################################################
#
#Util module handles methods that do not fall within a class's perview
#
#evaluate() calculates the effect of a certain move, this will be used to 
#poulate alpha and beta values for the minimax tree
#
###################################################################


import owariBoard

#evalute will need a reference to the original state of the board prior to 
#expanding the tree, this will allow it to check the "goodness" of a move
#by comparing it to the state of the board at a leaf of the tree
def evaluate (original_board, current_board):
    #value is going to see how many points were gained for max
    #this can be greatly improved upon to try and cleverly decide the best direction to go down
    value = current_board[6] - original_board[6]