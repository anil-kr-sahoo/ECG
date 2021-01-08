import pandas as pd
import matplotlib.pyplot as plt

column_names =[
    "ecg",
    "t"
]

restingecg = pd.read_csv("ecg_data.txt",
                         names=column_names, sep='\t', skiprows=5000, skipfooter=5000)

restingecg.t = restingecg.t/1000        # Converting miliseconds to seconds

plt.plot(restingecg.t, restingecg.ecg)
plt.show()