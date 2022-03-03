import numpy as np


class LUTFactory:
    def __init__(self):
        self.table_size = 2**16 # 65536 values
        self.pi2 = 2 * np.pi

    def get_table_size(self):
        return self.table_size

    def generate_sin_table(self):
        return np.sin(np.linspace(0, self.pi2, self.table_size))

    def generate_cos_table(self):
        return np.cos(np.linspace(0, self.pi2, self.table_size))

    def generate_saw_table(self):
        return np.linspace(-1, 1, self.table_size)

    def generate_tri_table(self):
        ramp = int(self.table_size / 4)
        return np.append(np.linspace(0, 1, ramp + 1)[:-1],
                         np.append(np.linspace(1, -1, ramp * 2),
                                   np.linspace(-1, 0, ramp + 1)[1:]))

    def generate_sqr_table(self):
        return np.append(np.ones(int(self.table_size / 2)), np.ones(int(self.table_size / 2)) * -1)


lutf = LUTFactory()

# Module wide global variables 
table_size = lutf.get_table_size()

sin_lookup = lutf.generate_sin_table()
cos_lookup = lutf.generate_cos_table()
saw_lookup = lutf.generate_saw_table()
tri_lookup = lutf.generate_tri_table()
sqr_lookup = lutf.generate_sqr_table()
