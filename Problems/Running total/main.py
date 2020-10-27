my_input = input()
numbers = [i for i in str(my_input)]
print(numbers)
length = len(numbers)
new_array = [numbers[0]]
for i in range(length - 1):

    new_array.append(numbers[i - 1] + numbers[i])


print(new_array)
