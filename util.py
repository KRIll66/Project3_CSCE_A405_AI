###################################################################
#
#Util module handles methods that do not fall within a class's perview
#
#evaluate() calculates the effect of a certain move, this will be used to 
#poulate alpha and beta values for the minimax tree
#
#minimax() performs the recursive searhc and accomplishes alpha beta pruning
#using the evaluate() function. minimax() needs to be passed the current state 
#of the board, depth to which the search will expand, as well as alpha and beta
#and a boolean for max vs min level
#
###################################################################


import math, owariBoard

#evalute will need a reference to the original state of the board prior to 
#expanding the tree, this will allow it to check the "goodness" of a move
#by comparing it to the state of the board at a leaf of the tree
def evaluate (original_board, current_board):
    #value is going to see how many more points max has earned vs min
    #this can be greatly improved upon to try and cleverly decide the best direction to go down
    value = current_board[6] - original_board[13]
    return value


#getChildren() returns the child states that can be expanded from a move
#if is_max then south will move, otherwise it is norths turn and we will expand their moves
def getChildren (game_object, curr_state, player_letter):
    children = []   
    #this means moves are on our side of the board, find all child nodes for our turns
    if player_letter == "s":
        for i in range (0,6):
            if curr_state[i] > 0:
                child = game_object.getChildMove(i, curr_state)
                children.append([i,child])    
    else:
        for i in range (7,13):
            if curr_state[i] > 0:
                child = game_object.getChildMove(i, curr_state)
                children.append([i, child])

   
    #children takes the form of [[move[state]], [move[state]]]
    return children



#minimax() does not actually handle the recursion, this function has the available first moves
#it will send each first move to minimaxRecursion() and then assess which first move is the best
def minimax (game_object, curr_state, depth, alpha, beta, is_max, move, player_letter):
    first_moves = getChildren(game_object, curr_state, player_letter)
    best_alpha = -math.inf
    best_move = None
    alpha_list = []
    moves = []
    for move in first_moves:
        this_alpha = minimaxRecursion(game_object, move[1], depth-1, alpha, beta, False, move, player_letter)
        alpha_list.append(this_alpha)
        moves.append(move[0])
    #find the best alpha value, store what move takes us here
    index = 0    
    for a in alpha_list:
        if a > best_alpha:
            best_move = moves[index]
            best_alpha = a
        index+=1

    
    return best_move
    

#TODO: assess best move, figure out how to pass it back
#on initial call, alpha must be -inf and beta must be +inf
def minimaxRecursion (game_object, curr_state, depth, alpha, beta, is_max, move, player_letter):
    best_move = move
    
    #base case, we have reached the end of recursion or have finished the game down this 
    #search path, return utility of final state
    if depth == 0 or game_object.gameOver(curr_state):
        eval = evaluate(game_object.board, curr_state)
        return eval



    #this means we are on a maximizing level (it's our turn), initialize best value
    #to -inf, recurse through each child, and pass false for is_max to the recursion call
    if is_max:
        children = getChildren(game_object, curr_state, player_letter)
        #print ("In minimax, children = ", children)
        for child in children:          
            move = child[0]
            child = child[1]           
            #recursive call, continue down until we reach depth or game over state
            utility = minimaxRecursion(game_object,child,depth-1,alpha,beta,False, move, player_letter)
            if alpha < utility:           
                alpha = utility
                              
            #opponent should not choose this move, prune this branch
            if beta <= alpha:
                break      
        return alpha

    
    #this means we are on a mnimizing level (bad guy's turn), initialize best value
    #to inf, recurse through each child, and pass true for is_max to the recursion call
    else:       
        children = getChildren(game_object, curr_state, player_letter)
        for child in children:
            move = child[0]
            child = child[1]            
            utility = minimaxRecursion(game_object,child,depth-1,alpha,beta,True,move, player_letter)
            if beta > utility:
                beta = utility
                
            #opponent will not choose this move, prune this branch
            if beta <= alpha:
                break
        return beta
