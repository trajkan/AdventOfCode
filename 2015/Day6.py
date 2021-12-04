""" Day 6: Probably a fire hazard """
import json
import re
with open('input_d6.txt') as f:
    data = f.readlines()

lights_grid = []
for x in range(1000):
    for y in range(1000):
        lights_grid.append([x, y, 0])

xy_regex = re.compile(r'([0-9,]*) through ([0-9,]*)')
# action = ''
for instructions in data:
    if 'on' in instructions:
        action = 'on'
    elif 'off' in instructions:
        action = 'off'
    elif 'toggle' in instructions:
        action = 'toggle'

    first_xy = xy_regex.search(instructions).group(1)
    second_xy = xy_regex.search(instructions).group(2)
    x1 = int(first_xy.split(',')[0])
    y1 = int(first_xy.split(',')[1])
    x2 = int(second_xy.split(',')[0])
    y2 = int(second_xy.split(',')[1])

    delta_x = x2 - x1
    delta_y = y2 - y1

    for x in range(x1,x1+delta_x+1):
        for y in range(y1, y1+delta_y+1):
            pos = x*1000 + y
            if action == 'on':
                lights_grid[pos] = [x, y, 1]
            elif action == 'off':
                lights_grid[pos] = [x, y, 0]
            elif action == 'toggle':
                if lights_grid[pos][2] == 0:
                    lights_grid[pos] = [x, y, 1]
                elif lights_grid[pos][2] == 1:
                    lights_grid[pos] =[x, y, 0]

on = 0
for light in lights_grid:
    on += light[2] 

print('number of light on: ', on)





""" part 2 """

lights_grid = []
for x in range(1000):
    for y in range(1000):
        lights_grid.append([x, y, 0])

xy_regex = re.compile(r'([0-9,]*) through ([0-9,]*)')
# action = ''
for instructions in data:
    if 'on' in instructions:
        action = 'on'
    elif 'off' in instructions:
        action = 'off'
    elif 'toggle' in instructions:
        action = 'toggle'

    first_xy = xy_regex.search(instructions).group(1)
    second_xy = xy_regex.search(instructions).group(2)
    x1 = int(first_xy.split(',')[0])
    y1 = int(first_xy.split(',')[1])
    x2 = int(second_xy.split(',')[0])
    y2 = int(second_xy.split(',')[1])

    delta_x = x2 - x1
    delta_y = y2 - y1

    for x in range(x1,x1+delta_x+1):
        for y in range(y1, y1+delta_y+1):
            pos = x*1000 + y
            if action == 'on':
                brightness = lights_grid[pos][2]
                lights_grid[pos] = [x, y, brightness + 1]
            elif action == 'off':
                brightness = lights_grid[pos][2]
                if brightness > 0:
                    lights_grid[pos] = [x, y, brightness-1]
            elif action == 'toggle':
                brightness = lights_grid[pos][2]
                lights_grid[pos] = [x, y, brightness+2]


brightness_total = 0
for light in lights_grid:
    brightness_total += light[2]

print('Total brightness:', brightness_total)



