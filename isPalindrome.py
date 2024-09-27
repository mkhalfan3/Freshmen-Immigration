class Solution(object):
    def isPalindrome(self, x):
        original = x
        if x < 0:
            return False
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        if original == reverse:
            return True
        else:
            return False