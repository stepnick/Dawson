text = input()

len = len(text)

for i in range(len-1, -1, -1):
    print(text[i], end="")

print(text[::-1])