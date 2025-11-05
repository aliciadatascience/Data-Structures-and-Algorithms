class Solution:
    def romanToInt(self,s):
        sym_num = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0   
        
        for i in range(len(s)):
            if i >0 and sym_num[s[i]] > sym_num[s[i-1]]:
                result += sym_num[s[i]] - 2 * sym_num[s[i-1]]
            else:
                result += sym_num[s[i]]
                
        return result
