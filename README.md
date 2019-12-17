# Time Series Prediction
Simple project for time series prediction with keras

In this small project I tried to develop a python script to predict universal time series data.
My programm reads the data from an csv file and choose every numerical value as input for the nerual network.
For the prediction itself, I used the high-level API keras based on Tensorflow, developed by google.

## Dependencies
* keras
* numpy
You can install all dependencies via pip like this:
```pip
pip install keras
```

## Usage
Start the man.py from the terminal and pass in the csv.file:
```py
main.py mydata.csv
```