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
	
	#record time
	start_time = timeit.default_timer()

	#get the total length and path 
	#len_path = tsp_greedy(cities, coords)
	len_path = tsp_dp(cities, coords)
	end_time = timeit.default_timer()

	print "Time for get the tour is: " + str(end_time - start_time) + " s" 

	#Get the name of output file
	output_file = input_file + '.tour'

	#open the output file
	ofile = open(output_file, 'w')

	#Output results into output file
	for i in range(len(len_path) ):
		ofile.write(len_path[i] + "\n")


	ofile.close()

#Calculate distance from city i to city j
def get_distance(coords, i, j):
	iCoordx = coords[str(i)+'x']
	iCoordy = coords[str(i)+'y']
	jCoordx = coords[str(j)+'x']
	jCoordy = coords[str(j)+'y']
	distance = round(math.sqrt(pow((iCoordx - jCoordx),2)+pow((iCoordy - jCoordy),2)))
	return distance

#Get the total distance of a path
def get_length(coords, path, cities):
	dis = 0
	for i in range(len(path)):
		dis = dis + get_distance(coords, cities[path[i]], cities[path[i - 1]])
	return dis

def nearest(coords, unvisited, endpoint):
	nearest_dis = float('inf')
	for i in range(len(unvisited)):
		cur_dis = get_distance(coords, unvisited[i], endpoint)
		if(cur_dis < nearest_dis):
			nearest_city = unvisited[i]
			nearest_dis = cur_dis
	return nearest_city
		

def tsp_dp(cities, coords):
        #distances = dict()
	sub_length = get_distance(coords, 0, 1)
	end_point_1 = 0;
	path = list()
	unvisited = dict()
	for i in range(0, len(cities)):
		unvisited.append(i)

	path.append(0)
	unvisited.remove(0)
	nearest_city = nearest(coords, unvisited, 0)
	path.append(nearest_city)
	unvisited.remove(nearest_city)
	ep_front = 0
	ep_end = nearest_city
	print("first nearest city" + str(nearest_city))
	print("fisrt end" + str(nearest_city))
	sub_length = get_distance(coords, 0, nearest_city) 



	#front_flag = 1
	#end_flag = 1
	while(len(unvisited) > 0):
		front_flag = 1
		end_flag = 1
		for i in range(len(cities)):
			visited_flag = 0
			for j in range(len(path)):
				if(i == path[j]):
					visited_flag = 1
					break
	
			if(visited_flag == 1):
				continue
			print("front_flag " + str(front_flag))		
			print("end_flag " + str(end_flag))		

			if(front_flag == 1): 
				print("front near")
				nearest_front = nearest(coords, unvisited, ep_front)
				front_dis = get_distance(coords, nearest_front, ep_front)
			if(end_flag == 1):
				print("end near")
				nearest_end = nearest(coords, unvisited, ep_end)
				end_dis = get_distance(coords, nearest_end, ep_end)
			#print("nearest_front " + str(nearest_front))
			#print("nearest_end " + str(nearest_end))


			print("front_dis " + str(front_dis))
			print("end_dis " + str(end_dis))

			if(front_dis < end_dis):
				ep_front = nearest_front
				path.insert(0, nearest_front) 
				sub_length = front_dis + sub_length
				print("ep_front " + str(ep_front))
				unvisited.remove(ep_front)
				#end_flag = 0
				front_flag = 1
			else:
				ep_end = nearest_end
				print("ep_end " + str(ep_end))
				path.append(nearest_end)
				sub_length = end_dis + sub_length
				unvisited.remove(ep_end)
				#front_flag = 0
				end_flag = 1
			print("path ")
			print (path)
			#print("unvisited")
			#print(unvisited)
			print("sub_length:" + str(sub_length))

	length = sub_length + get_distance(coords, ep_front, ep_end)
	#length_1 = get_length(coords, path, cities)
	print(path)
	#print(cities)
	print("path_lenght " + str(len(path)))
	print(length)
	#print(length_1)
	return [length] + path


#Greedy algorithm for tsp problem
"""
def tsp_greedy(cities, coords):
	unvisited = dict()
	current_path = list()
	current_length = 0
	current_city = -1
	closest_city = -1
	shortest_path = list()
	shortest_length = float('inf')

	for i in range(0, len(cities)):
		unvisited[i] = i
	current_path = list()
	shortest_length = float('inf')
	current_length = 0

	distances = dict()
	for i in range(0, len(cities)):
		for j in range (0, len(cities)):
			distances[str(i)+ '-' + str(j)] = get_distance(coords, i, j)

	for i in range(0, len(cities)):
		for i in range(0, len(cities)):
			unvisited[i] = i
		current_path = list()
		shortest_length = float('inf')
		current_length = 0

		current_city = cities[i]
		del unvisited[i]

		current_path.append(str(i))
		while(len(unvisited) > 0):
			closest_distance = float('inf')
			closest_city = -1
			for each in unvisited:
				distance = distances[str(each)+ '-' + str(current_city)]
				if distance > 0 and distance < closest_distance:
					closest_distance = distance
					closest_city = each
			current_city = closest_city
			current_path.append(str(closest_city))
 			del unvisited[closest_city]
			current_length = current_length + closest_distance
		if current_length < shortest_length:
 			shortest_length = current_length
			shortest_path = current_path

	#Add the distance from last city to the first city to shortest length
	start = shortest_path[0]
	end = shortest_path[len(shortest_path) - 1]
	shortest_length = shortest_length + distances[str(start)+'-'+str(end)]

	#Convert float to integer
	shortest_length = int(round(shortest_length))
	return [str(shortest_length)] + shortest_path
"""


if __name__ == "__main__":
	sys.exit(main(sys.argv[1]))
