#################################################################
#
#Class: owariBoard
#the owariBoard class keeps track of the current state of the board
#it will end up being recursively called to populate the minimax tree
#in order to choose moves
#
#Attributes:
#An owari board has 6 dishes on it's north and south sides, with a 
#goal dish at the east and west side. It also tracks the user scores
#
#methods:
#move()
#handles rearranging the board after a move is selected
#
#display()
#the state of the board will need to be displayed after every move
#
#gameOver()
#this check to see if conditions have been met to end the game
#returns boolean
#
#getFinalScore()
#calculates and prints the final score, declares a winner
#################################################################

import copy

class owariBoard:
    
    #the initiator will populate the board in its start state
    
    def __init__(self):
        #board represents the current state of the game
        self.board = [3,3,3,3,3,3,0,3,3,3,3,3,3,0]                
        self.alpha = 0
        self.beta = 0
        #capture maps link the opposite dishes to one another
        #these are delcared in the initiator so we don't waste time
        #and space declaring them with every possible move
        self.capture_map_south = {
            0: 12,
            1: 11,
            2: 10,
            3: 9,
            4: 8,
            5: 7
        }
        self.capture_map_north = {
            7: 5,
            8: 4,
            9: 3,
            10: 2,
            11: 1,
            12: 0
        }        


    #TODO: modify this to receive a board array and calculate score based off that 
    #TODO: received array, do not modify self.board   
    def getFinalScore(self, final_board_state):
        north_list = final_board_state[7:13]
        south_list = final_board_state[0:6]
        south_goal = final_board_state[6]
        north_goal = final_board_state[13]
        #to tabulate the final score, whoever has stones left their side gets to conut them as points
        for v in north_list:
            north_goal += v
        for v in south_list:
            south_goal += v

        if south_goal == north_goal: 
            print("It's a tie!!")
            print ("Each side has a score of: ", south_goal)
        elif south_goal > north_goal:
            print ("Hooray!! South wins!!")
            print ("South's score: ", south_goal)
            print ("North's score: ", north_goal)
        else:
            print ("North has bested South for the last time!")
            print ("South's score: ", south_goal)
            print ("North's score: ", north_goal)
        return south_goal, north_goal
        
    
    #This checks for conditions that end a game, if met then it calls the getFinalScore method
    def gameOver(self, board_state):              
        north_list = board_state[7:13]
        south_list = board_state[0:6]        
        #check if north is empty, if so then game is over
        if all (v == 0 for v in north_list): 
            #self.getFinalScore(board_state)
            return True

        #next check if south is empty
        if all (v == 0 for v in south_list):
            #self.getFinalScore(board_state)
            return True
        
        return False
    
    #capture handles the logic for capturing the opponents stones
    def capture (self, turn, index, board_state):        
        if turn == "south":
            capture_index = self.capture_map_south.get(index)
            if board_state[capture_index] != 0:               
                board_state[6] += board_state[capture_index]
                board_state[capture_index] = 0

        if turn == "north":
            capture_index = self.capture_map_north.get(index)
            if board_state[capture_index] != 0:             
                board_state[13] += self.board[capture_index]
                board_state[capture_index] = 0
        
        return board_state 
   
    def move (self, index, board_state):
        
        #get the value at the selected index, this is the number of available moves
        num_moves = board_state[index]        
        board_state[index]=0
        
        if index < 6:
            turn = "south"
        else: turn = "north"        
        
        while num_moves > 0:           
            #this means that moves increment the index, north side moves decrement the index
            if index < 7: 
                index +=1                        
                #we are south and this is the opponents goal, don't increment it, move back to index of 0
                #if index == 6 and turn == "north":
                #    index = 13           
                #set index to 13 as that is the far right of the north side moves, log a goal for team south
                if index == 6 and turn == "south":
                    board_state[index]+=1                   
                    #we are still in the south side, increment the value of the dish at index
                else: 
                    board_state[index]+=1                    

            #this means that we are in the north side of the board
            if index > 6:
                index+=1
                #this is the opponent and they have just scored, log score and move to index 0
                if index == 13 and turn == "north":
                    board_state[index]+=1
                    index = -1
                
                else: 
                    if index == 13: index = 0
                    board_state[index]+=1                     
                    
            #performed a move, decrement move count
            num_moves-=1        

        #moves complete, check to see if the final move landed in an empty dish on the player's side
        #if so, then all the stone's opposite now belong to the player
        if board_state[index] == 1:
            if turn == "south" and index <6:
               board_state = self.capture(turn, index, self.board)
            if turn == "north" and index > 6 and index < 13:
                board_state = self.capture(turn, index, self.board)

        return board_state

    def getChildMove(self, index, current_state):
        child_state = copy.deepcopy(current_state)
        #get the value at the selected index, this is the number of available moves
        num_moves = child_state[index]        
        child_state[index]=0
        
        if index < 6:
            turn = "south"
        else: turn = "north"        
        
        while num_moves > 0:
           
            #this means that moves increment the index, north side moves decrement the index
            if index < 7: 
                index +=1                        
                #we are south and this is the opponents goal, don't increment it, move back to index of 0
                #if index == 6 and turn == "north":
                #    index = 13           
                #set index to 13 as that is the far right of the north side moves, log a goal for team south
                if index == 6 and turn == "south":
                    child_state[index]+=1                   
                    #we are still in the south side, increment the value of the dish at index
                else: 
                    child_state[index]+=1                    

            #this means that we are in the north side of the board
            if index > 6:
                index+=1
                #this is the opponent and they have just scored, log score and move to index 0
                if index == 13 and turn == "north":
                    child_state[index]+=1
                    index = -1
                
                else: 
                    if index == 13: index = 0
                    child_state[index]+=1                     
                    
            #performed a move, decrement move count
            num_moves-=1

        #moves complete, check to see if the final move landed in an empty dish on the player's side
        #if so, then all the stone's opposite now belong to the player
        if child_state[index] == 1:
            if turn == "south" and index <6:
                self.capture(turn, index, child_state)
            if turn == "north" and index > 6 and index < 13:
                self.capture(turn, index, child_state)

        return child_state



    def display (self, board_state):
        #display the board in a fashion that is clear and readable
        #first, we must reverse the north side of the list since it's indexes move from right to left
        north_list = board_state[7:13]
        north_list.reverse()
        print (" ", north_list)
        print (board_state[13], "                  ", board_state[6])
        print (" ", board_state[0:6])
