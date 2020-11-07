numbers = [1234, 5678, 90]
string_num = str(numbers)

# save this list in `file_with_list.txt`
my_file = open("file_with_list.txt", "w")
my_file.write(string_num)
my_file.close()
