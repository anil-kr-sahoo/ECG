import pandas as pd
import numpy as np
import heart_rate_functions as l2f

column_names =[
    "ecg",
    "t"
]

restingecg = pd.read_csv("heart_rate_data.txt",
                         names=column_names, sep=',', skiprows=5000, skipfooter=5000)

restingecg.t = restingecg.t/1000

d_ecg, peaks_d_ecg = l2f.decg_peaks(restingecg.ecg, restingecg.t)
Remove_peaks_d_ecg = l2f.d_ecg_peaks(d_ecg, restingecg.t, 0.4, 0.5)
restingecg_remove_t = l2f.Rwave_peaks(restingecg.ecg, d_ecg, Remove_peaks_d_ecg, restingecg.t)
RR_interval = np.diff(restingecg_remove_t)
heartrate = (1/RR_interval)*60
