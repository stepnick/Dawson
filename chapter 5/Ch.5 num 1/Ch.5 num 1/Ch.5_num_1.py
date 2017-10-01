import random 
#import numpy 
words = ["ОЧЕНЬ", "НАДОЕЛО", "УЧИТЬСЯ", "АНТИХАЙП"]
str = []
str1 = [1, 2, 3, 4 ]
print(random.shuffle(words))
numberDEL2 = len(words) // 2

length = len(words)
#while len(words) > 0   :
    #str = words.pop(random.randint(0, len(words) - 1))
    #print(str)

for number in range(numberDEL2):
    #x = random.choice(words)
    #y = random.choice(words)
    #z = x 
    #x = y
    #y = z 

    x = random.randint(0, length)
    y = random.randint(0, length)
    buf = words[x]
    words[x] = words[y]
    words[y] = buf
   

for number in range(len(words)):
    print(words[number])