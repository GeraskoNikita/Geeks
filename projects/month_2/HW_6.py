from faker import Faker

# Эта библиотека нужна для генерации случайных данных:
# имен, адресов, телефонов и другой тестовой информации.

fake = Faker()

print("Имя:", fake.name())
print("Адрес:", fake.address())
print("Телефон:", fake.phone_number())


# Часть 2 — Two Sum
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
