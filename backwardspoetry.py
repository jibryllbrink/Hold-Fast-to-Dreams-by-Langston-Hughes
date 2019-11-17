import random, upsidedown


def get_poem():
    # returns poem list from poetry.txt
    f = open('poetry.txt', 'r')
    poem = f.readlines()
    f.close()

    return poem


def print_poem(input):

    for index in range(0, len(input)):
        line = input[index]
        print(str(index)+": "+line)

def sorted_sentence(input):
    #def sorted_sentence():
    # implement a function of your choice that rearranges the poem in a unique way

    for index in range(0, len(input)):
        line = upsidedown.transform(input[index])
        print(str(index)+": "+line)



def lines_printed_backwards(input):
#This function takes in a list of strings containing the lines of your poem as arguments and
#  will print the poem lines out in reverse with the line numbers reversed."""
    for index in range(len(input), 0, -1):
        print(str(index)+": "+input[index-1])


def lines_printed_random(input):
    #def lines_printed_random():
    # function which will randomly select lines from a list of strings and print them out in random order.
    for index in range(0, len(input)):
        random_index = random.randint(0, len(input)-1)
        line = input[index]
        print(str(random_index)+": "+line)
        
    


        
__name__ == "__main__"


# Poem author: "Hold Fast To Dreams" By Langston Hughes
input = get_poem()
print()
print("_________ Poem _________\n")

print_poem(input)

print()
print("_________ Reversed _________\n")

lines_printed_backwards(input)

print()
print("_________ Random _________\n")

lines_printed_random(input)

print()
print("_________ Unique _________\n")

sorted_sentence(input)


