import math

f = open('tsp_example_1.txt')

cities_raw = f.read().splitlines()
cities = list()
coords = dict()
distances = dict()

for city in cities_raw:
    temp = city.split()
    xCoord = str(temp[0]) + 'x'
    yCoord = str(temp[0]) + 'y'
    coords[xCoord] = int(temp[1])
    coords[yCoord] = int(temp[2])
    cities.append(temp[0])

#for i in range(0, len(cities)):
#   for j in range (0, len(cities)):
#       iCoordx = coords[str(i)+'x']
#       iCoordy = coords[str(i)+'y']
#       jCoordx = coords[str(j)+'x']
#       jCoordy = coords[str(j)+'y']
#       distance = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))
#       distances[str(i)+ '-' + str(j)] = distance

reached = list()
unreached = cities
distances = dict()

temp_city = unreached[0]
reached.append(temp_city)
unreached.remove(temp_city)
current_city = 0
closest = float('inf')
shortest_length = 0

while (len(unreached) > 0):
    closest_distance = float('inf')
    for i in range(0, len(reached)):
        for j in range(0, len(unreached)):
            iCoordx = coords[str(reached[i])+'x']
            iCoordy = coords[str(reached[i])+'y']
            jCoordx = coords[str(unreached[j])+'x']
            jCoordy = coords[str(unreached[j])+'y']
            distance = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))
            if distance < closest_distance:
                closest_distance = distance
                closest_city = unreached[j]
    shortest_length += closest_distance
    reached.append(str(closest_city))
    unreached.remove(str(closest_city))

iCoordx = coords[str(reached[0])+'x']
iCoordy = coords[str(reached[0])+'y']
jCoordx = coords[str(reached[len(reached)-1])+'x']
jCoordy = coords[str(reached[len(reached)-1])+'y']

last_leg = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))

shortest_length += last_leg
print reached
print "Number of Cities: ",len(reached)
print "Length of Shortest Path: ",shortest_length
