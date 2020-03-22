# How to read a file
f = open("Mustafa.txt", "rt")
# content = f.read()
# print(content)

f.seek(15)
print(f.readline())
f.close()