# pySoundToolz
pySoundToolz is a developing library designed for streamlined audio programming in Python

# Example

The code below is a suggested use case. Simply create a class that inherits from the `AudioProcessorGeneric` class. 
The three methods `on_start_up()`, `process_block()`, and `post_process()` need to be implemented. You need to at the very 
least put `pass` in each method to get the class to run. The names suggest when, and how they are imeplemtned. All
modules of pySoundToolz will be available as member variables of this class. For example, oscillators can be accessed 
through the `.os` variable. 

```python
import soundfile as sf
from audioprocessorgeneric import AudioProcessorGeneric

class AudioProcessor(AudioProcessorGeneric):
    def on_start_up(self):
        self.set_process_time(5) # <--- set how long your audio loop will be (5 seconds)
        self.os.create_sin_oscillators(3) # <--- create 3 oscillators 
  
    def process_block(self):
        for i in range(self.process_time): # <--- number of samples for 5 seconds of audio
            self.output_stream[i] += self.os.sinosc(440, 1)
  
    def post_process(self):
        sf.write("example.wav", self.output_stream, self.samplerate)

```
