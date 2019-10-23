#This code takes a user's input for height and creates a 'mario-like' half pyramid with that height. This code was made by Julian.

height = int(input("Height: "))

while height < 0 or height > 23:
    print ("Try again!")
    height = int(input("Height: "))

length = height + 1

hashtag = "#"
layer = " "

for x in range (height, 0, -1):
    layer = " " * (x - 1)
    hashtag = "#" * (length - x + 1) 
    print (layer + hashtag)
