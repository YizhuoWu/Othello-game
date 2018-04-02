'''
Yizhuo Wu 14863527
'''
import math

class Disc:
    '''
    This class will provide the information for a certain clicked point(spot).
    '''
    def __init__(self,frac_x: float, frac_y: float):
        '''
        This function will initialize the x and y position on the board.
        '''
        self._frac_x = frac_x
        self._frac_y = frac_y
        self.row_delta = 1
        self.col_delta = 1
        
    def frac_cordi(self):
        '''
        This function will return the fractional cordinates of the point.
        '''
        return (self._frac_x, self._frac_y)

    def pixel_cordi(self, width: float, height: float,row_number:int, col_number:int):
        '''
        This function will give the position of a spot in the board by using
        the column delta and row delta.
        '''
        row_delta = self.row_delta
        col_delta = self.col_delta

        if (self._frac_x * width)-(width/col_number)*col_delta < 0 and (self._frac_y * height)-(height/row_number)*row_delta < 0:

            return(int(2*(col_delta-1)+1)*(600/(2*col_number)), int(2*(row_delta-1)+1)*(600/(2*row_number)))

        if (self._frac_x * width)-(width/col_number)*col_delta > 0 and (self._frac_y * height)-(height/row_number)*row_delta < 0:

            self.col_delta+=1

            self.pixel_cordi(width, height,row_number,col_number)

        if (self._frac_x * width)-(width/col_number)*col_delta < 0 and (self._frac_y * height)-(height/row_number)*row_delta > 0:

            self.row_delta+=1

            self.pixel_cordi(width, height,row_number,col_number)
        if (self._frac_x * width)-(width/col_number)*col_delta > 0 and (self._frac_y * height)-(height/row_number)*row_delta > 0:

            self.row_delta+=1
            self.col_delta+=1

            self.pixel_cordi(width, height,row_number,col_number)            

    def dis_between_points(self, p:'Point') -> float:
        '''
        This function will return the distance between two points.
        '''
        return math.sqrt(
            (self._frac_x - p._frac_x) * (self._frac_x - p._frac_x)
            + (self._frac_y - p._frac_y) * (self._frac_y - p._frac_y))

def create_frac_point(frac_x: float, frac_y: float):
    '''
    This function will return the point's fraction cordinates.
    '''
    return Disc(frac_x, frac_y)

def from_pixel(pixel_x: float, pixel_y: float, width: float, height: float) -> Disc:
    '''
    This function will return the point's pixel cordinates.
    '''
    return Disc(pixel_x / width, pixel_y / height)
