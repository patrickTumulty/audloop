import numpy as np
import soundfile as sf
from abc import ABCMeta, abstractmethod
from audloop import *


class AudioProcessorGeneric:
    __metaclass__ = ABCMeta

    def __init__(self, fs=44100):
        self.fs = fs
        self.fio = AudioFileHandler()
        self._event_chain()

    def _event_chain(self):
        self.on_start_up()
        self.process_block()
        self.post_process()

    def set_process_time(self, time, mode='seconds'):
        """
        Set the length of the process block audio loop as well as the length 
        of the output stream array. 

        time : int or float (Depends on mode)
            Set audio loop duration as well as output stream length

        mode : string
            Either 'seconds' or 'samples'. Dictates how you want to define time. 
            Recommended to use samples when making the audio loop the same length as an imported audio file. 
        """
        if mode.lower() == 'seconds':
            self.process_time = int(self.fs * time)
        elif mode.lower() == 'samples':
            self.process_time = time
        self.output_stream = np.zeros(self.process_time)

    @abstractmethod
    def on_start_up(self):
        raise NotImplementedError("Need to implement 'on_start_up()' method.")

    @abstractmethod
    def process_block(self):
        raise NotImplementedError("Need to implement 'process_block()' method.")

    @abstractmethod
    def post_process(self):
        raise NotImplementedError("Need to implement 'post_process()' method.")


class AudioFileHandler:
    def __init__(self, fs=44100):
        self.fs = fs
        self.imported_audio = 0
        self.length_samples = 0
        self.length_seconds = 0
        self.is_stereo = False

    def read_wav(self, filename):
        """
        Import audio file. 

        fileName : string
            Name, or file path, for local wav file to be imported. 
        """
        f = sf.read(filename)
        self.fs = f[1]
        self.imported_audio = f[0]
        self.length_samples = len(self.imported_audio)
        self.length_seconds = round(self.length_samples / self.fs, 2)
        if len(self.imported_audio.shape) == 2:
            self.is_stereo = True
        self._file_info_printer(filename)

    def _file_info_printer(self, fileName):
        print("{} | Is Stereo : {} | SampleRate : {} | Length : {}s".format(fileName, self.is_stereo, self.fs,
                                                                            self.length_seconds))

    def write_wav(self, name, data, playback=False):
        """
        Export audio to wav file. 

        name : string 
            Filename

        data : numpy array
            Audio data 
        """
        print("Writing {} ...".format(name))
        sf.write(name, data, self.fs)
        if playback:
            self._play_wav(name)

    def _play_wav(self, name):
        print("Playing {} ...".format(name))
