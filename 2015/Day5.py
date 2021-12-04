""" Day 5: Doesn't he have intern-elves for this? """

def vowels_check(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    sum = 0
    for i in word:
        if any(y in i for y in vowel):
            sum +=1
            if sum >=3:
                return True
    return False

def combo_letters_check(word):
    return not any(i in word for i in ('ab', 'cd', 'pq', 'xy'))

def double_letters_check(word):
    for i in range(0,len(word)-1):
        if word[i+1] == word[i]:
            return True
    return False

def pair_of_letters(word):
    for i in range(0,len(word)-1):
        string = word[i]+word[i+1]
        counts = word.count(string)
        if counts>=2:
            return True
    return False

def repeat_letters_check(word):
    for i in range(0,len(word)-2):
        if word[i] == word[i+2]:
            return True
    return False

def nice_string(part_two = False):
    with open('input_d5.txt') as f:
        data = [line.split() for line in f]
    print('Total lines of text: ', len(data))
    nice_sum = 0
    if part_two == False:
        for word in data:
            if (vowels_check(word[0]) and
            combo_letters_check(word[0]) and
            double_letters_check(word[0])):
                nice_sum += 1
    else:
        for word in data:
            if (pair_of_letters(word[0]) and 
            repeat_letters_check(word[0])):
                nice_sum += 1
    return nice_sum
            

    
print('Nice strings: ',nice_string())
print('Nice strings part two: ', nice_string(part_two = True))


# import re

# with open('input_d5.txt') as f:
#     strings = f.readlines()
# naughty_regex = re.compile(r'ab|cd|pq|xy')
# vowel_regex = re.compile(r'([aeiou].*){3,}')
# double_regex = re.compile(r'(.)\1')
# repeated_regex  = re.compile(r'(..).*\1')
# gapped_regex = re.compile(r'(.).\1')

# x = 'auwwwoww'
# print(gapped_regex.search(x))