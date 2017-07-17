#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import statistics

name = input('Enter your name: ')
print('My name is', name)

exList = [34, 43, 81, 106, 106, 115]
print('Mean for',exList,'is',statistics.mean(exList)) 
print('Mode for',exList,'is',statistics.mode(exList)) 

exList2 = [44,50,38,96,42,47, 40,39,46,50, 'abc']

'''
https://www.ltcconline.net/greenl/courses/201/descstat/mean.htm

Variance and Standard Deviation: Step by Step

1. Calculate the mean, x. 

2. Write a table that subtracts the mean from each observed value.

3. Square each of the differences.

4. Add this column.

5. Divide by n -1 where n is the number of items in the sample  This is the variance.

6. To get the standard deviation we take the square root of the variance.  

'''        

print('Mean for',exList2,'is',statistics.mean(exList2)) 
print('Median for',exList2,'is',statistics.median(exList2)) 
print('Variance for',exList2,'is',statistics.variance(exList2)) 
print('Standard Deviation for',exList2,'is',statistics.stdev(exList2)) 

print(dir(statistics))
print(statistics.median.__annotations__)