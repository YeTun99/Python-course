
def replace(replace_string,replace_character):
    vowel="AEIOUaeiou"
    for i in vowel:
        replace_string=replace_string.replace(i,replace_character)
    return replace_string

string=input("Enter a Word:")
print(replace(string,"$"))