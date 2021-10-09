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
#################################################################


class owariBoard:
    
    #the initiator will populate the board in its start state
    
    def __init__(self):
        #board represents the current state of the game
        self.board = [3,3,3,3,3,3,0,3,3,3,3,3,3,0]        
        #this is the right of the board
        self.north_goal = 0
        #this is the left of the board
        self.south_goal = 0
        self.alpha = 0
        self.beta = 0
        self.game_over = False



    def move (self, index):
        
        #get the value at the selected index, this is the number of available moves
        num_moves = self.board[index]
        self.board[index]=0
        if index < 6:
            turn = "south"
        else: turn = "north"
        
        while num_moves > 0:
            #this means that moves increment the index, north side moves decrement the index
            if index < 7:                         
                #we are south and this is the opponents goal, don't increment it, move back to index of 0
                if index == 6 and turn == "north":
                    index = 13           
                #set index to 13 as that is the far right of the north side moves, log a goal for team south
                if index == 6 and turn == "south":
                    self.board[index]+=1
                    index = 13
                    #we are still in the south side, increment the value of the dish at index
                else: self.board[index]+=1

            #this means that we are in the north side of the board, moves now decrement the index
            if index > 6:
                #this is the opponent and they have just scored, log score and move to index 0
                if index == 13 and turn == "north":
                    self.board[index]+=1
                    index = 0                
                #set index to 0 as that is the far left of the south side moves
                if index == 13 and turn == "south":
                    index = 0
        #moves complete, check to see if the final move landed in an empty dish


    def display (self):
        #display the board in a fashion that is clear and readable
        print (" ", self.board[7:13])
        print (self.board[13], "                  ", self.board[6])
        print (" ", self.board[0:6])
