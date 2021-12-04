""" part 1
"""

with open('input_d3.txt') as f:
    data = f.read()
print(len(data))
x = 0  #first x-position in the grid
y = 0  #first y-position in the grid
visited_list = [[0,0]]
visited = 1
for z in data:
    if z == '<':
        x -= 1
    elif z == '>':
        x += 1
    elif z == '^':
        y += 1
    elif z == 'v':
        y -= 1
    if [x,y] not in visited_list:
        visited_list.append([x,y])
        visited += 1 
print(visited)


""" part 2 """
x = 0  #first x-position in the grid
y = 0  #first y-position in the grid
x2 = 0
y2 = 0
visited_list = [[0,0]]
visited = 1
santa = True
for z in data:
    if santa:
        if z == '<':
            x -= 1
        elif z == '>':
            x += 1
        elif z == '^':
            y += 1
        elif z == 'v':
            y -= 1
        if [x,y] not in visited_list:
            visited_list.append([x,y])
            visited += 1
        santa = False 
    else:
        if z == '<':
            x2 -= 1
        elif z == '>':
            x2 += 1
        elif z == '^':
            y2 += 1
        elif z == 'v':
            y2 -= 1
        if [x2,y2] not in visited_list:
            visited_list.append([x2,y2])
            visited += 1 
        santa = True
print(visited)