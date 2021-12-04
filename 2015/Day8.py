""" Day 8: Matchsticks """
import re
with open('input_d8.txt') as f:
    datarows = f.readlines()

letter_regex = re.compile(r'(a-z)')
# for row in datarows:


# test_text = "mikevjzhnwgx\"fozrj\x"h\""
test_text = "nugkdmqwdq\x50amallrskmrxoyo"
single_quote_regex = re.compile(r'(\")')
single_quote_regex = re.compile(r'(\+x)')
test =single_quote_regex.findall(test_text)

print(test)




"""
börja med att ta bort blanksteg
räkna sedan totalt antal tecken med r
räkna sedan totalt antal tecken utan r
"""
tot_char = 0
memory = 0
for row in datarows:
    row = row.replace(' ','') # delete all spaces
    memory += len(row) 
    double_quote = len(letter_regex.findall(row))
    tot_char += len(row) + double_quote*2

print(tot_char)
print(memory)
    

test_text = "nugkdmqwdq\x50amallrskmrxoyo"
test = '\xc4'
print(repr(test))

print(test[0])


