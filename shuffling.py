import csv
import numpy as np
shortlisted = []

with open('Final Shortlisted.csv','r') as pool:
	csv_pool = csv.reader(pool)
	for row in csv_pool:
		shortlisted.append(row)

shortlisted = np.array(shortlisted)

np.random.shuffle(shortlisted)

filename = "Final_pool.csv"

with open(filename,'w') as pool:
	csvwriter = csv.writer(pool)
	csvwriter.writerows(shortlisted)