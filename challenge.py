# Write a program to append the times tables to our jabberwock poem
# in sample.txt we want the tables from 2 to 12 (Similar to the output
# from the For loops part 2 lecture in section 6)

#The first column of numbers should be right justified. As an example
# the 2 times table should look like this:
# 1 times 2 is 2
# 2 times 2 is 4
# 3 times 2 is 6
# 4 times 2 is 8
# 5 times 2 is 10
# 6 times 2 is 12
# 7 times 2 is 14
# 8 times 2 is 16
# 9 times 2 is 18
# 10 times 2 is 20
# 11 times 2 is 22
# 12 times 2 is 24
#------------------

with open("sample.txt", 'a') as tables:
    for i in range(2, 13):
        for j in range (1, 13):
            print("1:>2 times {0} is {2}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)
# this will append to the file

# 'Twas brillig, and the slithy toves
# Did gyre and gimble in the wabe:
# All mimsy were the borogoves,
# And the mome raths outgrabe.
#
# 1:>2 times 2 is 2
# 1:>2 times 2 is 4
# 1:>2 times 2 is 6
# 1:>2 times 2 is 8
# 1:>2 times 2 is 10
# 1:>2 times 2 is 12
# 1:>2 times 2 is 14
# 1:>2 times 2 is 16
# 1:>2 times 2 is 18
# 1:>2 times 2 is 20
# 1:>2 times 2 is 22
# 1:>2 times 2 is 24
# --------------------
# 1:>2 times 3 is 3
# 1:>2 times 3 is 6
# 1:>2 times 3 is 9
# 1:>2 times 3 is 12

#if you run it again it will append at the end


with open("sample2.txt", 'w') as tables:
    for i in range(2, 13):
        for j in range (1, 13):
            print("1:>2 times {0} is {2}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)

# w created new file and inputed thse values
# 1:>2 times 2 is 2
# 1:>2 times 2 is 4
# 1:>2 times 2 is 6
# 1:>2 times 2 is 8
# 1:>2 times 2 is 10
# 1:>2 times 2 is 12
# 1:>2 times 2 is 14
# 1:>2 times 2 is 16
# 1:>2 times 2 is 18
# 1:>2 times 2 is 20
# 1:>2 times 2 is 22
# 1:>2 times 2 is 24
# --------------------
# 1:>2 times 3 is 3
# 1:>2 times 3 is 6
# 1:>2 times 3 is 9
# 1:>2 times 3 is 12
# 1:>2 times 3 is 15
# 1:>2 times 3 is 18
# 1:>2 times 3 is 21
# 1:>2 times 3 is 24
# 1:>2 times 3 is 27
# 1:>2 times 3 is 30
# 1:>2 times 3 is 33
# 1:>2 times 3 is 36
# --------------------