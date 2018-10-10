# corresponds to code for biocomputing exercise 6
"""
Created on Fri Oct  5 10:28:05 2018

@author: Cole
"""

# part 1:
# Write python code that replicates functionality of Unix "head" function
# should define a variable with the file to return lines from
# and should define a variable representing the number of lines to be returned from the top of the indicated file
# selected file content should be printed to terminal in python


print('Part 1')
print(' ')
# Define the variable to choose files from (ex, wages.csv)
import pandas as pd

def head(filename,headlines):
    data=pd.read_csv(filename, header=0, sep=',')
    x=data.head(headlines)
    print(x)
    return x

filename='wages.csv' # this can be set to any filename with a csv format in the current working directory

#define the number of lines to include in the header
headlines=8 # this can be set to any positive integer value


head(filename,headlines) # different filenames or headline counts could be inputted directly here

print(' ')
print(' ')



# part 2: Using pandas, Load the data contained in the provided 'iris.csv'
# write python code to do the following:
# a) print the last 2 rows in the last two columns to the python terminal (take care with indexing)
# b) get the number of observations for each species included in the data set
# c) get rows wiith Sepal.Width > 3.5
# d) write the data for the species 'setosa' to a comma-delimited file named 'setosa.csv'
# e) calculate thee mean, minimum, and maximum of Petal.Length for observations from 'virginica'
print('Part 2')

# read in data from iris.csv
irisdata=pd.read_csv('iris.csv', header=0, sep=',')

print('Part 2a')
# a) print the last 2 rows in the last two columns to the python terminal (take care with indexing)
print(irisdata.iloc[148:150,3:5])
print(' ')

print('Part 2b')
# b) get the number of observations for each species included in the data set
species_count=irisdata.Species.unique().size # get the unique species count
species_uniq_names=irisdata.Species.unique() # get the names of the unique species

for i in range(0,species_count): # go through all of the species
    species=species_uniq_names[i] # pick out the species name
    species_list=irisdata[irisdata.Species==species] # give all of the data for that species
    print('Number of observations of ',species) # allows for easily understood output
    print(species_list.Species.size) # count the number of instances of the current species
    

print(' ')
print

# c) get rows wiith Sepal.Width > 3.5
enoughwidth=irisdata['Sepal.Width'][irisdata['Sepal.Width']>3.5] # save rows where width is sufficient and save
print('Number of instances with Sepal Width >3.5',enoughwidth.size)
    
# d) write the data for the species 'setosa' to a comma-delimited file named 'setosa.csv'
setosa_data=irisdata[irisdata.Species=='setosa']

save_data=setosa_data.to_csv() # picks out data to be saved
alt_save=open('setosa.csv','w') # opens a blank csv
alt_save.write(save_data) # writes the dato to the open empty
alt_save.close() # closes
    
print(' ')

print('Part e')

# e) calculate thee mean, minimum, and maximum of Petal.Length for observations from 'virginica'
virginica_length=irisdata['Petal.Length'][irisdata['Species']=='virginica'] # save the length data
print('Virginica Minimum Petal Length',min(virginica_length)) # take min of columnn
print('Virginica Maximum Petal Length',max(virginica_length)) # take max of column
print('Virginica Mean Petal Length',irisdata['Petal.Length'][irisdata['Species']=='virginica'].mean()) # mean function doesnt exist except in data frames








