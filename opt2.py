import math, sys, timeit

class Point:
    def __init__(self,x,y):
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

for city in cities_raw:
    temp = city.split()
    cities.append({'no':int(temp[0]),'x':int(temp[1]), 'y':int(temp[2])})

def calc_dist(city_a, city_b):
    delta_x = city_a['x'] - city_b['x']
    delta_y = city_a['y'] - city_b['y']
    total = round(math.sqrt(delta_x**2 + delta_y**2))
    return total

def path_dist(path):
    distance = 0
    for i in range(0,len(path)-1):
        distance += calc_dist(path[i], path[i+1])
    distance += calc_dist(path[0], path[len(path)-1])
    return int(distance)
        
def build_edge_list(path):
    edges = list()
    for i in range(0,len(path)-1):
        a = Point(path[i]['x'],path[i]['y'])
        b = Point(path[i+1]['x'],path[i+1]['y'])
        edges.append([a,b])
    last = len(path) - 1
    temp_a = Point(path[last]['x'],path[last]['y'])
    temp_b = Point(path[0]['x'],path[0]['y'])
    edges.append([temp_a,temp_b])
    return edges

def calc_edge_dist(edge):
    delta_x = edge[0].x - edge[1].x
    delta_y = edge[0].y - edge[1].y
    total = round(math.sqrt(delta_x**2 + delta_y**2))
    return total

def calc_edge_list_dist(edge_list):
    distance = 0
    for i in range(0, len(edge_list)):
        distance += calc_edge_dist(edge_list[i])
    return int(distance)

def display_edges(edge_list):
    for i in range(0, len(edge_list)):
        print edge_list[i][0].x, edge_list[i][0].y
    
def display_path_edges(path):
    for i in range(0, len(path)):
        print path[i]['x'],path[i]['y'],path[i+1]['x'],path[i+1]['y']

#def unique(a,b,c,d):
#   if a.x == c.x and a.y == c.y:
#       return False
#   if b.x == d.x and b.y == d.y:
#       return False
#   return True

def optimize(edge_list):
    for i in range(0, len(edge_list)):
        for j in range(i+1, len(edge_list)):
            a = Point(edge_list[i][0].x, edge_list[i][0].y)
            b = Point(edge_list[i][1].x, edge_list[i][1].y)
            c = Point(edge_list[j][0].x, edge_list[j][0].y)
            d = Point(edge_list[j][1].x, edge_list[j][1].y)
            if intersect(a,b,c,d):
                edge_list[i][1] = c
                edge_list[j][0] = b
    return edge_list

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


path = reached
print path_dist(reached)


edge_list = build_edge_list(reached)
display_edges(edge_list)
edge_list = optimize(edge_list)
print calc_edge_list_dist(edge_list)



output_file = input_file + '.tour'
ofile = open(output_file,'w')
ofile.write(str(path_dist(reached))+"\n")
for i in range(0, len(reached)):
    ofile.write(str(reached[i]['no']) + ' ')
    ofile.write(str(reached[i]['x']) + ' ')
    ofile.write(str(reached[i]['y']) + '\n')
ofile.close()


#found on stack overflow
def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


