import numpy as np
from oscillators import Oscillators

class AudioProcessorGeneric:
    def __init__(self, fs=44100):
        self.samplerate = fs
        self.os = Oscillators()
        self._event_chain()

    def _event_chain(self):
        self.on_start_up()
        self.process_block()
        self.post_process()

    def set_process_time(self, seconds):
        self.process_time = self.samplerate * seconds
        self.output_stream = np.zeros(self.process_time)

    def on_start_up(self):
        raise NotImplementedError("Need to implement 'on_start_up()' method.")

    def process_block(self):
        raise NotImplementedError("Need to implement 'process_block()' method.")

    def post_process(self):
        raise NotImplementedError("Need to implement 'post_process()' method.")





