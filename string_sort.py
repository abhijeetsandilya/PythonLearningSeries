# This code sorts all letters in a sentence alphabetically, based on their ASCII value.
a = str(input("Enter a word: \n"))
b = a.replace(" ", "")
c = list(b)
c.sort()
d = "".join(c)
print(d)
