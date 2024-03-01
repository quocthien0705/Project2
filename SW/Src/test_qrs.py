# import QRS_util as QRS_test
from biosppy import storage
from biosppy.signals import ecg
import numpy as np
import matplotlib.pyplot as plt
fs=360
# load raw ECG signal
signal, mdata = storage.load_txt(r'D:\HCMUT\huy\PJ2\New folder\7_1_2.csv')

# process it and plot
out = ecg.ecg(signal=signal, sampling_rate=1/0.006, show=True,interactive=False)
#   print(out)

# R_peaks, S_pint, Q_point=QRS_test.EKG_QRS_detect(filtered_signal, fs, True, False)
#print(R_peaks)

