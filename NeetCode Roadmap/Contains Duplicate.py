#https://leetcode.com/problems/contains-duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #creating a hashset
        hashset = set()

        #for loop checking every single index value within the list
        for n in nums:
            #checking if index value (n) already exists within the hashset
            if n in hashset:
                return True
            #adding the index value to the hashset (first value will not be checked as the hashset will be empty)
            hashset.add(n)
        #if not found
        return False