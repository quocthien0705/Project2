import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal 
import lib as lib
from scipy.signal import freqz
# Sampling rate of your data
fs = 300  # replace with your actual sampling rate

# Desired cutoff frequency
fc = 49 # replace with your desired cutoff frequency

# Nyquist frequency
nyquist = fs / 2.0

# Calculate Wn
wn = fc / nyquist
data = pd.read_csv(r'D:\HCMUT\huy\PJ2\New folder\7_1_2.csv')
t=np.linspace(0, len(data)*0.006, len(data))
fc_low = 0.09  # replace with your desired low cutoff frequency
fc_high = 60  # replace with your desired high cutoff frequency

# Calculate Wn for bandpass filter
wn_low = fc_low / nyquist
wn_high = fc_high / nyquist

# Design bandpass filter
b_band, a_band = scipy.signal.butter(5, [wn_low, wn_high], 'band', analog=False)

# Apply bandpass filter
filtered_signal_band = scipy.signal.filtfilt(b_band, a_band, data.squeeze(), axis=0)
filtered_signal_median = scipy.signal.medfilt(filtered_signal_band.squeeze(), kernel_size=3)
w, h = freqz(b_band, a_band, worN=8000)

# Convert gain to decibels
h_db = 20 * np.log10(abs(h))

# Create the plot
# plt.figure(2)
plt.plot(0.5*fs*w/np.pi, h_db, 'b')
plt.title('Bandpass Filter Frequency Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()
# Plot the original and filtered signals
#plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(t, data, 'b-', label='original data')
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal_median, 'r-', label='filtered data')
plt.legend()
plt.show()