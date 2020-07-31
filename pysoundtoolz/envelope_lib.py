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
        self.bpm = 0
        self.digital_period = 0
    
    def clock_hz(self, frequency):
        """
        This clock periodically returns a value of 1 at the desired frequency. 
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
    
    def clock_bpm(self, bpm):
        if self.bpm != bpm:
            self.bpm = bpm
            self.digital_period = int((60.0/bpm)*self.fs)
        self.counter = (self.counter + 1) % self.digital_period
        if self.counter == 0:
            return 1
        else:
            return 0

class Score:
    def __init__(self, s, fs=44100): 
        self.fs = fs
        self.s = s
        self.counter = 0
        
        self.current_note = 0
        self._time_score()
        self.number_of_notes = len(self.time) 
        self.frequency = self.s[0][1]

    def _time_score(self):
        self.time = np.array([], dtype=int)
        for i, item in enumerate(self.s):
            self.time = np.append(int(item[0] * self.fs), self.time)
    
    def score(self):
        if self.current_note < self.number_of_notes:
            self.counter += 1
            if self.counter % self.time[self.current_note] == 0:
                self.current_note += 1
                if self.current_note < self.number_of_notes:
                    self.frequency = self.s[self.current_note][1]

    def get_current_frequency(self):
        return self.frequency