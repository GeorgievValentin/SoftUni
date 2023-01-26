movie = input()
students = 0
standards = 0
kids = 0
total_tickets = 0
while movie != "Finish":
    free_spaces = int(input())
    sold_tickets = 0
    total_spaces = free_spaces
    while free_spaces > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            students += 1
        elif ticket_type == "standard":
            standards += 1
        elif ticket_type == "kid":
            kids += 1
        sold_tickets += 1
        free_spaces -= 1
    percent_full = sold_tickets / total_spaces * 100
    print(f"{movie} - {percent_full:.2f}% full.")
    movie = input()
total_tickets = students + standards + kids
percent_student = students / total_tickets * 100
percent_standard = standards / total_tickets * 100
percent_kid = kids / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")