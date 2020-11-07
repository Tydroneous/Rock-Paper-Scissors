# read animals.txt
old_file = open("animals.txt", "r")
# and write animals_new.txt
my_file = open("animals_new.txt", "w")

for i in old_file:
    my_file.write(i.rstrip("\n") + " ")

old_file.close()
my_file.close()
