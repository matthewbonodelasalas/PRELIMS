#C-1.15

def distinct_numbers(num):
    if len(num) == len(set(num)):
        return True
    else:
        return False
print([1,5,6,7,9,11,12,15])
print("Distinct?: ",distinct_numbers([1,5,6,7,9,11,12,15]))
print([1,1,2,2,3,3,4,4,5,5])
print("Distinct?: ",distinct_numbers([1,1,2,2,3,3,4,4,5,5]))