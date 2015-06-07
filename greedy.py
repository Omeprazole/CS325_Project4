import math, sys, timeit

input_file = sys.argv[1]

ifile = open(input_file,'r')

cities_raw = ifile.read().splitlines()
ifile.close()

cities = list()

for city in cities_raw:
    temp = city.split()
    cities.append({'no':int(temp[0]),'x':int(temp[1]), 'y':int(temp[2])})


def calc_dist(city_a, city_b):
    delta_x = city_a['x'] - city_b['x']
    delta_y = city_a['y'] - city_b['y']
    return round(math.sqrt(delta_x**2 + delta_y**2))

def path_dist(path):
    distance = 0
    for i in range(0,len(path)-1):
        distance += calc_dist(path[i], path[i+1])
    distance += calc_dist(path[0], path[len(path)-1])
    return int(distance)
                      
start_time = timeit.default_timer()

reached = list()
unreached = cities
reached.append(unreached[0])
unreached.remove(reached[0])

while(len(unreached) > 0):
    current_city = reached[len(reached)-1]
    closest_city = unreached[0]
    closest_dist = calc_dist(current_city,closest_city)
    for i in range(0, len(unreached)):
        distance = calc_dist(current_city, unreached[i])
        if distance < closest_dist:
            closest_dist = distance
            closest_city = unreached[i]
    reached.append(closest_city)
    unreached.remove(closest_city)

end_time = timeit.default_timer()

print "Time for get the tour is: " + str(10 * (end_time - start_time)) + " ms" 

output_file = input_file + '.tour'
ofile = open(output_file,'w')
ofile.write(str(path_dist(reached))+"\n")
for i in range(0, len(reached)):
    ofile.write(str(reached[i]['no']) + ' ')
    ofile.write(str(reached[i]['x']) + ' ')
    ofile.write(str(reached[i]['y']) + '\n')
ofile.close()




