import numpy as np
import matplotlib.pyplot as plt

class EnvGen:
    def __init__(self, break_points, fs=44100): # [(0.2, 1),(0.5, 0.3),(0.1, 0)]
        """
        Generate linear amplitude ramps in between defined breakpoints. 

        break_points : List of ordered pair of floats
            Example : [(0.2, 1),(0.5, 0.3),(2, 0)]
            Envelope starts at zero. The first value dictates time in milliseconds and the 
            second value dictates amplitude. Define as many breakpoints as you want. 
            Note: Envelope will start at zero but won't return to zero unless specified. See example. 
        """
        self.fs = fs
        self.bp = break_points
        self.counter = 0
        self.env_table = self.create_envelope()
        self.l = len(self.env_table)

    def create_envelope(self):
        last = 0
        l = len(self.bp)
        for i, item in enumerate(self.bp):
            s = int(item[0] * self.fs)
            if i == 0:
                env = np.linspace(0, item[1], s)
            else:
                env = np.append(env, np.linspace(last, item[1], s))
            last = item[1]
        return env

    def env(self, trigger):
        if trigger == 1:
            self.counter = 0
        self.counter += 1
        if self.counter < self.l:
            return self.env_table[self.counter]
        else:
            return 0
            


class Clock:
    def __init__(self, fs=44100):
        self.fs = fs
        self.counter = 0
        self.frequency = 0
        self.digital_period = 0
    
    def clock(self, frequency):
        """
        This clock periodically returns 1 at the desired frequency. 
        Will return zero at all other times. 

        frequency : float
        """
        if self.frequency != frequency:
            self.frequency = frequency
            self.digital_period = int(self.fs/self.frequency)
        self.counter = (self.counter + 1) % self.digital_period
        if self.counter == 0:
            return 1
        else:
            return 0


