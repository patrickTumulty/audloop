import numpy as np


class WhiteNoise:
    def __init__(self, fs=44100):
        self.fs = fs
        self.counter = 0
        self.frequency = 0
        self.digital_period = 0
        self.val = 0

    def whitenoise(self):
        return np.random.uniform(-1, 1, 1)[0]
    
    def whitenoise_range(self, mI, mA, frequency):
        if self.frequency != frequency:
            self.frequency = frequency
            self.digital_period = int(self.fs/self.frequency)
        self.counter += 1
        if self.counter % self.digital_period == 0:
            self.val = np.random.uniform(mI, mA, 1)[0]
        return self.val