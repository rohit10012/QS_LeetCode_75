import math

def gcdOfStrings(str1, str2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def check_divisibility(s, t):
        return s == t * (len(s) // len(t))
    
    gcd_len = gcd(len(str1), len(str2))
    candidate = str1[:gcd_len]
    
    if check_divisibility(str1, candidate) and check_divisibility(str2, candidate):
        return candidate
    return ""

# Example usage:
str1 = "abcabcabc"
str2 = "abc"
print(gcdOfStrings(str1, str2))  # Output: "abc"



