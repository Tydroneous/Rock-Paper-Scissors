seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
days = []
for i, _ in enumerate(seconds):
    temp = seconds[i] // (60 * 60 * 24)
    days.append(temp)

print(days)
