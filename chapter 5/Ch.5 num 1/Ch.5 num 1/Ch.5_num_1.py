import random 
words = ["ОЧЕНЬ", "НАДОЕЛО", "УЧИТЬСЯ", "АНТИХАЙРП"]
str = []
while len(words) > 0   :
    str = words.pop(random.randint(0, len(words) - 1))
    print(str)