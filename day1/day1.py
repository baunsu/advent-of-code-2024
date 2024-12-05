file = open("input", "r")
input = []

for c in file:
    line = c.split("\n")
    input.append(line[0])

file.close()

left, right = [], []
for line in input:
    numbers = line.split("   ")
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))
    
def part1(l, r):
    l.sort()
    r.sort()

    result = 0

    for i in range(len(l)):
        result += abs(l[i] - r[i])
    return result
print(part1(left, right))

def part2(l, r):
    result = [0] * len(l)
    pos = 0
    for i in range(len(l)):
        for j in range(len(r)):
            if l[i] == r[j]:
                result[pos] += 1
        result[pos] *= l[i]
        pos += 1
    return sum(result)

print(part2(left, right))