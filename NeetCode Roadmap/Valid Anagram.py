class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length of both the string are different, then it is obviously not an anagram
        #return false
        if len(s) != len(t):
            return False
        # creating an array contains [0] * 26 for the 26 lower case letters
        count = [0] * 26
        # going through all the letters of the string in s
        for i in range(len(s)):
            #ord('a') has a value of 97
            #ord converts the a ltter from the string into a index (0-25)
            #eg. s = abc
            #ord = 0, 1, 2 (a,b,c slots)
            count[ord(s[i]) - ord('a')] += 1 #adding 1 on that particular index         
            # (currently  0) in the array
            count[ord(t[i]) - ord('a')] -= 1 # doing the opposite for t, subtracting 1 
        
        #checking all the values of the indexes in the array 'count'
        for val in count:
            if val != 0:
                return False #that means all the letters didnt add op to 0, there is a negative or a positive value somehwere
        #return true if all values are 0
        return True



        
        
