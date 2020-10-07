import pickle
# pickle is used objects to be saved to a file so that they can be stored
# we are storing data into a file

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))
with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)
# ('More Mayhem', 'Imelda May', '2011', ((1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')))
album, artist, year, track_list = imelda2
print(album)  # More Mayhem
print(artist)  # Imelda May
print(year)  # 2011
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)
# 1 Pulling the Rug
# 2 Psycho
# 3 Mayhem
# 4 Kentish Town Waltz

print("----")

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=0)
    pickle.dump(2998302, pickle_file, protocol=0)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)
print("=" * 40)

for i in even_list:
    print(i)
# 0
# 2
# 4
# 6
# 8

print("=" * 40)

for i in odd_list:
    print(i)
# 1
# 3
# 5
# 7
# 9

print("=" * 40)
print(x) #2998302

print("=" * 40)

# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.") #for windows to remove the file
