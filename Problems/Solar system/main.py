my_file = open("planets.txt", "w", encoding='utf-8')

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for i in planets:
    my_file.write(i + "\n")
my_file.close()
