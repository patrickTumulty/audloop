import numpy as np

class utility:
    @staticmethod
    def rad2deg(radian):
        """
        Simple radian to degree conversion.

        radian : float
        """
        return radian * (180/np.pi)

    @staticmethod
    def deg2rad(degree):
        """
        Simple degree to radian conversion. 

        degree : float
        """
        return degree * (np.pi/180)

    @staticmethod
    def const_pwr_pan(p):
        """
        Constant power pan calculator. p is a value from -100 to 100. 
        -100 being panned left, 100 panned right.  

        p : int
            Panning value
        """
        p = (p*0.5)+50
        theta = p*(np.pi/200)
        return (np.cos(theta), np.sin(theta))
        
    @staticmethod
    def lin_pan(p):
        """
        Linear pan calculator. p is a value from -100 to 100. 
        -100 being panned left, 100 panned right.  

        p : int
            Panning value
        """
        p = ((p*0.5)+50) * 0.01
        return (1 - p, p)







    
