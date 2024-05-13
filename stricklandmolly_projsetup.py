''' This module provides functions for creating a series of project folders. '''

import math
import statistics
import pathlib
import random
import time
import os

import pip
import datafun_01_utils




#Create folders for a range of numbers.
def create_folders_for_range(start_year, end_year):

    for year in range(start_year, end_year+1):
        folder_names= str(year)
        pathlib.Path(folder_names).mkdir(exist_ok=True)

#Create folders from a list of names
def create_folders_from_list(folder_list):
  
    for folder_names in folder_list:
        pathlib.Path(folder_names).mkdir(exist_ok=True)

#create folders from a list with prefix data
def create_prefixed_folders(folder_list, prefix):
    for folder_names in folder_list:
        pathlib.Path(f"{prefix}-{folder_names}").mkdir(exist_ok=True)


# create a folder periodically: one folder every 30 minutes
def create_folders_periodically(duration):
    start_time=time.time()
    folder_count=0
    while time.time() - start_time < duration * 60:  # Convert duration to seconds
        folder_count += 1
        folder_name = f"Folder_{folder_count}"
        os.makedirs(folder_name)
        time.sleep(30 * 60)  # Wait for 30 minutes before creating the next folder
    pass
    
    
    
# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {datafun_01_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)


    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)


if __name__ == '__main__':
    main()
