country = list(input().split(", "))
capital = list(input().split(", "))

my_dict = dict(zip(country, capital))
for country, capital in my_dict.items():
    print(f"{country} -> {capital}")