import random


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

    def rest(self):
        self.health += 1
        print(f"{self.name} отдыхает и восстанавливает здоровье.")


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")


# Создаем героев
warrior = Warrior("Артур", 5, 100, 20, 50)
mage = Mage("Мерлин", 5, 80, 25, 100)
assassin = Assassin("Эцио", 5, 90, 22, 80)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

# Warrior  = Камень
# Assassin = Ножницы
# Mage     = Бумага

# Правила игры
wins = {
    "warrior": "assassin",
    "assassin": "mage",
    "mage": "warrior"
}

# Выбор игрока
choice = input(
    "Выберите героя (Warrior / Mage / Assassin): "
).lower()

if choice not in heroes:
    print("Неверный выбор!")
else:
    player = heroes[choice]

    enemy_name = random.choice(list(heroes.keys()))
    enemy = heroes[enemy_name]

    print(f"\nВы выбрали: {player.__class__.__name__}")
    print(f"Противник: {enemy.__class__.__name__}\n")

    if choice == enemy_name:
        print("Ничья!")
    elif wins[choice] == enemy_name:
        print(f"{player.__class__.__name__} победил!")
    else:
        print(f"{enemy.__class__.__name__} победил!")