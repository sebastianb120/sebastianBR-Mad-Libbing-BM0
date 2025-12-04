import random
from random import randint


print("adjective:")
adj1 = input()

print("adjective:")
adj2 = input()

print( "a place: ")
place = input()

print( "a verb ending in ING: ")
verb = input()

storynum = random.randint(0,1)

if storynum == 1:
	print(f"{place}, the location of the {adj1} {verb} turtle goose, I love {adj2} turtle-geese like him")

if storynum == 0:
	print(f"from the journal of clornton the explorer: a {adj1} being sat {verb} in front of me, it was then I realized I was in{place}. This {adj2} land is home to many creatures.")