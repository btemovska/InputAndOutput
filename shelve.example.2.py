import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])
print()

#add new value to a already existing key
fruit["lime"] = "great with tequila"
for snack in fruit:
    print(snack + ": " + fruit[snack])

# orange: a sweet, orange citrus fruit
# apple: good for making cider
# lemon: a sour, yellow citrus fruit
# grape: a small, sweet fruit growing in bunches
# lime: great with tequila


fruit.close()

# print(fruit)


