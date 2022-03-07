import numpy as np
from enum import Enum
from audloop.common import *
from audloop.lookup_tables import sin_lookup, saw_lookup, sqr_lookup, tri_lookup, cos_lookup

sin_osc_lookup = {}
cos_osc_lookup = {}
sqr_osc_lookup = {}
saw_osc_lookup = {}
tri_osc_lookup = {}


class OscType(Enum):
    SIN = 1
    COS = 2
    SAW = 3
    SQR = 4
    TRI = 5


def sinosc(frequency, osc_id) -> float:
    """
    Sin Oscillator function

    Note:
        Oscillator functions aim to simplify oscillator usage. Rather than instantiating individual oscillator
        objects, multiple concurrent oscillators can be utilized from the same function call. For these functions,
        the oscillator ID is used to specify individual oscillators.

    :param frequency: frequency (hz)
    :param osc_id: Unique oscillator ID
    :return: oscillator amplitude value
    """
    return _osc(frequency, osc_id, sin_osc_lookup, OscType.SIN)


def cososc(frequency, osc_id) -> float:
    """
    Cos Oscillator function

    Note:
        Oscillator functions aim to simplify oscillator usage. Rather than instantiating individual oscillator
        objects, multiple concurrent oscillators can be utilized from the same function call. For these functions,
        the oscillator ID is used to specify individual oscillators.

    :param frequency: frequency (hz)
    :param osc_id: Unique oscillator ID
    :return: oscillator amplitude value
    """
    return _osc(frequency, osc_id, cos_osc_lookup, OscType.COS)


def sqrosc(frequency, osc_id) -> float:
    """
    Square Wave Oscillator function

    Note:
        Oscillator functions aim to simplify oscillator usage. Rather than instantiating individual oscillator
        objects, multiple concurrent oscillators can be utilized from the same function call. For these functions,
        the oscillator ID is used to specify individual oscillators.

    :param frequency: frequency (hz)
    :param osc_id: Unique oscillator ID
    :return: oscillator amplitude value
    """
    return _osc(frequency, osc_id, sqr_osc_lookup, OscType.SQR)


def sawosc(frequency, osc_id) -> float:
    """
    Saw Wave Oscillator function

    Note:
        Oscillator functions aim to simplify oscillator usage. Rather than instantiating individual oscillator
        objects, multiple concurrent oscillators can be utilized from the same function call. For these functions,
        the oscillator ID is used to specify individual oscillators.

    :param frequency: frequency (hz)
    :param osc_id: Unique oscillator ID
    :return: oscillator amplitude value
    """
    return _osc(frequency, osc_id, saw_osc_lookup, OscType.SAW)


def triosc(frequency, osc_id) -> float:
    """
    Triangle Wave Oscillator function

    Note:
        Oscillator functions aim to simplify oscillator usage. Rather than instantiating individual oscillator
        objects, multiple concurrent oscillators can be utilized from the same function call. For these functions,
        the oscillator ID is used to specify individual oscillators.

    :param frequency: frequency (hz)
    :param osc_id: Unique oscillator ID
    :return: oscillator amplitude value
    """
    return _osc(frequency, osc_id, tri_osc_lookup, OscType.TRI)


def _osc(frequency, osc_id, osc_lookup: dict, osc_type: OscType):
    """
    Generic implementation of an oscillator function

    :param frequency:
    :param osc_id:
    :param osc_lookup:
    :param osc_type:
    :return:
    """
    if osc_id not in osc_lookup:
        osc_lookup[osc_id] = OscFactory.create_oscillator(osc_type)
    return osc_lookup[osc_id].osc(frequency)


class Osc:
    def __init__(self, lut: np.ndarray, fs=SAMPLE_RATE_DEFAULT):
        """
        Basic Lookup Table Oscillator

        :param lut: lookup table to read from
        :param fs: the sample rate
        """
        self._fs = fs
        self._lut = lut
        self._table_size = self._lut.size
        self._frequency = 0
        self._step = 0
        self._counter = 0

    def osc(self, frequency) -> float:
        """
        Oscillator

        :param frequency: frequency
        :return: wave amplitude value
        """
        if self._frequency != frequency:
            self._update_lut_step(frequency)
        amplitude_value = self._lut[self._counter]
        self._increment_counter()
        return amplitude_value

    def _increment_counter(self):
        """
        Increment the counter used to read from the lookup table
        """
        self._counter = (self._counter + self._step) % self._table_size

    def _update_lut_step(self, frequency):
        """
        Update the lookup table step value. This only need to be called when the frequency changes

        :param frequency: new frequency value
        """
        self._frequency = frequency
        self._step = (self._table_size * frequency) / self._fs
        if self._step % int(self._step) >= 0.5:
            self._step = int(np.ceil(self._step))
        else:
            self._step = int(np.floor(self._step))

    @property
    def sample_rate(self):
        """
        :return: the sample rate of this oscillator
        """
        return self._fs

    @property
    def frequency(self):
        """
        :return: the current frequency
        """
        return self._frequency


class Sinosc(Osc):
    def __init__(self, fs=SAMPLE_RATE_DEFAULT):
        """
        Cos Oscillator
        """
        super().__init__(sin_lookup, fs)

    def sinosc(self, frequency):
        """
        Sin Oscillator

        :param frequency: frequency
        :return: wave amplitude value
        """
        return self.osc(frequency)


class Cososc(Osc):
    def __init__(self, fs=SAMPLE_RATE_DEFAULT):
        """
        Cos Oscillator
        """
        super().__init__(cos_lookup, fs)

    def cososc(self, frequency):
        """
        Cos Oscillator

        :param frequency: frequency
        :return: wave amplitude value
        """
        return self.osc(frequency)


class Sawosc(Osc):
    def __init__(self, fs=SAMPLE_RATE_DEFAULT):
        """
        Saw Wave Oscillator
        """
        super().__init__(saw_lookup, fs)

    def sawosc(self, frequency):
        """
        Saw Wave Oscillator

        :param frequency: frequency
        :return: wave amplitude value
        """
        return self.osc(frequency)


class Sqrosc(Osc):
    def __init__(self, fs=SAMPLE_RATE_DEFAULT):
        """
        Square Wave Oscillator
        """
        super().__init__(sqr_lookup, fs)

    def sqrosc(self, frequency):
        """
        Square Wave Oscillator

        :param frequency: frequency
        :return: wave amplitude value
        """
        return self.osc(frequency)


class Triosc(Osc):
    def __init__(self, fs=SAMPLE_RATE_DEFAULT):
        """
       Triangle Wave Oscillator
       """
        super().__init__(tri_lookup, fs)

    def triosc(self, frequency):
        """
        Triangle Wave Oscillator

        :param frequency: frequency
        :return: wave amplitude value
        """
        return self.osc(frequency)


class OscFactory:
    @staticmethod
    def create_oscillator(osc_type: OscType) -> Osc:
        """
        Create an oscillator instance

        :param osc_type: the oscillator type
        :return: oscillator instance
        """
        case_matcher = {
            OscType.SIN: lambda: Sinosc(),
            OscType.COS: lambda: Cososc(),
            OscType.SQR: lambda: Sqrosc(),
            OscType.SAW: lambda: Sawosc(),
            OscType.TRI: lambda: Triosc()
        }
        return case_matcher[osc_type]()
