import numpy as np
import matplotlib.pyplot as plt

class EnvGen:
    def __init__(self, break_points, fs=44100): # [(0.2, 1),(0.5, 0.3),(2, 0)]
        self.fs = fs
        self.bp = break_points
        self.env = self.create_envelope()

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


e = EnvGen([(0.2, 1),(0.5, 0.3),(0.6, 2),(2, 0)])

plt.plot(e.env)
plt.show()