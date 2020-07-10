# pySoundToolz
`pySoundToolz` is a library in development. Its purpose is to enable similar functionality to that of sound specific languages/programs such as SuperCollider, FAUST, or MAX-MSP, but in a Python programming environment. `pySoundToolz`, in its current state, will run all audio DSP offline. Audio is meant to be read in as a wav file or synthesized from scratch and then exported as a new file. With that said, all `pySoundToolz` modules are coded as if they are running in a realtime audio loop. This design choice was made so that any algorithms written with `pySoundToolz` could be ported over to other languages, such as C++, to do realtime DSP. 

# Example

The code below is a suggested use case. Simply create a class that inherits from the `AudioProcessorGeneric` class. 
The three methods `on_start_up()`, `process_block()`, and `post_process()` need to be implemented. You need to, at the very 
least, put `pass` in each method to get the class to run. The names suggest when each one will be executed at runtime.

## Applying A Flanger Effect To An Imported Audio File
```python
from pysoundtoolz import AudioProcessorGeneric
import pysoundtoolz as pst

class AudioProcessor(AudioProcessorGeneric):
    def on_start_up(self):
        self.fio.import_audio("EXAMPLE_FILE.wav")  # import wav file
        self.set_process_time(self.fio.length_samples, 'samples') # set the audio loop to be the same length as the imported audio. 
        self.fl = pst.Flanger() # initialize the Flanger module
  
    def process_block(self):
        for i in range(self.process_time): 
            self.output_stream[i] += self.fl.flanger(self.fio.imported_audio[i], 2, 0.6, 0.3) # calling the flanger module in the audio loop 
            
    def post_process(self):
        self.fio.export_audio("EXAMPLE_OUTPUT.wav", self.output_stream)

```

## Creating A Random Melody Using A Saw Wave 
```python
class PTAudioProcessor(AudioProcessorGeneric):
    def on_start_up(self):
        self.set_process_time(10)
        self.s1 = pst.Sawosc()
        self.en = pst.EnvGen([(0.01, 1),(0.2, 0)])
        self.cl = pst.Clock() 
        self.no = pst.WhiteNoise()

    def process_block(self):
        for i in range(self.process_time):
            f = self.no.whitenoise_range(200, 1000, 2) 
            self.output_stream[i] += self.s1.sawosc(f) * self.en.env(self.cl.clock(2))

    def post_process(self):
        self.fio.export_audio('saw_melody.wav', self.output_stream)
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
`EnvGen` `Clock`

## Delays
`Delay` `FDelay`

## Effects
`Flanger`
`Transpose` In progress 

