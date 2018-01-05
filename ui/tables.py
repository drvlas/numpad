# -*- coding: utf-8 -*-
"""
Tables, constants
"""
MAX_DIG = 9
MAX_VAL = 999999999     # 9 nines

point10Power = {
            -1:('{: 011d}', 1, 1),
            0: ('{: 011d}.', 1, 1),
            1: ('{: 011.1f}', 10, 0.1),
            2: ('{: 011.2f}', 100, 0.01),
            3: ('{: 011.3f}', 1000, 0.001),
            4: ('{: 011.4f}', 10000, 0.0001),
            5: ('{: 011.5f}', 100000, 0.00001),
            6: ('{: 011.6f}', 1000000, 0.000001),
            7: ('{: 011.7f}', 10000000, 0.0000001),
            8: ('{: 011.8f}', 100000000, 0.00000001),
            9: ('{: 011.9f}', 1000000000, 0.000000001),
        }
FORMAT_POS = 0
LEFT_SHIFT = 1
RIGHT_SHIFT = 2
#Use samples:
#point10Power[self.point][FORMAT_POS]
#point10Power[self.point][LEFT_SHIFT]
#point10Power[self.point][RIGHT_SHIFT]

# NumPad result index
VALID = 0
VAL = 1
PNT = 2
SGN = 3

