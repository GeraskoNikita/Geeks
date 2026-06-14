import time


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


# Декоратор проверки администратора
def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            func(user)
        else:
            print("У вас нет доступа")
    return wrapper


@is_admin
def delete_video(user):
    print("Видео удалено")


# Декоратор таймера
def timer(func):
    def wrapper():
        start_time = time.time()

        func()

        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time:.1f} секунд")

    return wrapper


@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")


# Проверка задания 1
admin = User("Ardager", "admin")
user = User("Bek", "user")

delete_video(admin)
delete_video(user)

print()

# Проверка задания 2
download_video()