import re


def muls(string):
    return sum(int(p[0]) * int(p[1]) for p in re.findall(r"mul\((\d+),(\d+)\)", string))


data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
with open("data.txt") as f:
    data = f.read()

print(muls(data))

total = 0
offset = 0
active = True

# data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

while True:
    print(active, offset)
    if active:
        try:
            dont_start, dont_end = re.search(r"don't\(\)", data[offset:]).span()
            total += muls(data[offset:offset + dont_start])
        except AttributeError:
            total += muls(data[offset:])
            break

        offset += dont_end
        active = False
    else:
        try:
            offset += re.search(r"do\(\)", data[offset:]).span()[1]
        except AttributeError:
            break
        active = True
print(total)
