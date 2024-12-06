#Statistics library contains built in median function to
#calculate the median of the list

import statistics

str_value = "Hi, Welcome!"
print("Length of string: ",len(str_value))

sample_list = [12,34,21,89,10,4]
print("Min value in sample_list is: ",min(sample_list))
print("Max value in sample_list is: ",max(sample_list))
print("sum of values in sample_list is: ",sum(sample_list))

print("Median of the list: ", statistics.median(sample_list))