countries = input().split(", ")
capitals = input(). split(", ")

result = zip(countries, capitals)
final = {country: capital for country, capital in result}
for country, capital in final.items():
    print(f"{country} -> {capital}")
