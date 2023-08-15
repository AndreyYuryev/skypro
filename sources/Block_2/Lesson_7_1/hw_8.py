employees = [

    {"fio": "Киселёв Всеволод Эдуардович", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []
for item in employees:
    if item['vaccinated']:
        vaccinated.append(item)
    else:
        not_vaccinated.append(item)

print("Вакцинированные:")
for item in vaccinated:
    print(item['fio'])
print("Остальные:")
for item in not_vaccinated:
    print(item['fio'])
