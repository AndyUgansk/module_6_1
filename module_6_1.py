# Создаем базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name  # Имя животного
        self.alive = True  # Животное изначально живое
        self.fed = False  # Животное изначально не накормлено

    # Метод для поедания растения
    def eat(self, food):
        if food.edible:  # Если растение съедобное
            print(f"{self.name} съел {food.name}")
            self.fed = True  # Животное накормлено
        else:  # Если растение несъедобное
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # Животное погибает


# Создаем базовый класс Plant
class Plant:
    def __init__(self, name):
        self.name = name  # Имя растения
        self.edible = False  # Растение изначально несъедобное


# Создаем класс Mammal, наследующийся от Animal
class Mammal(Animal):
    pass  # Пока что ничего дополнительного не добавляем


# Создаем класс Predator, наследующийся от Animal
class Predator(Animal):
    pass  # Пока что ничего дополнительного не добавляем


# Создаем класс Flower, наследующийся от Plant
class Flower(Plant):
    pass  # Пока что ничего дополнительного не добавляем


# Создаем класс Fruit, наследующийся от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)  # Вызываем конструктор родительского класса
        self.edible = True  # Переопределяем атрибут edible на True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
