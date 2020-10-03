# write a program that reads a text file

jabber = open("C:/Users/btemo/IdeaProjects/Udemy/Python/8 Section/sample.txt", 'r')  # opens the text file in read only
for line in jabber:  # circling through each line
    print(line)
jabber.close()  # closes the file
# Twas brillig, and the slithy toves
# Did gyre and gimble in the wabe;
# All mimsy were the borogoves,
# And the mome raths outgrabe.
# "Beware the Jabberwock, my son!
print("---")

with open("sample.txt", "r") as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

# "Beware the Jabberwock, my son!
# The Jabberwock, with eyes of flame,
# "And hast thou slain the Jabberwock?
print("---")

with open("sample.txt", "r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')  #the end='' is what makes the double spacing to go away
        line = jabber.readline()
#it eliminates the double spacing

# print("-----")
# with open("sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines:
#     print(line, end='')
# #also does the same thing
# print("----")
#
# with open("sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line, end='')
