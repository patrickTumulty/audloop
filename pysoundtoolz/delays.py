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








        