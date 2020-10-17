import shelve

locations = shelve.open('locations')
vocabulary = shelve.open('vocabulary')

loc = '1'
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc == '0':
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits).upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

locations.close()
vocabulary.close()

#
# You are standing at the end of a road before a small brick building
# Available exits are W, E, N, S, Qw
#
# You are at the top of a hill
# Available exits are N, Qn
#
# You are in the forest
# Available exits are W, S, Qs
#
# You are standing at the end of a road before a small brick building
# Available exits are W, E, N, S, Qq
#
# You are sitting in front of a computer learning Python