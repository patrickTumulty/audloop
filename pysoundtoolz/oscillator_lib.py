import numpy as np
from pysoundtoolz.lookup_tables import sin_lookup, sin_lookup, saw_lookup, sqr_lookup, tri_lookup, table_size


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


class Oscillators: 
    def __init__(self, fs=44100):
        self.fs = fs
        self._sin_oscillators = []
        self._cos_oscillators = []
        self._saw_oscillators = []
        self._tri_oscillators = []
        self._sqr_oscillators = []

    def create_sin_oscillators(self, number=1):
        """
        Indicate the number of independent sin (sinosc()) oscillators 
        that you want available. 

        number : int
            Number of independent sin oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter" : 0,
                "frequency" : 0
            }
            self._sin_oscillators.append(new_osc)

    def create_cos_oscillators(self, number=1):
        """
        Indicate the number of independent cos (cososc()) oscillators 
        that you want available. 

        number : int
            Number of independent cos oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter": 0,
                "frequency": 0,
            }
            self._cos_oscillators.append(new_osc) 
    
    def create_saw_oscillators(self, number=1):
        """
        Indicate the number of independent saw (sawosc()) oscillators 
        that you want available. 

        number : int
            Number of independent saw oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter": 0,
                "frequency": 0,
            }
            self._saw_oscillators.append(new_osc)

    def create_tri_oscillators(self, number=1):
        """
        Indicate the number of independent triangle (triosc()) oscillators 
        that you want available. 

        number : int
            Number of independent triangle oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter": 0,
                "frequency": 0,
            }
            self._tri_oscillators.append(new_osc)
    
    def create_sqr_oscillators(self, number=1):
        """
        Indicate the number of independent square (sqrosc()) oscillators 
        that you want available. 

        number : int
            Number of independent square oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter" : 0,
                "frequency" : 0
            }
            self._sqr_oscillators.append(new_osc)

    def _update_osc(self, osc_dict, frequency):
        osc_dict["frequency"] = frequency
        osc_dict["step"] = (table_size * frequency) / self.fs
        if osc_dict["step"] % int(osc_dict["step"]) >= 0.5:
            osc_dict["step"] = int(np.ceil(osc_dict["step"]))
        else:
            osc_dict["step"] = int(np.floor(osc_dict["step"])) 

    def sinosc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._sin_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_sin_oscillators()' first.")
        osc_dict = self._sin_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = sin_lookup[osc_dict["counter"]]
        osc_dict["counter"] = (osc_dict["counter"] + osc_dict["step"]) % table_size
        return amplitude_value

    def cososc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._cos_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_cos_oscillators()' first.")
        osc_dict = self._cos_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = cos_lookup[osc_dict["counter"]]
        osc_dict["counter"] += osc_dict["step"]
        osc_dict["counter"] %= table_size
        return amplitude_value

    def sawosc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._saw_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_saw_oscillators()' first.")
        osc_dict = self._saw_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = saw_lookup[osc_dict["counter"]]
        osc_dict["counter"] += osc_dict["step"]
        osc_dict["counter"] %= table_size
        return amplitude_value

    def triosc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._tri_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_tri_oscillators()' first.")
        osc_dict = self._tri_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = tri_lookup[osc_dict["counter"]]
        osc_dict["counter"] += osc_dict["step"]
        osc_dict["counter"] %= table_size
        return amplitude_value

    def sqrosc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._sqr_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_sqr_oscillators()' first.")
        osc_dict = self._sqr_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = sqr_lookup[osc_dict["counter"]]
        osc_dict["counter"] += osc_dict["step"]
        osc_dict["counter"] %= table_size
        return amplitude_value



class Oscillators2: 
    def __init__(self, fs=44100):
        self.fs = fs
        self.pi2 = np.pi * 2
        self.table_size = 2**16
        self._sin_oscillators = []
        self._cos_oscillators = []
        self._saw_oscillators = []
        self._tri_oscillators = []
        self._sqr_oscillators = []
        self._generate_sin_table()
        self._generate_cos_table()
        self._generate_saw_table()
        self._generate_tri_table()
        self._generate_sqr_table()

    def create_sin_oscillators(self, number=1):
        """
        Indicate the number of independent sin (sinosc()) oscillators 
        that you want available. 

        number : int
            Number of independent sin oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter" : 0,
                "frequency" : 0
            }
            self._sin_oscillators.append(new_osc)

    def create_cos_oscillators(self, number=1):
        """
        Indicate the number of independent cos (cososc()) oscillators 
        that you want available. 

        number : int
            Number of independent cos oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter": 0,
                "frequency": 0,
            }
            self._cos_oscillators.append(new_osc) 
    
    def create_saw_oscillators(self, number=1):
        """
        Indicate the number of independent saw (sawosc()) oscillators 
        that you want available. 

        number : int
            Number of independent saw oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter": 0,
                "frequency": 0,
            }
            self._saw_oscillators.append(new_osc)

    def create_tri_oscillators(self, number=1):
        """
        Indicate the number of independent triangle (triosc()) oscillators 
        that you want available. 

        number : int
            Number of independent triangle oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter": 0,
                "frequency": 0,
            }
            self._tri_oscillators.append(new_osc)
    
    def create_sqr_oscillators(self, number=1):
        """
        Indicate the number of independent square (sqrosc()) oscillators 
        that you want available. 

        number : int
            Number of independent square oscillators
        """
        for i in range(number):
            new_osc = {
                "step" : 0,
                "counter" : 0,
                "frequency" : 0
            }
            self._sqr_oscillators.append(new_osc)

    def _generate_sin_table(self):
        self._sin_lookup = np.sin(np.linspace(0, self.pi2, self.table_size))

    def _generate_cos_table(self):
        self._cos_lookup = np.cos(np.linspace(0, self.pi2, self.table_size))
    
    def _generate_saw_table(self):
        self._saw_lookup = np.append(np.linspace(0, 1, int(self.table_size/2)), np.linspace(-1, 0, int(self.table_size/2))) 

    def _generate_tri_table(self):
        ramp = int(self.table_size / 4)
        self._tri_lookup = np.append(np.linspace(0, 1, ramp + 1)[:-1], np.append(np.linspace(1, -1, ramp*2), np.linspace(-1, 0, ramp + 1)[1:]))     
    
    def _generate_sqr_table(self):
        self._sqr_lookup = np.append(np.ones(int(self.table_size/2)), np.ones(int(self.table_size/2))*-1)

    def _update_osc(self, osc_dict, frequency):
        osc_dict["frequency"] = frequency
        osc_dict["step"] = (self.table_size * frequency) / self.fs
        if osc_dict["step"] % int(osc_dict["step"]) >= 0.5:
            osc_dict["step"] = int(np.ceil(osc_dict["step"]))
        else:
            osc_dict["step"] = int(np.floor(osc_dict["step"])) 

    def sinosc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._sin_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_sin_oscillators()' first.")
        osc_dict = self._sin_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = self._sin_lookup[osc_dict["counter"]]
        osc_dict["counter"] = (osc_dict["counter"] + osc_dict["step"]) % self.table_size
        return amplitude_value

    def cososc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._cos_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_cos_oscillators()' first.")
        osc_dict = self._cos_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = self._cos_lookup[osc_dict["counter"]]
        osc_dict["counter"] += osc_dict["step"]
        osc_dict["counter"] %= self.table_size
        return amplitude_value

    def sawosc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._saw_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_saw_oscillators()' first.")
        osc_dict = self._saw_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = self._saw_lookup[osc_dict["counter"]]
        osc_dict["counter"] += osc_dict["step"]
        osc_dict["counter"] %= self.table_size
        return amplitude_value

    def triosc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._tri_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_tri_oscillators()' first.")
        osc_dict = self._tri_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = self._tri_lookup[osc_dict["counter"]]
        osc_dict["counter"] += osc_dict["step"]
        osc_dict["counter"] %= self.table_size
        return amplitude_value

    def sqrosc(self, frequency, osc_num):
        """
        frequency : float or int
            Frequency in Hertz
        
        osc_num : int
            Indicate a unique oscillator 
            Note : Numbering starts at 1 (Not 0)
        """
        if len(self._sqr_oscillators) == 0:
            raise AssertionError("No oscillators created. Run 'create_sqr_oscillators()' first.")
        osc_dict = self._sqr_oscillators[osc_num - 1]
        if osc_dict["frequency"] != frequency:
            self._update_osc(osc_dict, frequency)
        amplitude_value = self._sqr_lookup[osc_dict["counter"]]
        osc_dict["counter"] += osc_dict["step"]
        osc_dict["counter"] %= self.table_size
        return amplitude_value
      
