import shelve
#
# blt = ["bacon", "lettuce", "tomatoe", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tino of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes') as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    for snack in recipes:
        print(snack, recipes[snack])
# blt ['bacon', 'lettuce', 'tomatoe', 'bread']
# beans on toast ['beans', 'bread']
# scrambled eggs ['eggs', 'butter', 'milk']
# pasta ['pasta', 'cheese']
# soup ['tino of soup']

    print()

#what happens when we modify the list
    #note you have to make a temporarly list
    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])
# blt ['bacon', 'lettuce', 'tomatoe', 'bread', 'butter']
# beans on toast ['beans', 'bread']
# scrambled eggs ['eggs', 'butter', 'milk']
# pasta ['pasta', 'cheese', 'tomato']
# soup ['tino of soup']
    print()


#a different way of modifying the list
with shelve.open('recipes', writeback=True) as recipes:
    recipes["soup"].append("croutons")

    for snack in recipes:
        print(snack, recipes[snack])
#
# blt ['bacon', 'lettuce', 'tomatoe', 'bread', 'butter', 'butter']
# beans on toast ['beans', 'bread']
# scrambled eggs ['eggs', 'butter', 'milk']
# pasta ['pasta', 'cheese', 'tomato', 'tomato']
# soup ['tino of soup', 'croutons']


