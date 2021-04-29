# Native deps
import os, sys

# ML/AI Deps used
import pandas as pd
#
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg, optimize
from bs4 import BeautifulSoup as bs


# 0. Some configs etc...

## Environment Configs
DATA_PATH = os.environ.get('DATA_PATH', './data/housing.csv')

## Globals
PROBLEM_SECTION_FORMAT = "\t------ %d ------"

# 1.
print("\n", PROBLEM_SECTION_FORMAT % 1)

## Loading the dataset

try:
    housing_data_frame = pd.read_csv(DATA_PATH)
except pd.errors.ParserError as pe:
    print(str(pe))
    sys.exit(1)
except Exception as e: # anything we missed collect
    print(str(e))      # and work in properly above...
    sys.exit(1)

## Printing the first 5 rows
print("\n Showing first 5 rows of data frame \n")
print(housing_data_frame.head())

## Showing input x and output y
print("\n Showing the Input X and Output Y variables \n")
input_x = housing_data_frame.columns[0:-1]
output_y = housing_data_frame.columns[-1]
print("Inputs X: ", input_x.format())
print("\nOutputs Y: ", output_y)

# 2.
print("\n", PROBLEM_SECTION_FORMAT % 2)

## Shows that total_bedrooms contains null values
print("\n Showing the sum of null values in each column \n")
print(housing_data_frame.isnull().sum())

## Fills null/na values in provided column with the mean of that column
housing_data_frame_mean = housing_data_frame['total_bedrooms'].mean()
print("\n Shows the mean of the total_bedrooms cloumn is %f \n" %\
       housing_data_frame_mean)
housing_data_frame = housing_data_frame.fillna(housing_data_frame_mean)

## Shows null values have been filled for respective columns
print("\n Showing the sum of null values in each column is now all zero \n")
print(housing_data_frame.isnull().sum())

# 3.
print("\n", PROBLEM_SECTION_FORMAT % 3)

print("\n Show unique categorical values for ocean_proximity data variable \n")
print(housing_data_frame['ocean_proximity'].unique())
housing_data_frame['ocean_proximity'] = housing_data_frame['ocean_proximity'].\
                                        astype('category').cat.codes

print("\n Show new encoded numerical values for ocean_proximity data variable \n")
print(housing_data_frame['ocean_proximity'].unique())
print("\n New encoded values in original dataframe \n")
print(housing_data_frame.sample(5))

