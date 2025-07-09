# 1. Rotate a list to the left by k positions
def rotate_left(lst, k):
    return lst[k:] + lst[:k]

print("1. Rotate Left:")
lst1 = [1, 2, 3, 4, 5]
k = 2
print("Input:", lst1, "| k =", k)
print("Output:", rotate_left(lst1, k))
print()



# 2. Find the second largest number in a list
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

print("2. Second Largest:")
lst2 = [5, 1, 9, 6, 9]
print("Input:", lst2)
print("Output:", second_largest(lst2))
print()



# 3. Remove all even numbers from a list
def remove_even(lst):
    return [x for x in lst if x % 2 != 0]

print("3. Remove Even:")
lst3 = [1, 2, 3, 4, 5, 6]
print("Input:", lst3)
print("Output:", remove_even(lst3))
print()



# 4. Remove all vowels from a string
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in text if char not in vowels])

print("4. Remove Vowels:")
text4 = "Hello World"
print("Input:", text4)
print("Output:", remove_vowels(text4))
print()



# 5. Count the number of words in a sentence
def count_words(sentence):
    return len(sentence.split())

print("5. Count Words:")
text5 = "This is a test sentence."
print("Input:", text5)
print("Output:", count_words(text5))
print()



# 6. Find the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print("6. Longest Word:")
text6 = "Python is awesome"
print("Input:", text6)
print("Output:", longest_word(text6))
print()



# 7. Check if two strings are anagrams
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print("7. Anagram Check:")
a = "listen"
b = "silent"
print("Input:", a, "and", b)
print("Output:", is_anagram(a, b))
print()



# 8. Replace spaces with underscores
def replace_spaces(text):
    return text.replace(' ', '_')

print("8. Replace Spaces:")
text8 = "Hello World Again"
print("Input:", text8)
print("Output:", replace_spaces(text8))
print()



# 9. Multiply all numbers in a tuple
def multiply_tuple(tup):
    result = 1
    for num in tup:
        result *= num
    return result

print("9. Multiply Tuple:")
tup9 = (2, 3, 4)
print("Input:", tup9)
print("Output:", multiply_tuple(tup9))
print()



# 10. Return max and min from a tuple
def max_min_tuple(tup):
    return max(tup), min(tup)

print("10. Max and Min from Tuple:")
tup10 = (2, 7, 4, 1)
print("Input:", tup10)
print("Output:", max_min_tuple(tup10))
print()



# 11. Find repeated items in a tuple
def repeated_items(tup):
    return list(set([x for x in tup if tup.count(x) > 1]))

print("11. Repeated Items:")
tup11 = (1, 2, 3, 2, 4, 1)
print("Input:", tup11)
print("Output:", repeated_items(tup11))
print()



# 12. Find key with maximum value in a dictionary
def key_with_max_value(d):
    return max(d, key=d.get)

print("12. Key with Max Value:")
dict12 = {'a': 10, 'b': 25, 'c': 20}
print("Input:", dict12)
print("Output:", key_with_max_value(dict12))
print()



# 13. Filter dictionary items based on value
def filter_dict(d, threshold):
    return {k: v for k, v in d.items() if v >= threshold}

print("13. Filter Dictionary:")
dict13 = {'a': 10, 'b': 5, 'c': 20}
threshold = 10
print("Input:", dict13, "| Threshold:", threshold)
print("Output:", filter_dict(dict13, threshold))
print()
