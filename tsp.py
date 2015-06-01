import math

f = open('tsp_example_1.txt')

cities_raw = f.read().splitlines()
cities = list()
coords = dict()
distances = dict()

for city in cities_raw:
    temp = city.split(' ')
    xCoord = str(temp[0]) + 'x'
    yCoord = str(temp[0]) + 'y'
    coords[xCoord] = int(temp[1])
    coords[yCoord] = int(temp[2])
    cities.append(temp[0])

for i in range(0, len(cities)):
    for j in range (0, len(cities)):
        iCoordx = coords[str(i)+'x']
        iCoordy = coords[str(i)+'y']
        jCoordx = coords[str(j)+'x']
        jCoordy = coords[str(j)+'y']
        distance = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))
        distances[str(i)+ '-' + str(j)] = distance

unvisited_cities = dict()
current_path = list()
current_length = 0
current_city = -1
closest_city = -1
shortest_path = list()
shortest_length = float('inf')

def reset():
    global unvisited_cities, current_path, current_length, shortest_length
    for i in range(0, len(cities)):
        unvisited_cities[i] = i
    current_path = list()
    shortest_length = float('inf')
    current_length = 0
    
reset()

for i in range(0, len(cities)):
   reset()
   current_city = cities[i]
   del unvisited_cities[i]

   while(len(unvisited_cities) > 0):
       closest_distance = float('inf')
       closest_city = -1
       for each in unvisited_cities:
           distance = distances[str(each)+ '-' + str(current_city)]
           if distance > 0 and distance < closest_distance:
               closest_distance = distance
               closest_city = each
       current_city = closest_city
       current_path.append(str(closest_city))
       del unvisited_cities[closest_city]
       current_length = current_length + closest_distance
   if current_length < shortest_length:
       shortest_length = current_length
       shortest_path = current_path

print shortest_path
print shortest_length
