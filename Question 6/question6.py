#The working principle of the code:
#     The ray method can be used to determine whether a point is in a polygon.
#     If the number of intersections with the polygon is odd, 
#           then the point is inside the polygon, 
#           otherwise it is outside the polygon.

#Steps:
#     First, use the loop to treat each side of the polygon the same way.
#     Then, determine whether there is an intersection with the horizontal right ray of point P. 
#           If there is an intersection, the flag is flipped once.

def is_in_polygon(point, polygon):
    px, py = point
    is_in = False
    for i, corner in enumerate(polygon):
        #enumerate: index value and element value can be obtained simultaneously during the loop
        next_i = i + 1 if i + 1 < len(polygon) else 0
        x1, y1 = corner
        x2, y2 = polygon[next_i]
        if (x1 == px and y1 == py) or (x2 == px and y2 == py):  # if point is on vertex
            is_in = True
            break
        if min(y1, y2) < py <= max(y1, y2):          # find horizontal edges of polygon
            x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x == px:                                           # if point is on edge
                is_in = True
                break
            elif x > px:                             # if point is on left-side of line
                is_in = not is_in
    if is_in == True:
        is_in ="inside"
    else:
        is_in="outside"
    return is_in

def readData(filename):
    file=open(filename)
    data=file.readlines()
    res=[]
    for i in data:
        tmp=i.strip().split()                        #Split data
        res.append([int(i) for i in tmp])            #Convert to float 
    return res

polygon=readData('input_question_6_polygon')
point=readData('input_question_6_points')
file=open('output_question_6',mode='w')
for i in range(len(polygon)):
     file.write(f'{point[i][0]} {point[i][1]} '+is_in_polygon(point[i], polygon)+'\n')
file.close()

