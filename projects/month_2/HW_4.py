rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    def __add__(self, other):
        total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    def __sub__(self, other):
        total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    def __mul__(self, number):
        return Money(self.amount * number, self.currency)

    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"


# Пример использования
money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

print("money1:", money1)
print("money2:", money2)

result_add = money1 + money2
print("Сложение:", result_add)

result_sub = money1 - money2
print("Вычитание:", result_sub)

result_mul = money1 * 3
print("Умножение:", result_mul)

result_div = money1 / 2
print("Деление:", result_div)

print("100 USD в сомах:", money1.convert_to_kgs(), "KGS")