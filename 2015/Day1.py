""" Part 1 """

with open('input_d1.txt') as f:
    data = f.read()
print (data)

counter = 0
for x in data:
    if x == '(':
        counter = counter + 1
    elif x == ')':
        counter = counter - 1

print(counter)

""" Part 2 """
pos=0
test=[]
counter = 0
for x in data:
    if x == '(':
        counter = counter + 1
    elif x == ')':
        counter = counter - 1
    pos = pos+1
    if counter == -1:
        break
    test.append(counter)
print(test)
print("Counter reached ", counter, " at position ", pos)
