""" Part 1 """
with open('input_d2.txt') as f:
    data = [line.split() for line in f]
    print(data)
area_total = 0
for x in data:
    list = x[0].split('x')
    li = []
    for y in list:
        li.append(int(y))
    li.sort()
    area_inc = 2*(li[0]*li[1]+li[1]*li[2]+li[0]*li[2])+li[0]*li[1]
    area_total = area_total + area_inc


print(li)
print(area_total)

""" part 2 """

ribbon_total = 0
for x in data:
    list = x[0].split('x')
    li = []
    for y in list:
        li.append(int(y))
    li.sort()
    ribbon_inc =  2*(li[0]+li[1])+li[0]*li[1]*li[2]
    ribbon_total = ribbon_total + ribbon_inc

print(ribbon_total)

    



