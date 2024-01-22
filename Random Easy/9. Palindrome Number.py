#want to know if the number is a palindrome
class Solution(object):
    def isPalindrome(self, x):
       x_str =str(x)
       if x_str == x_str[::-1]:
           return True
           