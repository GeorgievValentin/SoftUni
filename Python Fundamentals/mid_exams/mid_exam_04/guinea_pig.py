def guinea_pig():
    food_amount = float(input()) * 1000
    hay_amount = float(input()) * 1000
    cover_amount = float(input()) * 1000

    guinea_pig_weight = float(input()) * 1000

    for day in range(1, 31):
        daily_food = 300
        daily_cover = guinea_pig_weight / 3

        if food_amount < daily_food:
            break
        food_amount -= daily_food
        daily_hay = food_amount * 0.05
        if day % 2 == 0:
            if hay_amount < daily_hay:
                break
            hay_amount -= daily_hay
        if day % 3 == 0:
            if cover_amount < daily_cover:
                break
            cover_amount -= daily_cover
    else:
        return f"Everything is fine! Puppy is happy! Food: {food_amount / 1000:.2f}, Hay: {hay_amount / 1000:.2f}, Cover: {cover_amount / 1000:.2f}."
    return "Merry must go to the pet store!"


print(guinea_pig())
