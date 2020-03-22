# "Mustafa"
# "Mustaaf" permutation
# "MMustafa" not a permutation
str_1=  "Mustafa"
str_2 = "Mustaaf"

def is_permutation(str_1, str_2):
    str_1 = str_1.replace(" ", "")
    str_2 = str_2.replace(" ", "")

    if len(str_1) != len(str_2):
        return False

    for char in str_1:
        if char in str_2:
            str_2= str_2.replace(char, "")
    return len(str_2) == 0

print(is_permutation(str_1, str_2))