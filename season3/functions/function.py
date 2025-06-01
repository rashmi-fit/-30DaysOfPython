# you are given two list of numbers and you need to find the total of iteach of the lists
def total_of_lists(expected_list):

      # total1 = sum(list1)
      # total2 = sum(list2)
      total = 0
      for i in expected_list:
            total = total+i
      return total

list1 =[1,2,3,4,5]
list2 =[6,7,8,9,10]
list1total = total_of_lists(list1)
list2total = total_of_lists(list2)

print(f"Total of list1: {list1total}")
print(f"Total of list2: {list2total}")
