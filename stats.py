import pandas as pd
import glob
from scipy.stats import chisquare

#open the csv in bin

path = r'build/bin'
all_files = glob.glob(path + "/*.csv")

list = []
for filename in all_files:
    df = pd.read_csv(filename)
    list.append(df)
print(len(list))
