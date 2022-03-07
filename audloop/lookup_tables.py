import numpy as np

PI2 = np.pi * 2
TABLE_SIZE = 2 ** 16  # 65536 values


class LUTFactory:
    @staticmethod
    def generate_sin_table():
        return np.sin(np.linspace(0, PI2, TABLE_SIZE))

    @staticmethod
    def generate_cos_table():
        return np.cos(np.linspace(0, PI2, TABLE_SIZE))

    @staticmethod
    def generate_saw_table():
        return np.linspace(-1, 1, TABLE_SIZE)

    @staticmethod
    def generate_tri_table():
        ramp = int(TABLE_SIZE / 4)
        return np.append(np.linspace(0, 1, ramp + 1)[:-1],
                         np.append(np.linspace(1, -1, ramp * 2),
                                   np.linspace(-1, 0, ramp + 1)[1:]))

    @staticmethod
    def generate_sqr_table():
        return np.append(np.ones(int(TABLE_SIZE / 2)), np.ones(int(TABLE_SIZE / 2)) * -1)


sin_lookup = LUTFactory.generate_sin_table()
cos_lookup = LUTFactory.generate_cos_table()
saw_lookup = LUTFactory.generate_saw_table()
tri_lookup = LUTFactory.generate_tri_table()
sqr_lookup = LUTFactory.generate_sqr_table()
