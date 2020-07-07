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
    
    def delay(self, x, samples):
        """
        Sample delay.

        x : float
            Audio signal

        samples : int 
            Signal delayed by indicated number of samples
        """
        if self.buffer.read_point != samples:
            self.buffer.set_read_point(samples)
        self.buffer.push(x)
        return self.buffer.read()


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








        