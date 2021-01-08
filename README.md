# ECG

- Creating ECG wave form with Python
- Having a 333K+ data 
- Filtering Noice from ECG signals2_compair_row_filter
- Compair ECG waveform with stabble ECG waveform
- Stable ECG waveform
- Choosing positive peaks
- Creating all combination of heartrate wave form

Steps to run
- Create a virtualenv (preferable python3.6+)
- pip install -r requirements.txt
- Route to the ECG_codebase
- run 1_raw_data.py (Get the actual ECG from data with noise)
- run 2_compair_row_filter.py (Get compairision between actual wave form and Stable wave form)
- run 3_filtered_data.py (Get Stable wave form)
- run 4_peak_filtered_data.py (Get Peaks from the wave form)
- run 5_heart_rate.py (Get all combination of heart rate in wave form)
