def reverse_string(string):
    return string[::-1]

def replace_digits(string, replace_dict):
    for digit, replace_with in replace_dict.items():
        string = string.replace(digit, replace_with)
    return string

input_string = '0401200100483'
# replace_dict = {}
replace_dict = {'0': 'W'}

print('Input string:', input_string)
replaced_string = replace_digits(input_string, replace_dict)
print('Replaced string:', replaced_string)
reversed_string = reverse_string(replaced_string)
print('Reversed string:', reversed_string)