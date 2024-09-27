class Solution(object):
    def reverseString(self, s):
        last = len(s) - 1
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[last]
            s[last] = temp
            last = last - 1