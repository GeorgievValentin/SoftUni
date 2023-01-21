from math import ceil

movie_name = input()
movie_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4
left_time = break_time - lunch_time - relax_time
diff = abs(movie_time - left_time)

if movie_time <= left_time:
    print(f"You have enough time to watch {movie_name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(diff)} more minutes.")
