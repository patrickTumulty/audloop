import numpy as np
import soundfile as sf
from pysoundtoolz import *

class AudioProcessorGeneric:
    def __init__(self, fs=44100):
        self.fs = fs
        self.fio = AudioFileHandler()
        self._event_chain()

    def _event_chain(self):
        self.on_start_up()
        self.process_block()
        self.post_process()

    def set_process_time(self, time, mode='seconds'):
        if mode.lower() == 'seconds':
            self.process_time = int(self.fs * time)
        elif mode.lower() == 'samples':
            self.post_process = time
        self.output_stream = np.zeros(self.process_time)

    def on_start_up(self):
        raise NotImplementedError("Need to implement 'on_start_up()' method.")

    def process_block(self):
        raise NotImplementedError("Need to implement 'process_block()' method.")

    def post_process(self):
        raise NotImplementedError("Need to implement 'post_process()' method.")


class AudioFileHandler:
    def __init__(self, fs=44100):
        self.fs = fs
        self.imported_audio = 0
        self.length_samples = 0
        self.length_seconds = 0
        self.is_stereo = False

    def import_audio(self, fileName):
        f = sf.read(fileName)
        self.fs = f[1]
        self.imported_audio = f[0]
        self.length_samples = len(self.imported_audio) 
        self.length_seconds = round(self.length_samples / self.fs, 2) 
        if len(self.imported_audio.shape) == 2:
            self.is_stereo = True
        self.file_info_printer(fileName)

    def file_info_printer(self, fileName):
        print("{} | Is Stereo : {} | SampleRate : {} | Length : {}s".format(fileName, self.is_stereo, self.fs, self.length_seconds))

    def export_audio(self, name, data):
        print("Writing {} ...".format(name))
        sf.write(name, data, self.fs)