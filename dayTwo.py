count = 0
arr = []


def multiplicationSize(l, w, h):
    values = []
    total = (2 * int(l) * int(w)) + (2 * int(w) * int(h)) + (2 * int(h) * int(l))

    va1 = int(l) * int(w)
    val2 = int(w) * int(h)
    val3 = int(h) * int(l)

    values.append(va1)
    values.append(val2)
    values.append(val3)

    return total + min(values)


def ribbon(l, w, h):
    values = []
    ribbonValues = []

    bow = int(l) * int(w) * int(h)

    va1 = int(l) * int(w)
    val2 = int(w) * int(h)
    val3 = int(h) * int(l)

    values.append(va1)
    values.append(val2)
    values.append(val3)

    ribbonValues.append((int(l), int(w)))
    ribbonValues.append((int(w), int(h)))
    ribbonValues.append((int(h), int(l)))

    return bow + calc(ribbonValues[values.index(min(values))][0], ribbonValues[values.index(min(values))][1])


def calc(val, val1):
    return val + val + val1 + val1


with open('papers.txt') as f:
    for line in f.readlines():
        arr.append(line.strip().split('x'))

    for element in arr:
        count += ribbon(element[0], element[1], element[2])
print(count)

f.close()
