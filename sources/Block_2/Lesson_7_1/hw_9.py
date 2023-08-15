fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for item in fish:
    if 'fresh' in item.values():
        fresh_water.append(item['specie'])
    else:
        sea_water.append(item['specie'])

print("Морские: ", end='')
print(*sea_water, sep=', ')

print("Пресноводные: ", end='')
print(*fresh_water, sep=', ')
