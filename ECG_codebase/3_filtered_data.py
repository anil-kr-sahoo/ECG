import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal

column_names =[
    "ecg",
    "t"
]

restingecg = pd.read_csv("ecg_data.txt",
                         names=column_names, sep='\t', skiprows=5000, skipfooter=5000)

restingecg.t = restingecg.t/1000

Wn= 0.1
b, a = scipy.signal.butter(4, Wn, "low", analog=False)
filt_resingecg = scipy.signal.filtfilt(b,a,restingecg.ecg)

plt.plot(restingecg.t, filt_resingecg)
plt.show()
