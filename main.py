#import keras
#import numpy as np
import csv
from matplotlib import pyplot as plt
from os import path
import argparse
import numpy as np
from keras import Sequential

# get arguments from console
def getArgs():
	parser = argparse.ArgumentParser("main.py -f data.csv -t false")
	parser.add_argument("-f", help="filename of the csv.file", type=str)
	parser.add_argument("-t", help="wheter the csv-file starts with column titles (true/false)", type=bool)
	return parser.parse_args()

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

# maps the value which is between istart and istop between ostart and ostop
def map(value, istart, istop, ostart, ostop):
	if value == 0 or istart == 0 or istop == 0:
		return 0
	return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

if __name__ == '__main__':

	# get terminal arguments
	args = getArgs()
	if not args.f or not args.t:
		exit('arguments f and t required')
	
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
		exit('file "' + args.f + '" does not exists')
	print(len(data), 'useable lines in "' + args.f + '" found')
	
	# check wheter every row has the same amount of columns
	cols = len(data[0])
	for d in data:
		if len(d) != cols:
			print('csv data is not correct. This line has another amount of data:', d)
			exit(-1)
	print('the data seems correct')
	
	# normalize data
	data = np.array(data)
	min = data.min()
	max = data.max()
	for i in range(len(data)):
		for j in range(len(data[i])):
			data[i][j] = map(data[i][j], min, max, 0, 1)

	# split data into training and testing
	split_index = int(len(data)*0.8)
	training_data = data[:split_index]
	testing_data = data[split_index:]

	# bring data into right shape
	# todo

	# build RNN model
	model = Sequential()
	# todo

	'''
	TODOs:
	* prepare data for training (reshaping)
	* build RNN (recurrent nerual network) from keras ((maybe try different models))
	* train model
	* visualize the result
	'''
	