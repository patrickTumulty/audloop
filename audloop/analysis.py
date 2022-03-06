import numpy as np
from audloop import *


class RMSDetector:
    def __init__(self, fs=44100):
        """
        This envelope detector provides an approximation of an RMS envelope. The 
        result is very close to that of a proper RMS calculation while being
        more efficient. One different is the time constant component. 
        """
        self.fs = fs
        self.t = 0.1
        self.alpha = np.exp(-1 / (self.t * self.fs))
        self.prev = 0

    def rms_detector(self, signal, t=0.01):
        """
        This envelope detector provides an approximation of an RMS envelope. The 
        result is very close to that of a proper RMS calculation while being
        more efficient. One different is the time constant component. 

        Parameters:

        signal : float
            Audio sample    
        
        t : float
            Speed, in seconds, that the envelope detector reacts to changes
            in the signal. 
        """
        if self.t != t:
            self.t = t
            self.alpha = np.exp(-1 / (t * self.fs))
        self.prev = np.sqrt((self.alpha * (self.prev ** 2)) + ((1 - self.alpha) * (signal ** 2)))
        return self.prev


class PeakDetector:
    def __init__(self, fs=44100):
        """
        Level corrected peak envelope detector. Provides immediate responsiveness 
        to transient signals with an adjustable decay release time. 
        """
        self.fs = fs
        self.t = 0.01
        self.rA = np.exp(-1 / (self.t * self.fs))
        self.prev = 0

    def _recalc_coef(self, rel):
        self.t = rel
        self.rA = np.exp(-1 / (self.t * self.fs))

    def peak_detector(self, signal, rel=0.01):
        """
        Level corrected peak envelope detector. Provides immediate responsiveness 
        to transient signals with an adjustable decay release time. 

        Parameters:

        signal : float
            Audio sample

        t : float 
            Peak detector decay time in seconds
        """
        if (rel != self.t):
            self._recalc_coef(rel)
        signal = np.abs(signal)
        if signal > self.prev:
            self.prev = signal
        else:
            self.prev = (self.rA * self.prev) + ((1 - self.rA) * signal)
        return self.prev
