import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0 and self._cords[2] + dz * self.speed < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        return f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True  # Наличие клюва

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")  # Количество яиц может быть от 1 до 4

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        if dz < 0:
            self._cords[2] -= abs(dz) * self.speed / 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

    def speak(self):
        print(self.sound)

# Пример использования классов
db = Duckbill(10)

# Утконос жив и имеет клюв
print(db.live)  # True
print(db.beak)  # True

# Утконос издает звук
db.speak()      # Click-click-click

# Утконос пытается атаковать
db.attack()     # Be careful, I'm attacking you 0_0

# Утконос совершает маневры
db.move(1, 2, 3)
print(db.get_cords())  # X: 10 Y: 20 Z: 30

# Утконос ныряет
db.dive_in(-6)
print(db.get_cords())  # X: 10 Y: 20 Z: 0 (или другой Z, если скорость разная)

# Утконос откладывает яйца
db.lay_eggs()  # Here are(is) X eggs for you (где X - случайное число от 1 до 4)
