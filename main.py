#import keras
#import numpy as np
import csv
from matplotlib import pyplot as plt
from os import path
import argparse

# get arguments from console
def getArgs():
	parser = argparse.ArgumentParser("main.py -f data.csv -t false")
	parser.add_argument("-f", help="filename of the csv.file", type=str)
	parser.add_argument("-t", help="wheter the csv-file starts with column titles (true/false)", type=bool)
	args = parser.parse_args()
	return args

# tries to convert value to float
def toNumerical(val):
	tp = type(val)
	if tp == 'int' or tp == 'float':
		return val
	else:
		try:
			return(float(val))
		except:
			return val

if __name__ == '__main__':

	print('Author:', 'Elias Theis')

	# get terminal arguments
	args = getArgs()
	
	# load csv data
	data = []
	if(path.isfile(args.f)):
		with open(args.f) as file:
			csv_reader = csv.reader(file)
			if args.t:
				print('ignore first line:', next(csv_reader))
			for line in csv_reader:
				# just use numerical values and dont one-hot-encode other types
				numerical_values = []
				for value in line:
					value = toNumerical(value)
					tp = type(value)
					if tp == int or tp == float:
						numerical_values.append(value)
				if len(numerical_values) > 0:
					data.append(numerical_values)
	else:
		print('file "' + args.f + '" does not exists')
	print(len(data), 'useable lines in "' + args.f + '" found')
	
	# check wheter every row has the same amount of columns
	cols = len(data[0])
	for d in data:
		if len(d) != cols:
			print('csv data is not correct. This line has another amount of data:', d)
			exit(-1)
	print('the data seems correct')
	
	plt.plot(data)
	plt.show()
	print(data)
	