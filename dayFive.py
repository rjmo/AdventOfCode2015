import re

all_words = []
naughty = []
potentially_nice = []
at_least_3_vowels = []
double_letter = []
final = []
check = []

DOUBLE_LETTERS = [item + item for item in 'abcdefghijklmnopqrstuvwxyz']
with open('day_five.txt') as f:
    for line in f.readlines():
        all_words.append(line.strip())

f.close()


def find_naughty(string):

    pattern = re.compile(r'ab|cd|pq|xy')
    sttrb = pattern.findall(string.strip())
    if len(sttrb) > 0:
        naughty.append(string.strip())
    else:
        potentially_nice.append(string.strip())


def find_vowels(string):

    pattern_nice = re.compile(r'[aeiouAEIOU]')
    wor = pattern_nice.findall(string.strip())

    if len(wor) >= 3:
        check.append(string.strip())


def double_letters(string):
    for item in DOUBLE_LETTERS:
        if item in string:
            if string not in final:
                final.append(string.strip())


for bb in all_words:
    find_naughty(bb)

for element in potentially_nice:
    find_vowels(element)

for el in check:
    double_letters(el)


print(len(potentially_nice))
print(len(check))
print(len(final))
# done