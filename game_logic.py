'''
Yizhuo Wu 14863527
'''
NONE='.'
BLACK='B'
WHITE='W'

class InvalidMoveError(Exception):
    '''
    When a player wants to drop by input an
    invalid move, this error will raise.
    '''
    pass

class GameOverError(Exception):
    '''
    When the player wants to make a drop after the game is over,
    this error will raise.
    '''
    pass
class InvalidColError(Exception):
    '''
    When the player inputs an invalid column number,
    this error will raise.
    '''
    pass
    
class InvalidRowError(Exception):
    '''
    When the player inputs an invalid row number,
    this error will raise.
    '''

    
class Game_state:
    '''
    The Game_state class will include the methods that will used while playing the game.
    '''

    def __init__(self,row_number,col_number,turn,win_condition):
        '''
        This function will establish the initial mode of the game(Including first turn, winning condition, board,
        row number and column number, and the number of the discs on the board).
        '''
        self.turn=turn

        self.win_condition=win_condition

        self.board=self.create_game_borad(row_number,col_number)

        self.row=row_number

        self.col=col_number

        self.black = 0

        self.white = 0

    def get_ini_board(self,row_number,col_number):

        for i in range(row_number):

            row=input().split()

            for p in range(col_number):

                self.board[i][p]=row[p]                            

    def create_game_borad(self,row_number,col_number):

        board=[]

        for i in range(int(row_number)):

            board.append([])

            for a in range(int(col_number)):

                board[-1].append(NONE)

        return board

    def is_flippy_move_this_direction(self,row_number,col_number,row_delta,col_delta,current_color):
        '''
        This function will check whether the drop is invalid in a specific direction. It will use the
        row delta and col delta to show the direction and determine whether there are other color's discs
        on that direction.
        '''
        i=1

        if  self.board[row_number][col_number]=='.':

            


            if self._is_valid_row(row_number+row_delta*i) and self._is_valid_col(col_number+col_delta*i):


        
                adj_point=self.board[row_number+row_delta*i][col_number+col_delta*i]



                if adj_point != NONE and adj_point != current_color:


                    while True:

                        i+=1
                        
                        if self.row>row_number+row_delta*i >=0 and self.col> col_number+col_delta*i >= 0:

                            new_adj_point=self.board[row_number+row_delta*i][col_number+col_delta*i]

                            if new_adj_point == current_color:
    
                                return True

                            elif new_adj_point == NONE:

                                return False
                        else:

                            break

        return False

    def is_valid_drop(self,row_numebr,col_number,current_color):
        '''
        This function will check whether the location that the user want to drop
        is valid by checking all the direction of that disc.
        '''
        return self.is_flippy_move_this_direction(row_numebr,col_number,-1,-1,current_color)\
            or self.is_flippy_move_this_direction(row_numebr,col_number,0,-1,current_color)\
            or self.is_flippy_move_this_direction(row_numebr,col_number,1,-1,current_color)\
            or self.is_flippy_move_this_direction(row_numebr,col_number,0,1,current_color)\
            or self.is_flippy_move_this_direction(row_numebr,col_number,-1,1,current_color)\
            or self.is_flippy_move_this_direction(row_numebr,col_number,1,1,current_color)\
            or self.is_flippy_move_this_direction(row_numebr,col_number,1,0,current_color)\
            or self.is_flippy_move_this_direction(row_numebr,col_number,-1,0,current_color)

    def flippy_this_direction(self,row_number,col_number,row_delta,col_delta,current_color):
        '''
        This function will flip the discs on the specific direction, it will use the row_delta
        and col_delta to represent the direction.
        '''
        i=1
        
        while True:

            adj_point = self.board[row_number+row_delta*i][col_number+col_delta*i]

            if adj_point != current_color:

                self.board[row_number+row_delta*i][col_number+col_delta*i] = current_color

                i+=1

            else: 

                break
        
    def flippy_disc(self,row_number,col_number,current_color):
        '''
        This function will flip the discs on the given direction.
        It will check which direction is valid to flip then flip the
        discs on that direction.
        '''
        if self.is_flippy_move_this_direction(row_number,col_number,-1,-1,current_color):

            self.flippy_this_direction(row_number,col_number,-1,-1,current_color)

        if self.is_flippy_move_this_direction(row_number,col_number,0,-1,current_color):

            self.flippy_this_direction(row_number,col_number,0,-1,current_color)

        if self.is_flippy_move_this_direction(row_number,col_number,1,-1,current_color):

            self.flippy_this_direction(row_number,col_number,1,-1,current_color)

        if self.is_flippy_move_this_direction(row_number,col_number,0,1,current_color):

            self.flippy_this_direction(row_number,col_number,0,1,current_color)

        if self.is_flippy_move_this_direction(row_number,col_number,-1,1,current_color):

            self.flippy_this_direction(row_number,col_number,-1,1,current_color)

        if self.is_flippy_move_this_direction(row_number,col_number,1,1,current_color):

            self.flippy_this_direction(row_number,col_number,1,1,current_color)

        if self.is_flippy_move_this_direction(row_number,col_number,1,0,current_color):

            self.flippy_this_direction(row_number,col_number,1,0,current_color)

        if self.is_flippy_move_this_direction(row_number,col_number,-1,0,current_color):

            self.flippy_this_direction(row_number,col_number,-1,0,current_color)


    def drop_disc(self,row_number,col_number,turn_color):
        '''
        This function will drop the disc on the given cell, it also will
        raise the error if a player wants to move after the game is over or the
        player wants to drop in a invalid cell.It also will raise error when a
        player input an invalid row or column number.
        '''
        
        if self.is_valid_drop(row_number,col_number,turn_color):

            self.flippy_disc(row_number,col_number,turn_color)

            self.board[row_number][col_number]=turn_color

            self.turn=self.whos_turn()

    def is_this_color_can_drop(self,current_color):
        '''
        This function will check whether there is a cell for
        the current color to drop, if not, return False.
        '''
        for row in range(self.row):

            for col in range(self.col):
                
                if self.is_valid_drop(row,col,current_color):


                    return True

        return False
                    
    def game_over(self):
        '''
        This function will determine whether there is more cell for black or white
        player to drop, if there is no more, then the game is over.
        '''
        if (self.is_this_color_can_drop('B') == False) and (self.is_this_color_can_drop('W')==False):

            return True

        return False

    def winner(self):
        '''
        This function will return the winner to the players.
        If the winning condition is '>'(who has most discs then wins),
        the winner will be the one who has the most discs on the board.
        If the winning condition is '<'(who has most discs then wins),
        the winner will be the one who has the least discs on the board.        
        '''

        
        if self.win_condition == '>':

            if self.black > self.white:

                winner = 'B'

            elif self.black < self.white:

                winner = 'W'

            elif self.black == self.white:

                winner = 'NONE'

        if self.win_condition == '<':

            if self.black < self.white:

                winner = 'B'

            elif self.black > self.white:

                winner = 'W'

            elif self.black == self.white:

                winner = 'NONE'
            
        return winner
        
    def count_discs(self)->int:
        '''
        This function will count the number of
        the two discs on the board.
        '''
        white_number=0
        
        black_number=0

        for row in self.board:

            for col in row:

                if col=='B':

                    black_number+=1

                elif col=='W':

                    white_number+=1


        self.black=black_number
        
        self.white=white_number

    def change_turn(self):
        '''
        This function will change the turn(color) of
        the current turn(color).
        '''
        self.turn=self.whos_turn()
        
    def whos_turn(self)->str:
        '''
        This function will return the opposite turn of the
        current turn(color).
        '''
        if self.turn == BLACK:

            return WHITE
        else:
            return BLACK
                            
    def _is_valid_col(self,col_number):
        '''
        This function will return False if the column number
        is invalid.
        '''
        return 0 <= col_number <self.col

    def _is_valid_row(self,row_number):
        '''
        This function will return False if the row number
        is invalid.
        '''
        return 0 <= row_number <self.row
