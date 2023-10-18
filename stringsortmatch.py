"""
Problem Statement: Sorting and Dictionary Lookup

You are given a string containing a sequence of characters. Your task is to perform the following operations:

1. Convert the string into an array of characters.
2. Sort the array in ascending order.
3. Create a dictionary where the keys are individual characters from the original array, and the values are the corresponding characters from the sorted array.
4. Given a character as input, find the character associated with it in the dictionary.

Write a Python program that accomplishes these tasks and returns the associated character for the provided key character.

Input:

- The input consists of two lines:
  - The first line contains a string S (1 <= |S| <= 1000), which represents the sequence of characters.
  - The second line contains a single character K (a-z, A-Z), which is the key character to be looked up in the dictionary.

Output:

- If the key character is found in the dictionary, output the associated character.
- If the key character is not found in the dictionary, output "Key not found."

Example:

Input:
"""
hacktoberfest
k
"""

Output:
"""
e
"""

Explanation:

- The input string "hacktoberfest" is converted into an array and sorted to "abceefhkorrstt."
- The dictionary is created as follows: {'h': 'a', 'a': 'b', 'c': 'c', 'k': 'e', 't': 'f', 'o': 'h', 'b': 'k', 'e': 'o', 'r': 'r', 'f': 's', 's': 't'}
- When we input 'k', the associated value is 'e.'

Note:

- The input string may contain uppercase and lowercase letters.
- The dictionary should be case-sensitive.
- Ensure that your program handles cases where the key character is not in the dictionary correctly.
"""


# Take a string input from the user
user_input = input("Enter a string: ")

# Convert the input string to a list and sort it
original_list = list(user_input)
sorted_list = sorted(original_list)

# Create a dictionary with elements of the original list as keys and elements of sorted list as values
result_dict = {original_list[i]: sorted_list[i] for i in range(len(original_list))}

# Take another input from the user (a character to find the associated value)
key_character = input("Enter a character to find the associated value: ")

# Find the associated value in the dictionary
associated_value = result_dict.get(key_character, "Key not found")

# Print the result
print("Dictionary:", result_dict)
print("Associated value for key character '{}': {}".format(key_character, associated_value))


"""
Enter a string: hacktober
Enter a character to find the associated value: t
Dictionary: {'h': 'a', 'a': 'b', 'c': 'c', 'k': 'e', 't': 'h', 'o': 'k', 'b': 'o', 'e': 'r', 'r': 't'}
Associated value for key character 't': h
"""
