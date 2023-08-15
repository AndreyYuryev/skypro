class Hero:

  def go_right(self, lenght):
    print(f"Я иду {lenght} метров направо")

  def go_left(self, lenght):
    print(f"Я иду {lenght} метров налево")

  def observe(self):
    print(f"Я осматриваюсь")


hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()