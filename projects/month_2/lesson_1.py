class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


# Создаем два объекта
hero1 = Hero("Артур", 5, 10, 7)
hero2 = Hero("Ланселот", 3, 8, 5)

# Работа с первым героем
hero1.greet()
print(f"До атаки: сила = {hero1.strength}")
hero1.attack()
print(f"После атаки: сила = {hero1.strength}")

print(f"До отдыха: здоровье = {hero1.health}")
hero1.rest()
print(f"После отдыха: здоровье = {hero1.health}")

print()

# Работа со вторым героем
hero2.greet()
print(f"До атаки: сила = {hero2.strength}")
hero2.attack()
print(f"После атаки: сила = {hero2.strength}")

print(f"До отдыха: здоровье = {hero2.health}")
hero2.rest()
print(f"После отдыха: здоровье = {hero2.health}")