'''
Yizhuo Wu 14863527
'''
import tkinter
import my_points
import disc_models
import math
import game_logic

DEFAULT_FONT = ('Helvetica', 14)

class setting_window:
    '''
    This class will be the class for the setting windows.
    '''

    def __init__(self):
        '''
        This init function will initialize the instruction message and the row number and col number box for
        user to input the row and column number. It will also construct options for user to choose which color
        they want to start with and which win mode they want to use. It also build some buttons like ok for user
        to click.
        '''
        
        self._dialog_window = tkinter.Toplevel()

        self.start_color_var = tkinter.StringVar()
        self.win_mode_var = tkinter.StringVar()

        self.start_color_var.set('B')
        self.win_mode_var.set('>')

        instruction_lable = tkinter.Label(
            master = self._dialog_window, text = 'You can set the game as you wish.',
            font = DEFAULT_FONT)

        instruction_lable.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_number_lable = tkinter.Label(
            master = self._dialog_window, text = 'Number of Rows:',
            font = DEFAULT_FONT)

        row_number_lable.grid(
            row = 1, column = 0, padx = 10, pady =10,
            sticky = tkinter.W)

        self._row_number_entry = tkinter.Entry(
            master = self._dialog_window, width = 2, font = DEFAULT_FONT)

        self._row_number_entry.grid(
            row = 1, column = 1, padx =10, pady = 1,
            sticky = tkinter.W)

        col_number_lable = tkinter.Label(
            master = self._dialog_window, text = 'Number of Columns:',
            font = DEFAULT_FONT)

        col_number_lable.grid(
            row = 2, column = 0, padx = 10, pady =10,
            sticky = tkinter.W)

        self._col_number_entry = tkinter.Entry(
            master = self._dialog_window, width = 2, font = DEFAULT_FONT)

        self._col_number_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W)        

        start_color_button_frame = tkinter.Frame(master = self._dialog_window)
        start_color_button_frame.grid(
            row = 3, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N
            )
        
        start_color_lable_black = tkinter.Radiobutton(
            master = start_color_button_frame, text = 'Black moves first:',
            font = DEFAULT_FONT, variable = self.start_color_var, value = 'B')

        start_color_lable_black.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        start_color_lable_white = tkinter.Radiobutton(
            master = start_color_button_frame, text = 'White moves first:',
            font = DEFAULT_FONT, variable = self.start_color_var, value = 'W')

        start_color_lable_white.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

        how_win_button_frame = tkinter.Frame(master = self._dialog_window)

        how_win_button_frame.grid(
            row = 4, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N
            )

        how_win_button_more = tkinter.Radiobutton(
            master = how_win_button_frame, text = 'More discs wins',
            font = DEFAULT_FONT, variable = self.win_mode_var, value = '>')

        how_win_button_more.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        how_win_button_fewer = tkinter.Radiobutton(
            master = how_win_button_frame, text = 'Fewer discs wins',
            font = DEFAULT_FONT, variable = self.win_mode_var, value = '<')

        how_win_button_fewer.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)        
  

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._clicked_ok = False
               
        self._row_numebr = ''
        self._col_number = ''
        
    def show(self) -> None:
        '''
        This function will show the setting window to the user for set the game board and
        game options.
        '''

        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def if_clicked_ok(self) -> bool:
        '''
        This function will return True if the user clicked OK button.
        '''
        return self._clicked_ok

    def row_number_get(self):
        '''
        This function will return the row number input by the user.
        '''
        return self._row_number

    def col_number_get(self):
        '''
        This function will return the column number input by the user.
        '''
        return self._col_number

    def start_color_get(self):
        '''
        This function will return the start color input by the user.
        '''        
        return self.start_color_var.get()

    def win_mode_get(self):
        '''
        This function will return the win mode input by the user.
        '''
        return self.win_mode_var.get()

        
    def _on_ok_button(self) -> None:
        '''
        If the user finish the setting step, this function will get the row and
        column number and then close the setting window.
        '''

        self._clicked_ok = True

        self._row_number = self._row_number_entry.get()
        self._col_number = self._col_number_entry.get()

        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        '''
        This function will return to the main window if the user click
        the cancel button.
        '''
        self._dialog_window.destroy()

    
class main_menu:
    '''
    This class is for the game running and the whole process of the game.
    It will draw the canvas, handle the move and draw the disc then
    generates the winner of the game.
    '''
    def __init__(self, state: disc_models.DiscState):
        '''
        This function will initialize the game state and canvas window for the user. Then the function
        will initialize the game start button for the user, when user click it. This function will also
        initialize the row number and column number of the board, and the number of white and black discs,
        some delta for computing and the height, width of the canvas.
        '''
        self._state = state
        self._root_window = tkinter.Tk()

        game_start_button = tkinter.Button(
            master = self._root_window, text = 'START A GAME', font = DEFAULT_FONT,
            command = self._on_game_start)
        game_start_button.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)



        self._save_text = tkinter.StringVar()
        self._save_text.set('No changes made.')

        configure_lable = tkinter.Label(
            master = self._root_window, textvariable = self._save_text,
            font = DEFAULT_FONT)

        configure_lable.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self.game_board_height = 600
        self.game_board_width = 600

        self._row_number = ''
        self._col_number = ''

        self.row_col_list=[]
        self.color = 'B'
        self._clicked_finishB = False

        self.white_count = 0
        self.black_count = 0

        self.win_mode = ''
        self.start_color = ''

        self.row_delta = 1
        self.col_delta = 1

        self.is_setting_board = True
 
        
    def run(self) -> None:
        '''
        This function will keep tracking for the user's action.
        '''
        self._root_window.mainloop()

    def draw_board(self,row_number,col_number,game_board_height,game_board_width) -> None:
        '''
        This function will draw the board for the user based on the row and column number.
        '''
        for line in range(row_number):
            self.game_board.create_line(self.x0,
                                        self.y0+(game_board_height/row_number)*line,
                                        game_board_width,
                                        self.x0+(game_board_height/row_number)*line, fill = 'black')    

        for line in range(col_number):
            self.game_board.create_line(self.x0+(game_board_width/col_number)*line,
                                        0,
                                        self.x0+(game_board_width/col_number)*line,
                                        game_board_height, fill = 'black'
                )

    def _on_board_resized(self, event: tkinter.Event) ->None:
        '''
        This function will redraw the canvas if user changed the size of the window.
        '''
        self._redraw_all_spots()
        
    def _on_board_clicked(self, event: tkinter.Event) ->None:
        '''
        This function will draw the disc on the board when user clicked and their move is
        valid. The function will then update the board information.
        '''
        row_number = self.row_col_list[0]
        col_number = self.row_col_list[1]        

        width = self.game_board.winfo_width()
        height = self.game_board.winfo_height()

        col = int(event.x // (width / col_number) )
        row = int(event.y // (height / row_number) )

        click_point = my_points.from_pixel(
            event.x, event.y, width, height)

        DISC_RADIUS = (math.sqrt((1*1)/(row_number*col_number)))*0.35

        if self.is_setting_board:
            
            self._state.handle_click(click_point, DISC_RADIUS,self.color)
            self._redraw_all_spots()
            self.game.board[row][col] = self.color

        else:
            
            if self.game.is_valid_drop(row,col,self.game.turn):

                self._state.handle_click(click_point, DISC_RADIUS,self.game.turn)
                self._redraw_all_spots()
                self.game.drop_disc(row,col,self.game.turn)

            for row in range(self.game.row):
                for col in range(self.game.col):
                    disc1 = self.game.board[row][col]
                    for disc in self._state._spots:
                        if (disc._center.row_delta == row+1) and (disc._center.col_delta == col+1):
                            disc.color = disc1

        self.update_infor()

        self._redraw_all_spots()

    def _redraw_all_spots(self) ->None:
        '''
        This function will redraw all the spots on the board if the user
        changed the size of the window or they made a new move.
        '''
        row_number = self.row_col_list[0]
        col_number = self.row_col_list[1]

        self.game_board.delete(tkinter.ALL)
        
        canvas_width = self.game_board.winfo_width()
        canvas_height = self.game_board.winfo_height()

        self.draw_board(row_number,col_number,canvas_height,canvas_width)

        row_length = canvas_height / self.game.row
        col_length = canvas_width / self.game.col

        for row in range(self.game.row):
            for col in range(self.game.col):

                x1 = col_length * col
                y1 = row_length * row
                x2 = col_length * (col+1)
                y2 = row_length * (row+1)

                if self.game.board[row][col] == 'B':

                    self.game_board.create_oval(x1,y1,
                                                x2,y2,
                    fill = 'black', outline = '#000000')

                elif self.game.board[row][col] == 'W':

                    self.game_board.create_oval(x1,y1,
                                                x2,y2,
                    fill = 'white', outline = '#000000')

    def _on_game_start(self) -> None:
        '''
        This function will generate a setting window when the user clicked the
        game start button.
        '''       
        configure_window = setting_window()
        configure_window.show()

        if configure_window.if_clicked_ok():

            row_number = int(configure_window.row_number_get())
            col_number = int(configure_window.col_number_get())
            start_color = configure_window.start_color_get()
            win_mode = configure_window.win_mode_get()

            self._row_numebr = row_number
            self._col_number = col_number
            self.win_mode = win_mode
            self.start_color = start_color

            self.row_col_list.append(row_number)
            self.row_col_list.append(col_number)
            

            self._save_text.set('Your settings have been saved! '+
                                'row: '+str(row_number)+' col: '+str(col_number)+'\n'
                                +'Start Color: '+start_color+'\n'
                                +'Win_mode '+win_mode+' Discs win.')


            self.game_board = tkinter.Canvas(
                master = self._root_window, width = 600, height = 600,
                background = 'pink')
            self.game_board.grid(
                row = 0, column = 0, padx = 10, pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

            self.game_board.rowconfigure(0,weight = 1)
            self.game_board.columnconfigure(0,weight = 1)

            self.x0 = 0
            self.y0 = 0

            self.draw_board(row_number,col_number,self.game_board_height,self.game_board_width)

            self.game_board.bind('<Configure>', self._on_board_resized)
            self.game_board.bind('<Button-1>',self._on_board_clicked)

            self.black_place_ok_button = tkinter.Button(
                master = self._root_window, text = 'Finish B', font = DEFAULT_FONT,
                command = self.on_finishb)

            self.black_place_ok_button.grid(
                row = 3, column = 0, padx = 10, pady = 10,
                sticky = tkinter.S)

            row_number = self.row_col_list[0]
            col_number = self.row_col_list[1]

            first_turn = self.start_color
            win_condition = self.win_mode

            self.game = game_logic.Game_state(row_number,col_number,first_turn,win_condition)

            self.turn_label = tkinter.Label(master = self._root_window, text = '', font = DEFAULT_FONT)
            self.turn_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)        

            self.count_label = tkinter.Label(master = self._root_window, text = ('Black:{}'.format(self.game.black)
                                            +'White:{}'.format(self.game.white)),
                                        font = DEFAULT_FONT)
            self.count_label.grid(
            row = 6, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

    def was_finishb_clicked(self):
        '''
        This function will return True if the user placed all the black discs
        before the game start.
        '''
        return self._clicked_finishB


    def on_finishb(self):
        '''
        This function will allow the user to put white discs after they finished
        putting black discs before the game start.
        '''
        self._clicked_finishB = True
        self.color = 'W'
        self.place_white()
        self.black_place_ok_button.grid_remove()
        
    def place_white(self):
        '''
        This function will initialize a button for user to start the game when
        they finished making a board(Put black and white discs on it).
        '''
        self.configure_done_button = tkinter.Button(
            master = self._root_window, text = 'Finish Config', font = DEFAULT_FONT,
            command = self.start_real_game)

        self.configure_done_button.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)   

    def start_real_game(self):
        '''
        When the user clicked the finish config button, the game will start. When user
        makes a move, the board information will get updated.
        '''
        self.configure_done_button.grid_remove()
        self.is_setting_board = False

  
        self.turn_label = tkinter.Label(master = self._root_window, text = '', font = DEFAULT_FONT)
        self.turn_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self.count_label = tkinter.Label(master = self._root_window, text = ('Black:{}'.format(self.game.black)
                                            +'White:{}'.format(self.game.white)),
                                        font = DEFAULT_FONT)
        self.count_label.grid(
            row = 6, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self.update_infor()

    def get_game_row_col(self):
        '''
        This function will get the row delta and col delta for locating
        the disc's position.
        '''
        row_number = self.row_delta
        col_number = self.col_delta

        return row_number, col_number
        
    def update_infor(self):
        '''
        This function will update the board's information including the turn, the
        number of the white and black discs and the winner. While game is not over,
        the game will just continue for a user to make a move.
        '''
        self.game.count_discs()

        if self.game.game_over():

            winner = self.game.winner()

            self.turn_label['text'] = 'Winner: {}'.format(winner)
            
        else:

            if not self.game.is_this_color_can_drop(self.game.turn):

                self.game.change_turn()

            self.turn_label['text'] = 'Turn: {}'.format(self.game.turn)
        self.count_label['text'] = 'Black:{}'.format(self.game.black)+'White:{}'.format(self.game.white)
        

if __name__ == '__main__':
    main_menu((disc_models.DiscState())).run()
