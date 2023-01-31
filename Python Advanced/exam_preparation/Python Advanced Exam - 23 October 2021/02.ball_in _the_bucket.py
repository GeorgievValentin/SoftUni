size = 6
matrix = []
score = 0
prize = ""

for row in range(size):
    line = input().split()
    matrix.append(line)

for _ in range(3):
    coord = [int(el) for el in input() if el.isdigit()]
    row = coord[0]
    col = coord[1]

    if row < size and col < size:
        if matrix[row][col] == "B":
            matrix[row][col] = "0"
            for row in range(size):
                score += int(matrix[row][col])

if score >= 300:
    prize = "Lego Construction Set"
elif 200 <= score <= 299:
    prize = "Teddy Bear"
elif 100 <= score <= 199:
    prize = "Football"

if score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
else:
    print(f"Good job! You scored {score} points, and you've won {prize}.")
