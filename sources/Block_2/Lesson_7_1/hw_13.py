fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]


def get_fish(fish_name):
    for item in fish:
        if fish_name in item.values():
            return item["specie"], item['water']


# Не удаляйте код ниже, он нужен для проверки!

fish_name = input()
fish, water = get_fish(fish_name)
print(fish, water)
