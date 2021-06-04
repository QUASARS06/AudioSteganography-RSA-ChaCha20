import librosa
import matplotlib.pyplot as plt
import math
import numpy as np

signal1, sr1 = librosa.load('./sample.wav')
signal2, sr2 = librosa.load('./sample_embedded.wav')

signal_diff = signal1 - signal2

signal1_sq = signal1**2
signal2_sq = signal2**2

sum_of_sq_of_orig=np.sum(signal1_sq)
sum_of_sq_of_orig_minus_steg=np.sum(signal_diff**2)


# SNR Calculation
snr = 10*np.log10(sum_of_sq_of_orig/(sum_of_sq_of_orig_minus_steg))
print('SNR = ', snr)

# PSNR Calculation
psnr = 10*np.log10(np.max(signal1)**2/(sum_of_sq_of_orig_minus_steg/len(signal1)))
print('PSNR = ', psnr)

# RMSE Calculation
rmse = math.sqrt(sum_of_sq_of_orig_minus_steg/len(signal1))
print('RMSE = ', rmse)

# MAE Calculation
mae = np.sum(signal_diff)/len(signal1)
print('MAE = ', mae)

output = str(snr)+','+str(psnr)+','+str(rmse)+','+str(mae)
with open("analysis_results.txt", "w") as text_file:
    text_file.write(output)