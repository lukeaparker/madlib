from random import shuffle 

nouns = list()
verbs = list()
adjectives = list()
people = list()

def pos_input(pos):
    for _ in range(4):
        pos.append(input())

name = input('Hello! What is your name? ')
print("hello " + name + " we're going to create a little story!")

print("Start by giving me a couple objective nouns...")
pos_input(nouns)
print("Now try giving me a couple action verbs...")
pos_input(verbs)
print("Almost done! Shout out some adjectives...")
pos_input(adjectives)
print("Finally give me some names")
pos_input(people)

shuffle(nouns)
shuffle(verbs)
shuffle(adjectives)
shuffle(people)

print("Great! Now story time!")

madlib = f"""{people[0]} was afraid to go outside because of the spiders. They went online and saw a 
{nouns[0]} that interested him. {people[0]} decided to buy {nouns[0]}. The next day {people[0]} went outside and {verbs[0]} the spiders 
with {nouns[0]}. {people[0]} invited {people[1]} to look at the
{adjectives[0]} spiders. They never feared the spiders again."""

print(madlib)


