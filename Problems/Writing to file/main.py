f_name = "test.txt"
my_string = "A string to be written to a file!"
my_file = open(f_name, "w")
# what to do with the file and the string
print(my_string, file=my_file)
my_file.close()
