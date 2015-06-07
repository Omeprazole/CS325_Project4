#!/usr/bin/python

import sys, math, timeit, decimal

#usage: python tsp.py input_file

def main(input_file):
	#open the input file, the file name from command line
	ifile = open(input_file,'r')

	#split each line in the file
	cities_raw = ifile.read().splitlines()

	#Define a list to hold the identifier of cities
	cities = list()

	#Define a list to hold the coordinates of each city
	coords = list()
	
	#Define a list to hold the lenght(The first element) and path
	len_path = list()
	
	#Extract data from file
	for city in cities_raw:
		temp = city.split()
		coord = (int(temp[1]), int(temp[2]))
		coords.append(coord)
		cities.append(int(temp[0]))
	ifile.close()
	
	#record time
	start_time = timeit.default_timer()

	#get the total length and path 
	len_path = tsp_dp(cities, coords)
	end_time = timeit.default_timer()

	print "Time for get the tour is: " + str(end_time - start_time) + " s" 

	#Get the name of output file
	output_file = input_file + '.tour'

	#open the output file
	ofile = open(output_file, 'w')

	#Output results into output file
	for i in range(len(len_path) ):
		ofile.write(str(len_path[i]) + "\n")


	ofile.close()

#Calculate distance from city i to city j
def get_distance(coords, i, j):
	iCoordx = coords[i][0]
	iCoordy = coords[i][1]
	jCoordx = coords[j][0]
	jCoordy = coords[j][1]
	distance = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))
	return distance

#Get the minimum distance from city endpoint to all the cities in unvisited list
def nearest(coords, unvisited, endpoint):
	nearest_dis = float('inf')
	for i in unvisited.keys():
		cur_dis = get_distance(coords, i, endpoint)
		if(cur_dis < nearest_dis):
			nearest_city = i
			nearest_dis = cur_dis
	return (nearest_city, nearest_dis)
		
#Dynamic programming: Add the nearest city(from unvisited cities to endpoints)
#to the path, until all the cities are added to the path.
def tsp_dp(cities, coords):
	sub_length = get_distance(coords, 0, 1)
	end_point_1 = 0;

	#Define a list to hold the path of shortest path
	path = list()

	#Define a dictionary to hold visited cities
	visited = dict()
	#Define a dictionary to hold unvisited cities
	unvisited = dict()
	for i in range(0, len(cities)):
		unvisited[i] = True

	#start the path with city 0
	path.append(0)
	visited[0] = True
	del unvisited[0]

	#Get the nearest city to city 0
	(nearest_city, sub_length) = nearest(coords, unvisited, 0)
	path.append(nearest_city)
	visited[nearest_city] = True
	del unvisited[nearest_city]

	#Initailize the two endpoints
	ep_front = 0
	ep_end = nearest_city


	#In the loop, add the nearest city to endpoints to path
	while(len(unvisited) > 0):
		#Get the nearest city to the front endpoint
		#and the distance between those two cities
		(nearest_front, front_dis) = nearest(coords, unvisited, ep_front)
		
		#Get the nearest city to the end endpoint
		#and the distance between those two cities
		(nearest_end, end_dis) = nearest(coords, unvisited, ep_end)

		#Compare the above two minimum distances
		if(front_dis < end_dis):
			#reset front endpoint
			ep_front = nearest_front
			path.insert(0, nearest_front) 
			sub_length = front_dis + sub_length
			del unvisited[ep_front]
		else:
			#reset end endpoint
			ep_end = nearest_end
			path.append(nearest_end)
			sub_length = end_dis + sub_length
			del unvisited[ep_end]

	#Get the length of the tour/path
	length = int(round(sub_length + get_distance(coords, ep_front, ep_end)))
	print(length)
	return [length] + path

if __name__ == "__main__":
	sys.exit(main(sys.argv[1]))
