import numpy as np
import matplotlib as plt
import pandas as pd

data_sargent_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87793/Sargent_RawDataOnly.txt?sequence=1&isAllowed=y'
data_nueces_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87766/NuecesBay_RawDataOnly.txt?sequence=2&isAllowed=y'
data_sargent = np.loadtxt(data_sargent_url,  dtype=str, delimiter=',')
data_nueces = np.loadtxt(data_nueces_url,  dtype=str, delimiter=',')

