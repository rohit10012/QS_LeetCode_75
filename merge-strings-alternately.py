def merge_alternately(str1, str2):
    merged = []
    len1, len2 = len(str1), len(str2)
    for i in range(max(len1, len2)):
        if i < len1:
            merged.append(str1[i])
        if i < len2:
            merged.append(str2[i])
    return ''.join(merged)

# Example usage
str1 = "abc"
str2 = "12345"
result = merge_alternately(str1, str2)
print(result)  # Output: a1b2c345
