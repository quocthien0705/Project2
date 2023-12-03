import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal 
import lib as lib

# Sampling rate of your data
fs = 200  # replace with your actual sampling rate

# Desired cutoff frequency
fc = 60  # replace with your desired cutoff frequency

# Nyquist frequency
nyquist = fs / 2.0

# Calculate Wn
wn = fc / nyquist
data = pd.read_csv(r'D:\HCMUT\huy\PJ2\filter\test.csv')
t=np.linspace(0, len(data)/200, len(data))
print(len(data))
b, a =scipy.signal.butter(5, wn, 'low', analog=False)
print(b)
print(a)
filter = scipy.signal.filtfilt(b, a, data.squeeze(), axis=0)
plt.figure(1)
plt.plot(t, data, 'b-', label='data')
plt.figure(2)
plt.plot(t, filter, 'r-', linewidth=2, label='filter')
#peaks, _ = scipy.signal.find_peaks(data.squeeze(), height=0)
peaks, _ = scipy.signal.find_peaks(filter.squeeze(), height=2.5)
data_series = data.squeeze()
plt.plot(t[peaks], data_series[peaks], 'x')
plt.show()