import shelve
#large dictionary if needed to be loaded in memory, use shelve
#it is stored in a file, rather in memory


with shelve.open("bike") as bike:
    bike['make'] = "Honda"
    bike['model'] = "250 dream"
    bike['colour'] = "read"
    bike['engine_size'] = "250"

    print(bike["engine_size"])  # 250
    print(bike["colour"])  # red

    for key in bike:
        print(key)
#make
# model
# colour
# engine_size

    del bike['model']

    for key in bike:
        print(key)
# make
# colour
# engine_size

