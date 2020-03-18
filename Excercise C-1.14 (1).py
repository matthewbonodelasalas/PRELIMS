# Exercise C-1.14 page 52

def odd_num_product(nums):
  for x in range(len(nums)):
    for y in range(len(nums)):
      if  x != y:
        product = nums[x] * nums[y]
        if product & 1:
          return True
          return False
          
seq1 = [2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20]
seq2 = [1, 6, 4, 7, 8, 11 , 13, 15, 17, 19]
print(seq1, odd_num_product(seq1));
print(seq2, odd_num_product(seq2));
odd1 = list(filter(lambda i: (i % 2 !=0),seq1))
odd2 = list(filter(lambda i: (i % 2 !=0),seq2))
print("Numbers in the 1st sequence whose product is an odd number: ", odd1)
print("Numbers in the 2nd sequence whose product is an odd number: ", odd2)