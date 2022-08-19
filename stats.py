import csv
import glob
from scipy.stats import chisquare

path = r'build/bin'
all_files = glob.glob(path + "/*.csv")

buckets = 10
freq = [None] * buckets
file_counter = 0

for filename in all_files:
    print(file_counter)
    file_counter += 1
    reader = csv.reader(filename)
    data = list(reader)
    seq_len = data[0]
    for pos in range(1, len(data)):
        freq[pos * 10 / seq_len] += 1

print(freq)
