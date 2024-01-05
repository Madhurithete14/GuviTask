# Program that takes string and return a new string with all the vowels removed
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result


input_string = "Guvi Geeks Network Private Limited"
output_string = remove_vowels(input_string)
print(output_string)  