'''
Yizhuo Wu 14863527
'''
import my_points
import math

class Disc:
    '''
    This class will initialize the point of user's clicked point.
    '''
    def __init__(self,center: my_points.Disc,radius_frac: float,color:str):
        '''
        This function will initialize the center, radius and color of a spot(point).
        '''
        self._center = center
        self._radius_frac = radius_frac
        self.color = color

    def center(self) -> my_points.Disc:
        '''
        This fucntion will return the center of the point.
        '''        
        return self._center

    def radius_frac(self) -> float:
        '''
        This fucntion will return the radius frac of the point.
        '''
        return self._radius_frac

    def contains(self, point: my_points.Disc) -> bool:
        return self._center.dis_between_points(point) <= self._radius_frac
    
class DiscState:
    '''
    This class will provide a list of the spots.
    '''
    def __init__(self):
        '''
        This function will return an empty list.
        '''
        self._spots = []


    def all_spots(self):
        '''
        This funtion will return the list of spots.
        '''
        return self._spots


    def handle_click(self, click_point: my_points.Disc, DISC_RADIUS,color) -> None:
        '''
        This function will append the spot to a list when the user click on the board.
        '''
        self._spots.append(Disc(click_point, DISC_RADIUS,color))

