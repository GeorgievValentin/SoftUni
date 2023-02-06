def loading_bar(num):
    bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ]
    if num == 0:
        return bar
    num //= 10
    for index in range(num):
        bar[index] = "%"
    return bar


number = int(input())
result_bar = loading_bar(number)
if result_bar.count("%") == 10:
    print("100% Complete!")
    print(f"[{''.join(result_bar)}]")
else:
    print(f"{number}% [{''.join(result_bar)}]")
    print("Still loading...")
