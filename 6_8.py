countries: dict = {
    "Russia": ["Moscow", "Kaluga", "Smolensk"],
    "USA": ["New York", "Detroit", "Miami"]
}
city: str = input()
for country, cities in countries.items():
    if city in cities:
        print(country)
        break