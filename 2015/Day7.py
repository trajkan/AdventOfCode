""" Day 7: Some assembly required """
import re

def instruction_execution(instruction):
    target_regex = re.compile(r'-> (\S+)')
    target_wire = target_regex.search(instruction).group(1)

    not_regex = re.compile(r'NOT (\S+) ->')
    connection_regex = re.compile(r'(\S+) ->')
    logical_regex = re.compile(r'(\S+) (AND|OR|LSHIFT|RSHIFT) (\S+) ->')
    if logical_regex.search(instruction):
        first = logical_regex.search(instruction).group(1)
        operation = logical_regex.search(instruction).group(2)
        second = logical_regex.search(instruction).group(3)

        if first.isnumeric():
            first_comp = int(first)
        else:
            first_comp = wires[first]

        if second.isnumeric():
            second_comp = int(second)
        else:
            second_comp = wires[second]

        if operation == 'LSHIFT':
            value = first_comp << second_comp

        elif operation == 'RSHIFT':
            value = first_comp >> second_comp

        elif operation == 'AND':
            value = first_comp & second_comp

        elif operation == 'OR':
            value = first_comp | second_comp

    elif not_regex.search(instruction):
        wire_value = wires[not_regex.search(instruction).group(1)]
        binary_value = bin(wire_value)[2:].zfill(16)
        not_binary = ''
        for bit in binary_value:
            if bit == '1':
                not_binary += '0'
            else:
                not_binary += '1'
        value = int(not_binary,2)
    elif connection_regex.search(instruction):
        new_value = connection_regex.search(instruction).group(1)
        if new_value.isnumeric():
            value = new_value
        else:
            value = wires[new_value]
    
    try:
        wires[target_wire] = int(value)
    except:
        return

    return True


with open('input_d7.txt') as f:
    instructions = f.readlines()

wires = {}
while instructions:
    completed = []
    for instruction in instructions:
        try:
            if instruction_execution(instruction):
                completed.append(instruction)
        except:
            continue

    for done in completed:
        instructions.remove(done)

print("Part one answer: ", wires['a'])

""" Part two """

new_b = wires['a']
wires = {'b': new_b,}

with open('input_d7.txt') as f:
    instructions = f.readlines()

while instructions:
    completed = []
    for instruction in instructions:
        # Override the instruction which sets wire b to keep it at required value
        if instruction == "19138 -> b\n":
            completed.append(instruction)
            continue
        try:
            if instruction_execution(instruction):
                completed.append(instruction)
        except:
            continue

    for done in completed:
        instructions.remove(done)


# Answer Two
print("Answer Two =", wires['a'])


