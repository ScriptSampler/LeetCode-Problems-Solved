#https://leetcode.com/problems/two-sum
#the class that stores the "logic"
class Solution:
#function that has "self" as a way to store data within that class. It is necessary to add "self" to any function within a class. [int] means the whole list contains integers, int  means that the singular value is an integer. -> List[int] is returning a list of integers.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# creating a dictionary to store information so that we dont loop through the same numbers twice
        hashmap = {}
#a for loop, i (indices), n (the element), nums is the numbers in the list, defined in "twoSum" as an argument
#so, for all the indexs of the elements in the list "nums"
#enumerate makes the collection of elements and indexes in one step, where n is the elements in the array and i is the index in the array
        for i, n in enumerate(nums):
#basically saying: current_element + x = target, so, x = target - current_element.
            complement = target - n
# when "complement" (x) is found in the hashmap (stored data from doing target - current)
            if complement in hashmap:
# return the indicies of the 2 values (the current_element and the x)
                return [i, hashmap[complement]]
#store the index value of the element it just checked to the hashmap (the elements of the hashmap = the index of the array)
            hashmap[n] = i
#otherwise return nothing if an empty list is found
        return[]
