import numpy as np
import pandas as pd

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
data = pd.read_html(url)[0]

q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
iqr = q75 - q25
cut_off = iqr * 1.5
minimum, maximum = q25 - cut_off, q75 + cut_off

outliers = [x for x in data if x < minimum or x > maximum]
