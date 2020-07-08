import numpy as np


class DelayBuffer:
    def __init__(self, length):
        self.items = np.zeros(length)
        self.max_length = length
        self.read_point = 0;
    
    def set_read_point(self, i):
        self.read_point = i

    def push(self, value):
        self.items = np.roll(self.items, 1)
        self.items[0] = value

    def read(self):
        return self.items[self.read_point]


class Delay:
    def __init__(self, max_length):
        self.buffer = DelayBuffer(max_length)
    
    def delay(self, x, n):
        """
        Sample delay.

        x : float
            Audio signal

        n : int 
            Delay length in samples
        """
        if self.buffer.read_point != n:
            self.buffer.set_read_point(n)
        self.buffer.push(x)
        return self.buffer.read()


class FDelay:
    def __init__(self, max_length):
        self.d1 = Delay(max_length + 1)
        self.d2 = Delay(max_length + 1)
        self.frac = 0.0

    def fdelay(self, x, n):
        """
        Simple 'n' samples fractional delay based on 2 interpolated
        delay lines. 

        x : float
            Audio signal.

        n : int or float
            Delay length in samples 
        """
        if (samples % 1) != self.frac:
            self.frac = samples
        return self.d1.delay(x, int(n))*(1-self.frac) + self.d2.delay(x, int(n)+1)*(self.frac)

# Below is deprecated code 
class Delays:
    def __init__(self):
        self._delays = {}

    def create_delay(self, delay_id, max_delay):
        self._delays[delay_id] = DelayBuffer(max_delay)

    def delay(self, signal, samples, delay_id):
        de = self._delays[delay_id]
        if de.read_point != samples:
            de.read_point = samples
            de.set_read_point(samples)
        de.push(signal)
        return de.read()








        