class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(str)
        if n==0: 
            return ""
        if n ==1:
            return str[0]

        #find the minimum str from 0 to n-1 sort

        str.sort()
        #the shortest string will be the last one str[n-1]

        end = str[n-1]

        i=0

        while i<len(end) and end[i]==str[0][i]:
            i+=1

         
