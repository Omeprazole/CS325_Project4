#!/usr/bin/python

import sys, math, timeit

#usage: python tsp.py input_file

def main(input_file):
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
		temp = city.split(' ')
		xCoord = str(temp[0]) + 'x'
		yCoord = str(temp[0]) + 'y'
		coords[xCoord] = int(temp[1])
		coords[yCoord] = int(temp[2])
		cities.append(temp[0])
	ifile.close()
	
	#record time
	start_time = timeit.default_timer()

	#get the total length and path 
	len_path = tsp_greedy(cities, coords)
	end_time = timeit.default_timer()

	print "Time for get the tour is: " + str(end_time - start_time) + " s" 
	print len_path


	#Get the name of output file
	output_file = input_file + '.tour'

	#open the output file
	ofile = open(output_file, 'w')
	for i in range(len(len_path) ):
		ofile.write(len_path[i] + "\n")


	#Output results into output file
	ofile.close()

#Calculate distance from city i to city j
def get_distance(coords, i, j):
	iCoordx = coords[str(i)+'x']
	iCoordy = coords[str(i)+'y']
	jCoordx = coords[str(j)+'x']
	jCoordy = coords[str(j)+'y']
	distance = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))
	return distance

#Greedy algorithm for tsp problem
def tsp_greedy(cities, coords):
	unvisited_cities = dict()
	current_path = list()
	current_length = 0
	current_city = -1
	closest_city = -1
	shortest_path = list()
	shortest_length = float('inf')

	for i in range(0, len(cities)):
		unvisited_cities[i] = i
	current_path = list()
	shortest_length = float('inf')
	current_length = 0

	distances = dict()
	for i in range(0, len(cities)):
		for j in range (0, len(cities)):
			distances[str(i)+ '-' + str(j)] = get_distance(coords, i, j)

	for i in range(0, len(cities)):
		for i in range(0, len(cities)):
			unvisited_cities[i] = i
		current_path = list()
		shortest_length = float('inf')
		current_length = 0

		current_city = cities[i]
		del unvisited_cities[i]

		current_path.append(str(i))
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
	shortest_length = int(round(shortest_length))
	return [str(shortest_length)] + shortest_path

if __name__ == "__main__":
	sys.exit(main(sys.argv[1]))
