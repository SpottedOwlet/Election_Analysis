# Import the datetime class from the datetime Module
#import datetime
# Use the now() attribute on the datetime class to get the present time
#now = datetime.datetime.now()
# print the present time
#print("the time right now is ", now)

# Read data from a file

# Assign a variable for the file to load and the path for the file

#file_to_load = '/Users/kedarmarathe/Desktop/Coursework/UCB_BootCamp/Module 3/GitHub/Election_Analysis/Resources/election_results.csv'
# print the file object
    #print(election_data)
# close the file
#election_data.close()

# Add dependencies
import csv
import os
from typing import Text

#file_to_load = os.path.join("Resources","election_results.csv")


# Using the open() function with the "r" mode we will read data to the file.
#election_data = open(file_to_load,'r')

# Open the election results and read the file
#with open(file_to_load) as election_data:

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save,"w")
# write some data into the file
outfile.write("Hello World!")
#close the file
outfile.close()

#cleaner code
# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
# using the with statement open the file as a text file
with open(file_to_save,"w") as txt_file:
    # write some data to the file
    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------")
    # write three counties to the file
    txt_file.write("\nVentura")
    txt_file.write("\nOrange County")
    txt_file.write("\nMariposa")

# Read the election results:
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    # Read the file object woth the reader function
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file
    #for row in file_reader:
        #print(row[0])
    # Print the header row
    headers = next(file_reader)
    print(headers)