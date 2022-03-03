import numpy as np


class WhiteNoise:
    def __init__(self, fs=44100):
        self.fs = fs
        self.counter = 0
        self.frequency = 0
        self.digital_period = 0
        self.val = 0

    def whitenoise_range(self, range_low, range_high, frequency):
        """
        Generate values between range_low and range_high at the target frequency using a uniform distribution

        :param range_low: range low value
        :param range_high: range high value
        :param frequency: frequency (hz)
        :return: white noise value between 0 and 1
        """
        if self.frequency != frequency:
            self.frequency = frequency
            self.digital_period = int(self.fs / self.frequency)
        self.counter += 1
        if self.counter % self.digital_period == 0:
            self.val = np.random.uniform(range_low, range_high, 1)[0]
        return self.val
