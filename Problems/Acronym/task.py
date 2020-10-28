# read test.txt
my_text = open("test.txt", "r")

for line in my_text:
    print(line[0])
my_text.close()
