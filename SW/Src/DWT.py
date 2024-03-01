
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import pywt
import pandas as pd
def calculate_snr(signal, noise):
    power_signal = np.mean(np.abs(signal)**2)
    power_noise = np.mean(np.abs(noise)**2)
    return 10 * np.log10(power_signal / power_noise)
# Load your data here
data = pd.read_csv(r'D:\HCMUT\huy\PJ2\New folder\7_1_2.csv')
data = data.iloc[:, 0].values  # select the first column and get its values
t = np.linspace(0, len(data)*0.005, len(data))
# Decompose the signal using a wavelet transform
coeffs = pywt.wavedec(data, 'db4', level=3)
# Set the detail coefficients at the last two levels to zero
coeffs[-1] = np.zeros_like(coeffs[-1])
coeffs[-2] = np.zeros_like(coeffs[-2])
coeffs[-3] = np.zeros_like(coeffs[-3])
# Apply the inverse DWT to get the filtered signal
filtered_signal = pywt.waverec(coeffs, 'db4')
filtered_signal = scipy.signal.medfilt(filtered_signal.squeeze(), kernel_size=3)

# Apply a median filter


# Find all peaks in the filtered signal
peaks, _ = scipy.signal.find_peaks(filtered_signal,distance=20)

# Calculate the prominence of each peak
prominences = scipy.signal.peak_prominences(filtered_signal, peaks)[0]

# Set a threshold for the minimum prominence
prominence_threshold = 1.0  # adjust this value as needed
# Only keep peaks with prominences above the threshold
peaks = peaks[prominences > prominence_threshold]

# Initialize an empty list to store the heart rates
heart_rates = []

# Loop over the peaks array
for i in range(1, len(peaks)):
    # Calculate the difference in time between the current peak and the previous peak
    dt = t[peaks[i]] - t[peaks[i-1]]
    # Calculate the heart rate and append it to the heart_rates list
    heart_rate = 60 / dt
    heart_rates.append(heart_rate)
# print(round(np.mean(heart_rates[1:])))
print(f"Heart rate : {round(np.mean(heart_rates[1:]))} bpm")
print(60/(t[peaks[10]]-t[peaks[9]]))
# Print the heart rates
# for i, heart_rate in enumerate(heart_rates):
#     print(f"Heart rate {i+1}: {round(heart_rate)} bpm")
noise = data - filtered_signal[:-1]
snr = calculate_snr(data, noise[:-1])
print(f"SNR: {snr} dB")
# Plot the original and filtered signals
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(t, data, 'b-', label='original data')
plt.title('Original Data')
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal[:-1], 'r-', label='filtered data')
plt.title('Filtered Data')
# Plot the peaks
plt.scatter(t[peaks], filtered_signal[peaks], color='blue')

plt.legend()
plt.show()