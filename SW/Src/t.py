from biosppy import storage
from biosppy.signals import ecg
import numpy as np
import matplotlib.pyplot as plt

# load raw ECG signal
signal, mdata = storage.load_txt(r'D:\HCMUT\huy\PJ2\New folder\7_1_2.csv')

# process it and plot
out = ecg.ecg(signal=signal, sampling_rate=1/0.006, show=True)
#   print(out)

filtered_signal = out['filtered']
r_peaks = out['rpeaks']
np.savetxt('filtered_signal.csv', filtered_signal, delimiter=',')
plt.subplot(2, 1, 1)
plt.plot(filtered_signal)
plt.subplot(2, 1, 2)
plt.plot(signal)
#plt.plot(r_peaks, filtered_signal[r_peaks], 'ro')
plt.show()
print(filtered_signal)
print(signal)
print(r_peaks)
