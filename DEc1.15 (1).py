"""Matthew Bono I. De las Alas 
   DATALOG Lab02 
   Feb.9,2020 
   I have neither recieved nor provided any help on this lab activity,nor have I concealed any violation of the Honor Code.
"""

def distinct(a): #function to determine if the given set of numbers are distinct
    b = set() #initializing an empty set
    for d in a: #determines if there are unique elements or not
        if d in b: #if there are same elements in the list
          print("Not Distinct",end = "/")#to print in a single line
          return False          
        b.add(d) #adds a given element that is not in the set
    print("Distinct",end = "/") #to print in a single line
    return True

print("Program to determine if given numbers in the set are distinct or not")
print("-------------------------------------------------------------------")
first_set_numbers = [1,1,2,2,3,3,4,4,5,5]
print(first_set_numbers,end=" ") #prints the set of numbers
print(distinct(first_set_numbers)) #determines if the list has distinct numbers
second_set_numbers = [1,2,3,4,5,6,7,8,9,10]
print(second_set_numbers,end = " ") #prints the setof numbers
print(distinct(second_set_numbers)) #determines if the list has distinct numbers