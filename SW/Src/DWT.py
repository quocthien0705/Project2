import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal 
import lib as lib

# Sampling rate of your data
# fs = 200  # replace with your actual sampling rate

# # Desired cutoff frequency
# fc = 45  # replace with your desired cutoff frequency

# # Nyquist frequency
# nyquist = fs / 2.0

# # Calculate Wn
# wn = fc / nyquist
# data = pd.read_csv(r'D:\HCMUT\huy\PJ2\New folder\j.csv')
# t=np.linspace(0, len(data)*0.005, len(data))
# print(t)
# b, a =scipy.signal.butter(4, wn, 'low', analog=False)
# filter = scipy.signal.filtfilt(b, a, data.squeeze(), axis=0)
# wn_high = 0.66/(200/2)
# b_high, a_high = scipy.signal.butter(4, wn_high, 'high', analog=False)
# # Apply high pass filter
# filter_high = scipy.signal.filtfilt(b_high, a_high, filter.squeeze(), axis=0)
# plt.figure(1)
# plt.plot(t, data, 'b-', label='data')
# plt.figure(2)
# plt.plot(t, filter, 'r-', linewidth=2, label='filter')
# #peaks, _ = scipy.signal.find_peaks(data.squeeze(), height=0)
# # Adjust the height and add a distance parameter
# peaks, _ = scipy.signal.find_peaks(filter.squeeze(), height=2.7, distance=50)
# data_series = filter.squeeze()
# k=60/(t[peaks[20]]-t[peaks[19]])
# print(round(k))
# plt.plot(t[peaks], data_series[peaks], 'x')
# plt.show()
import pywt

# Load your ECG data
data = pd.read_csv(r'D:\HCMUT\huy\PJ2\New folder\j.csv')

coeffs = pywt.wavedec(data.values.squeeze(), 'db4', level=8)

# Set the detail coefficients at the last two levels to zero

coeffs[-1] *= 0.5
coeffs[-2] *= 0.5
#coeffs[-3] = np.zeros_like(coeffs[-3])
# Apply the inverse DWT to get the filtered signal
filtered_signal = pywt.waverec(coeffs, 'db4')
# Plot the original and filtered signals
t = np.linspace(0, len(data)*0.005, len(data))
# Trim filtered_signal to the same length as t
filtered_signal = filtered_signal[:len(t)]
peaks, _ = scipy.signal.find_peaks(filtered_signal, height=2.2, distance=50)
k = 60 / (t[peaks[10]] - t[peaks[9]])
print(round(k))
filtered_signal_median = scipy.signal.medfilt(filtered_signal.squeeze(), kernel_size=3)

# Plot the original and filtered signals
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(t, data, 'b-', label='original data')
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal_median, 'r-', label='filtered data')
plt.legend()
plt.show()