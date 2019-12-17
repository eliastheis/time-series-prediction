# Time Series Prediction (Not finished)
Simple project for time series prediction with keras

In this small project I tried to develop a python script to predict universal time series data.
My programm reads the data from an csv file and choose every numerical value as input for the nerual network.
For the prediction itself, I used the high-level API keras based on Tensorflow, developed by google.

## Dependencies
* keras
* numpy
* csv
* matplotlib

You can install all dependencies via pip like this:
```
pip install keras
```

## Usage
Start the main.py from the terminal and pass in the csv.file:
```
main.py -f data.csv -t true
```
Arguments:
* -f : filename
* -t : wheter the csv-file starts with column titles

## Example
As an example I use the Shampoo Sales Dataset. You can download it [here](https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv).
![Image of the dataset](dataset.png)