# audloop
`audloop` is a library in development. Its purpose is to enable rapid prototyping of DSP algorithms and/or audio synthesis 
experimentation in a Python programming environment. 

`audloop` will run all audio DSP offline. Audio is meant to be read in as a wav file or synthesized from scratch. The 
audible result will be a newly written wav file.

This library aims to achieve similar functionality to that of sound specific languages/programs 
such as SuperCollider, FAUST, or MAX-MSP. Unlike those programs, `audloop` is written entirely in the general purpose
language Python. This means that nothing is abstracted from the user. Because Python is general purpose, algorithms 
written in `audloop` can be ported to other general purpose languages such as C++. To further enable coherency with 
`audloop` and realtime DSP environment, all `audloop` modules are coded as if they are running in a realtime audio loop. 
This design choice was specifically made so that algorithms written with `audloop` could be ported into a realtime DSP
environment via another general purpose language.

# Quick Start

The code below is a suggested use case. Simply create a class that inherits from the `AudioProcessorGeneric` class. 
The three methods `on_start_up()`, `process_block()`, and `post_process()` need to be implemented. You need to, at the very 
least, put `pass` in each method to get the class to run. The names suggest when each one will be executed at runtime.

## Applying A Flanger Effect To An Imported Audio File

```python
from audloop import AudioProcessorGeneric
import audloop as pst


class AudioProcessor(AudioProcessorGeneric):
    def on_start_up(self):
        self.fio.read_wav("EXAMPLE_FILE.wav")  # import wav file
        self.set_process_time(self.fio.length_samples,
                              'samples')  # set the audio loop to be the same length as the imported audio. 
        self.fl = pst.Flanger()  # initialize the Flanger module

    def process_block(self):
        for i in range(self.process_time):
            self.output_stream[i] += self.fl.flanger(self.fio.imported_audio[i], 2, 0.6,
                                                     0.3)  # calling the flanger module in the audio loop 

    def post_process(self):
        self.fio.write_wav("EXAMPLE_OUTPUT.wav", self.output_stream)

```

## Creating A Random Melody Using A Saw Wave 
```python
class PTAudioProcessor(AudioProcessorGeneric):
    def on_start_up(self):
        self.set_process_time(10)
        self.s1 = pst.Sawosc()                     # Initialize Sawosc module
        self.en = pst.EnvGen([(0.01, 1),(0.2, 0)]) # Generate a linear envelope from breakpoints
        self.cl = pst.Clock()                      # Intialize Clock
        self.no = pst.WhiteNoise()                 # Initialize Whitenoise

    def process_block(self):
        for i in range(self.process_time):
            f = self.no.whitenoise_range(200, 1000, 2)                                  # Value between 200 and 1000 every 2Hz 
            self.output_stream[i] += self.s1.sawosc(f) * self.en.env(self.cl.clock(2))  # clock will trigger envelope every 2Hz 

    def post_process(self):
        self.fio.write_wav('saw_melody.wav', self.output_stream)
```

# Current Modules Available

`AudioProcessorGeneric`

## Oscillators
`Sinosc`
`Cososc`
`Sawosc`
`Triosc` 
`Sqrosc`

## Noise
`Whitenoise`

## Envelopes / Clocks
`EnvGen` `Clock` `Score`

## Analysis 
`RMSDetector`
`PeakDetector`

## Delays
`Delay` `FDelay`

## Effects
`Flanger`

## Utility
`rad2deg` 
`deg2rad`
`lin_pan`
`const_pwr_pan`

