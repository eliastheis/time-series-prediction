import keras
import numpy as np
import csv
from matplotlib import pyplot as plt
from os import path
import argparse

def getArgs():
	parser = argparse.ArgumentParser("main.py -f data.csv -t false")
	parser.add_argument("-f", help="filename of the csv.file", type=str)
	parser.add_argument("-t", help="Does the csv-file starts with column titles? (true/false)", type=bool)
	args = parser.parse_args()
	return args
	#print('file:',args.f)
	#print('title:', args.t)

if __name__ == '__main__':

	# get terminal arguments
	args = getArgs()
	if(path.isfile(args.f)):
		print('t:', args.t)
	else:
		print('file "' + args.f + '" does not exists')
	