# read sample.txt and print the number of lines
my_file = open("sample.txt", "r")
print(len(my_file.readlines()))
my_file.close()

