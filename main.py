import pprint
import sys
import random

with open(f"{sys.argv[1]}.txt", "r") as f:
    lines = f.readlines()

family = 0
people = {}
choices = {}
for line in lines:
    if line == "\n":
        family += 1
    else:
        people[line.strip("\n")] = family
        choices[line.strip("\n")] = ""

i = 0

while True:
    invalid = False
    unchosenPeople = list(people.keys())

    for person in people.keys():
        random.shuffle(unchosenPeople)
        for choice in unchosenPeople:
            if people[choice] != people[person]:
                break
        else:
            invalid = True
        unchosenPeople.remove(choice)
        choices[person] = choice
    
    if not invalid:
        break
    
    i+=1

print(i)
# pprint.pprint(choices)

with open (f"{sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]+'-out'}.txt", "w") as f:
    for person in choices:
        f.write(f"{person} -> {choices[person]}\n")