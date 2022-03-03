import numpy as np
from pysoundtoolz import *


# =========================================
#  CODE IN PROGRESS
# =========================================
class Transpose:
    def __init__(self, window, crossfade):
        self.max_delay = 65536
        self.window = window
        self.fd1 = FDelay(self.max_delay)
        self.fd2 = FDelay(self.max_delay)
        self.dt = 0

    def transpose(self, x, semitone):
        self.calc(semitone, self.window)
        return self.fd1.fdelay(x, self.dt) * np.fmin(self.dt / x, 1) + self.fd2.fdelay(x, self.dt + self.window) * (
                    1 - np.fmin(self.dt / x, 1))

    def calc(self, semitone, window):
        i = 1 - np.power(2, semitone / 12) + self.dt
        d = np.fmod((i + window), window)
        self.dt = d


# =========================================


class Flanger:
    def __init__(self):
        """
        Simple flanger audio effect. 
        """
        self.de = Delay(128)
        self.s1 = Sinosc()

    def flanger(self, signal, frequency=2, depth=1, wet=1):
        """
        Simple flanger audio effect. 

        Parameters: 

        signal : float
            Audio sample

        frequency : int or float
            Speed of flanger oscillation

        depth : float (0 < depth <= 1)
            Depth of the effect
        
        wet : float (0 < wet < <= 1)
            Level at which flange signal is added to the original
        """
        wav = ((self.s1.sinosc(frequency) + 1) * 63) * depth
        return signal + (self.de.delay(signal, int(wav)) * wet)
