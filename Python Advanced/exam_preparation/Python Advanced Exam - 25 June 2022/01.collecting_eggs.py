eggs = [int(x) for x in input().split(", ")]
papers = [int(x) for x in input().split(", ")]
eggs.reverse()
boxes = 0

while eggs and papers:
    current_egg = eggs.pop()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_paper = papers.pop()
    if current_egg + current_paper <= 50:
        boxes += 1

eggs.reverse()
if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")

