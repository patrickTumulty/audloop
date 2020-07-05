import numpy as np
from pysoundtoolz import *

class Flanger:
    def __init__(self):
        self.osc = Oscillators()
        self.osc.create_sin_oscillators(1)
        self.de = Delays()
        self.de.create_delay(1, 128)

    def flanger(self, x, frequency=2, depth=1, wet=1):
        """
        x : float
            Audio signal input

        frequency : int or float
            Speed of flanger oscillation

        depth : float (0 < depth <= 1)
            Depth of the effect
        
        wet : float (0 < wet < <= 1)
            Level at which flange signal is added to the original
        """
        wav = ((self.osc.sinosc(frequency, 1) + 1) * 63) * depth
        return x + (self.de.delay(x, int(wav), 1) * wet) 

        