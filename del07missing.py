""""Matthew Bono I. De las Alas
    DATALOG Lab07
    MAR. 18, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

def binary_missing(array,low,high): #defines the function to find the missing element in the set of data
  if low > high:
     return high + 1 #returns the high value + 1
  if (low != array[low]): #if not equal to the set of data
      return low;#returns the low value
  middle_value = int((low + high) / 2)  # determines the middle value of the set of data
  if (data_set[middle_value]==middle_value):#defines the set of data from lowest to the middle value
      return binary_missing(array,middle_value + 1,high)#returns the missing value in the data set
  return binary_missing(array,low,middle_value)

#main program
data_set = [0, 1, 5, 7, 5, 5, 8, 7, 11] # set of data
a = len(data_set)#returns the number of items in the given set
print(data_set)#prints the given set of data
print("The smallest missing element is", binary_missing(data_set, 0, a - 1)) #prints the missing value in the set of data provided

data_set = [1, 2, 3, 4, 6, 11, 17]# set of data
b = len(data_set)#returns the number of items in the given set
print(data_set)#prints the given set of data
print("The smallest missing element is", binary_missing(data_set, 0, b - 1)) #prints the missing value in the set of data provided

data_set = [0, 1, 2, 3, 4, 5, 6, 7, 8]# set of data
c = len(data_set)#returns the number of items in the given set
print(data_set)#prints the given set of data
print("The smallest missing element is", binary_missing(data_set, 0, c - 1)) #prints the missing value in the set of data provided