# Program takes string and returns the numbers of unique character in it
A = "Guvi Geeks Network Private Limited"
a = ""
for i in A:
    if i not in a:
        a += i
print(len(a))