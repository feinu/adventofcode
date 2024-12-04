import re


with open("data.txt") as f:
    data = f.read()

sdata = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

length = data.index("\n")
line_down = r"[XMAS\n]{" + str(length) + r"}"
line_down_left = r"[XMAS\n]{" + str(length - 1) + r"}"
line_down_right = r"[XMAS\n]{" + str(length + 1) + r"}"

right = r"XMAS"  # space right
left = r"SAMX"  # space right
down = line_down.join(right)  # space down
up = line_down.join(left)  # space down
down_left = line_down_left.join(right)  # space down and left
up_right = line_down_left.join(left)  # space down and left
down_right = line_down_right.join(right)  # space down and right
up_left = line_down_right.join(left)  # space down and right

matches = 0
for i in range(len(data)):
    if i % (length + 1) <= length - 4:  # We can go right
        if re.match(right, data[i:]):
            print(i // (length + 1), i % (length + 1), "right")
            matches += 1
        if re.match(left, data[i:]):
            print(i // (length + 1), i % (length + 1), "left")
            matches += 1
        if i // (length + 1) <= length - 4:  # and down
            if re.match(down_right, data[i:]):
                print(i // (length + 1), i % (length + 1), "downright")
                matches += 1
            if re.match(up_left, data[i:]):
                print(i // (length + 1), i % (length + 1), "upleft")
                matches += 1
    if i // (length + 1) <= length - 4:  # We can go down
        if i % (length + 1) >= 3:  # and left
            if re.match(up_right, data[i:]):
                print(i // (length + 1), i % (length + 1), "upright")
                matches += 1
            if re.match(down_left, data[i:]):
                print(i // (length + 1), i % (length + 1), "downleft")
                matches += 1
        if re.match(down, data[i:]):
            print(i // (length + 1), i % (length + 1), "down")
            matches += 1
        if re.match(up, data[i:]):
            print(i // (length + 1), i % (length + 1), "up")
            matches += 1

print(matches)


xmases = 0
"""
M S    S M
 A      A
M S    S M
"""

mas = line_down_left.join([r"S.M", "A", "S.M"])
sam = line_down_left.join([r"M.S", "A", "M.S"])
sas = line_down_left.join([r"S.S", "A", "M.M"])
mam = line_down_left.join([r"M.M", "A", "S.S"])
for i in range(len(data)):
    if i % (length + 1) <= length - 3 and i // (length + 1) <= length - 3:
        if re.match(mas, data[i:]):
            print(i // (length + 1), i % (length + 1), "mas")
            xmases += 1
        if re.match(sam, data[i:]):
            print(i // (length + 1), i % (length + 1), "sam")
            xmases += 1
        if re.match(sas, data[i:]):
            print(i // (length + 1), i % (length + 1), "sas")
            xmases += 1
        if re.match(mam, data[i:]):
            print(i // (length + 1), i % (length + 1), "mam")
            xmases += 1
print(xmases)
# 946 too low
