import math
import sys
import timeit

input_file = sys.argv[1]
#open the input file, the file name from command line
ifile = open(input_file,'r')

#split each line in the file
cities_raw = ifile.read().splitlines()

	#Define a list to hold the identifier of cities
cities = list()

	#Define a list to hold the coordinates of each city
coords = dict()

	#Define a list to hold the lenght(The first element) and path
len_path = list()

	#Extract data from file
for city in cities_raw:
    temp = city.split()
    xCoord = str(temp[0]) + 'x'
    yCoord = str(temp[0]) + 'y'
    coords[xCoord] = int(temp[1])
    coords[yCoord] = int(temp[2])
    cities.append(temp[0])
    ifile.close()

    start_time = timeit.default_timer()

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
    print closest_distance, closest_city
    shortest_length += closest_distance
    reached.append(str(closest_city))
    unreached.remove(str(closest_city))



shortest_path = 0
for i in range(0,len(reached)-1):
    j = i + 1
    iCoordx = coords[str(reached[i])+'x']
    iCoordy = coords[str(reached[i])+'y']
    jCoordx = coords[str(reached[j])+'x']
    jCoordy = coords[str(reached[j])+'y']
    distance = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))
    print iCoordx, iCoordy, jCoordx, jCoordy
    print "point1: %d point2: %d distance: %d" % (int(reached[i]), int(reached[j]), distance)

    shortest_path = distance + shortest_path

iCoordx = coords[str(reached[0])+'x']
iCoordy = coords[str(reached[0])+'y']
jCoordx = coords[str(reached[len(reached)-1])+'x']
jCoordy = coords[str(reached[len(reached)-1])+'y']
last_leg = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))
print shortest_path
print last_leg
shortest_length += last_leg
len_path = shortest_length
	#get the total length and path 


end_time = timeit.default_timer()

print "Time for get the tour is: " + str(10 * (end_time - start_time)) + " ms" 
print len_path
print len(reached)

	#Get the name of output file
output_file = input_file + '.tour'

	#open the output file
ofile = open(output_file, 'w')

#Output results into output file

ofile.write(str(int(len_path)) + "\n")
for i in range(0, len(reached)):
    ofile.write(str(reached[i]) + "\n")

ofile.close();
