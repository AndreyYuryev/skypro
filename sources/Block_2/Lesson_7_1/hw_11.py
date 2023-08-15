order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for itm in order:
    order_converted.append(dict(count=round(itm['skolko']),
                                specie=str(itm['poroda']).capitalize(),
                                avg_size=round(int(itm['sred_razmer']) / 10)))

# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
    for key, value in item.items():
        print(key, value)
