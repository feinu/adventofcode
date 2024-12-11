data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


with open("data.txt") as f:
    data = f.read().strip()

rules, books = data.split("\n\n")

rules = rules.split("\n")
books = books.split("\n")


def is_valid_page(index, pages):
    """Only check to the right, because we work left to right"""
    for page in pages[i + 1:]:
        if f"{page}|{pages[index]}" not in rules:
            return False
    return True


def make_valid_book(pages):
    """And return middle page number"""
    book = [pages[0]]
    remainder = pages[1:]
    while remainder:
        page = remainder.pop(0)
        if f"{page}|{book[0]}" in rules:  # insert before
            book = [page] + book
            continue
        elif f"{book[-1]}|{page}" in rules:  # append after
            book = book + [page]
            continue
        for i in range(len(book) - 1):
            # Slot page in after i
            if f"{book[i]}|{page}" in rules and f"{page}|{book[i + 1]}" in rules:
                book = book[:i + 1] + [page] + book[i + 1:]
                break
    return int(book[len(book) // 2])


valid_total = 0
invalid_total = 0
for book in books:
    is_valid = True
    pages = book.split(",")
    for i in range(len(pages)):
        for page in pages[i + 1:]:
            if f"{page}|{pages[i]}" in rules:
                # Bad order
                is_valid = False
                break
        if not is_valid:
            break
    if is_valid:
        valid_total += int(pages[len(pages) // 2])
    else:
        invalid_total += make_valid_book(pages)
print(valid_total, invalid_total)
