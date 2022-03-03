import numpy as np
from pysoundtoolz.lookup_tables import sin_lookup, saw_lookup, sqr_lookup, tri_lookup, table_size, cos_lookup


class Osc:
    def __init__(self, fs=44100):
        self.fs = fs
        self.frequency = 0
        self.step = 0
        self.counter = 0

    def _update_osc(self, frequency):
        self.frequency = frequency
        self.step = (table_size * frequency) / self.fs
        if self.step % int(self.step) >= 0.5:
            self.step = int(np.ceil(self.step))
        else:
            self.step = int(np.floor(self.step))


class Sinosc(Osc):
    def sinosc(self, frequency):
        if self.frequency != frequency:
            self._update_osc(frequency)
        amplitude_value = sin_lookup[self.counter]
        self.counter = (self.counter + self.step) % table_size
        return amplitude_value


class Cososc(Osc):
    def cososc(self, frequency):
        if self.frequency != frequency:
            self._update_osc(frequency)
        amplitude_value = cos_lookup[self.counter]
        self.counter = (self.counter + self.step) % table_size
        return amplitude_value


class Sawosc(Osc):
    def sawosc(self, frequency):
        if self.frequency != frequency:
            self._update_osc(frequency)
        amplitude_value = saw_lookup[self.counter]
        self.counter = (self.counter + self.step) % table_size
        return amplitude_value


class Sqrosc(Osc):
    def sqrosc(self, frequency):
        if self.frequency != frequency:
            self._update_osc(frequency)
        amplitude_value = sqr_lookup[self.counter]
        self.counter = (self.counter + self.step) % table_size
        return amplitude_value


class Triosc(Osc):
    def triosc(self, frequency):
        if self.frequency != frequency:
            self._update_osc(frequency)
        amplitude_value = tri_lookup[self.counter]
        self.counter = (self.counter + self.step) % table_size
        return amplitude_value
