# implement an algorithm to determine if a string has all unique characters
# what if we cannot use additional data structures

def is_unique(str):
    arr = [False] * 128
    for char in str:
         index = ord(char) #ASCII value of the char
         if arr[index]:
             return False
         arr[index] = True

    return True
print(is_unique("mustafa") == False)
print(is_unique("mstfa")) == True
