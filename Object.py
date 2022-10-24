class Warrior:
    def __init__(self, name = 'Ронин', health = 100, stamina = 100):
        self.name = name
        self.health = health
        self.stamina = stamina
    def introduces(self):
        print(f'Class: {self.__class__.__name__ }',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
    def heals(self, target):
        if self.stamina < 20:
            print('!Stamina is to low!')
        else:
            print("--------")
            print(f'{self.__class__.__name__} применяет лечебные травы')
            target.health += 10
            self.stamina -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}\n',
                  f'У {self.__class__.__name__} осталось {self.stamina} единиц стамины')
            print("--------")
    def attacks(self, target):
        print("--------")
        print(f'{self.__class__.__name__} атакует мечом')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} упало до {target.health}\n')
        print("--------")

class Mage:
    def __init__(self, health = 60, mana = 100):
        self.health = health
        self.mana = mana
    def introduces(self):
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nMana: {self.mana}')
    def heals(self, target):
        if self.mana < 20:
            print('!Mana is to low!')
        else:
            print("--------")
            print(f'{self.__class__.__name__} применяет заклинание лечения')
            target.health += 10
            self.mana -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}\n',
                  f'У {self.__class__.__name__} осталось {self.mana} единиц маны')
            print("--------")
    def attacks(self, target):
        print("--------")
        print(f'{self.__class__.__name__} атакует магией')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} упало до {target.health}\n')
        print("--------")

unit1 = Warrior()
unit2 = Warrior(stamina = 180)
unit3 = Mage()
unit4 = Mage(65, 200)

print(unit1.__dict__)
print(unit2.__dict__)
print(unit3.__dict__)
print(unit4.__dict__)
unit3.introduces()
unit1.introduces()
unit3.heals(unit1)
unit1.heals(unit3)
unit1.introduces()
unit3.introduces()
action = input(Выберите действие)
while unit1.health > 0 or unit1.health > 0: