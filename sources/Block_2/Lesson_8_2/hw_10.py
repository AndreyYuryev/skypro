class Hero():

    def __init__(self, name, posessions):
        self.name = name
        self.posessions = posessions

    def __repr__(self):
        things = ", ".join(self.posessions)
        return f"Герой ({self.name} взял с собой {things})"

# Не удаляйте код ниже, он нужен для проверки

hero = Hero("Питомир", ["меч", "плащ", "шляпа"])
print(hero)
