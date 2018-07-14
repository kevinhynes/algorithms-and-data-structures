# This program is a linear O(n) solution to determining if two strings are
# anagrams.
from string import ascii_lowercase
def find_anagram(s1, s2):


    s_lists = [s1.lower(), s2.lower()]
    s_dicts = [{}, {}]

    # Create a dictionary for each string. Fill keys with lowercase
    #   a-z and all values initialized to 0. This assumes inputs are 1 word
    #   with no symbols, spaces or special characters.
    for s_dict in s_dicts:
        for c in ascii_lowercase:
            s_dict[c] = 0

    # Iterate through each string, add 1 to the value for the character's key.
    for i in range(len(s_lists)):
        for char in s_lists[i]:
            try:
                s_dicts[i][char] += 1
            except:
                print("Input(s) are invalid.")
                return False

    # If all the values in the each dictionary are the same, input strings
    #   are anagrams!
    if s_dicts[0] == s_dicts[1]:j
        print(True)
        return True
    else:
        print(False)
        return False


find_anagram('kevin', 'nive2K')
