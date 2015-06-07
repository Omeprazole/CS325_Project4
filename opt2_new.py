import math, sys, timeit

class City:
    def __init__(self,num,x,y):
        self.num = num
        self.x = x
        self.y = y

#found on stack overflow
def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

input_file = sys.argv[1]

ifile = open(input_file,'r')

cities_raw = ifile.read().splitlines()
ifile.close()

cities = list()

def path_dist(cities):
    distance = 0
    for i in range(0,len(cities)-1):
        distance += calc_dist(cities[i],cities[i+1])
    return int(distance + calc_dist(cities[0],cities[len(cities)-1]))
        

def calc_dist(a, b):
    delta_x = a.x - b.x
    delta_y = a.y - b.y
    return round(math.sqrt(delta_x**2 + delta_y**2))

def print_city(city):
    print city.x, city.y

def print_path(path):
    for i in range(0,len(path)):
        print_city(path[i])

def city_to_string(city):
    return str(city.num)+" "+str(city.x)+" "+str(city.y)

def optimize(cities):
    for i in range(0, len(cities)-1):
        for j in range(i+2, len(cities)-1):
            a = cities[i]
            b = cities[i+1]
            c = cities[j]
            d = cities[j+1]
            if intersect(a,b,c,d):
                temp_cities = list(cities)
                temp_cities[i+1] = c
                temp_cities[j] = b
                if path_dist(cities) > path_dist(temp_cities):
                    cities = list(temp_cities)
    return cities
    
for city in cities_raw:
    temp = city.split()
    a = City(int(temp[0]),int(temp[1]),int(temp[2]))
    cities.append(a)

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


path = list(reached)
#print path_dist(path)
#print len(path)
#print_path(path)
one_pass = list(optimize(path))
print path_dist(one_pass)
print len(one_pass)



output_file = input_file + '.tour'
ofile = open(output_file,'w')
ofile.write(str(path_dist(one_pass))+"\n")
for i in range(0, len(one_pass)):
    ofile.write(city_to_string(one_pass[i])+"\n")
ofile.close()
