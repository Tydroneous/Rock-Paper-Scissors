# read sums.txt
my_file = open("sums.txt", "r")

for i in my_file:
    temp = i.split()
    print(int(temp[0]) + int(temp[int(1)]))
my_file.close()
