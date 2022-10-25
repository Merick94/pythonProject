import random



spec = random.randrange(5,16)
class Warrior:
    def __init__(self, name='warrior', health=100, stamina=100):
        self.name = name
        self.health = health
        self.stamina = stamina

    def introduces(self):
        print("--------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Name : {self.name}\n'
              f'Health: {self.health}\n'
              f'Stamina: {self.stamina}')
        print("--------")

    def heals(self, target):
        if self.stamina < 20:
            print("Недостаточный запас сил для лечения травами")
        else:
            print("--------")
            print(f'{self.name} собирает целебные травы и накладывает повязку',
                  f'на {target.name}')
            target.health += 10
            self.stamina -= 20
            print(f'Здоровье у {target.name} повышено до {target.health}\n',
                  f'У {self.name} осталось {self.stamina} единиц сил')
            print("--------")

    def attacks(self, target):
        print("--------")
        print(f'{self.name} наносит урон мечом {target.name}')
        target.health -= 3
        print(f'Здоровье у {target.name} понижено до {target.health}')
        print("--------")

    def special(self, target):
        print("--------")
        print("Натиск!")
        print(f' Собравшись {self.name} наносит повышенный урон ! {target.name}')
        target.health -= 10
        self.stamina -= 20
        print(f'Здоровье у {target.name} понижено до {target.health}\n',
            f'У {self.name} осталось {self.stamina} единиц сил')
        print("--------")

class Mage:
    def __init__(self, name='mage', health=60, mana=100):
        self.name = name
        self.health = health
        self.mana = mana

    def introduces(self):
        print("--------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Name : {self.name}\n'
              f'Health: {self.health}\n'
              f'Mana: {self.mana}')
        print("--------")

    def heals(self, target):
        if self.mana < 20:
            print("Недостаточно маны для заклинания лечения")
        else:
            print("--------")
            print(f'{self.name} применяет заклинание лечения',
                  f'на {target.name}')
            target.health += 10
            self.mana -= 20
            print(f'Здоровье у {target.name} повышено до {target.health}\n',
                  f'У {self.name} осталось {self.mana} единиц маны')
            print("--------")

    def attacks(self, target):
        print("--------")
        print(f'{self.name} наносит урон магией {target.name}')
        target.health -= 3
        print(f'Здоровье у {target.name} понижено до {target.health}')
        print("--------")

    def special(self, target):
        print("--------")
        print("Фаербол!")
        print(f'{self.name} наносит урон магией ОГНЯ! {target.name}')
        target.health -= spec
        self.mana -= 20
        print(f'Здоровье у {target.name} понижено до {target.health}\n',
            f'У {self.name} осталось {self.mana} единиц маны')
        print("--------")

unit1 = Warrior('Рыцарь')
unit2 = Mage('Сорка')

while unit1.health > 0 or unit2.health > 0:

    action = input('Выберите действие: 1 - атака, 2 - лечение '
                   '3 - специальный навык')
    if action == '1':
        print("Выбрана атака!")
        u = input('Выберите действующего юнита: 1 - Рыцарь, 2 - Сорка, ')
        if u == '1':
            to_u = input('Выберите цель: 1 - Рыцарь, 2 - Сорка, ')
            if to_u == '1':
                unit1.attacks(unit1)
                print('сам себя коцнул ;)\n---------')
            elif to_u == '2':
                unit1.attacks(unit2)

        elif u == '2':
            to_u = input('Выберите цель: 1 - Рыцарь, 2 - Сорка, ')
            if to_u == '1':
                unit2.attacks(unit1)
            elif to_u == '2':
                unit2.attacks(unit2)
                print('сам себя коцнул ;)\n---------')

    elif action == '2':
        print("Выбрано лечение!")
        u2 = input('Выберите действующего юнита: 1 - Рыцарь, 2 - Сорка, ')
        if u2 == '1':
            to_u2 = input('Выберите цель: 1 - Рыцарь, 2 - Сорка, ')
            if to_u2 == '1':
                unit1.heals(unit1)
            elif to_u2 == '2':
                unit1.heals(unit2)
                print('подлечил соперника ;)\n---------')

        elif u2 == '2':
            to_u2 = input('Выберите цель: 1 - Рыцарь, 2 - Сорка, ')
            if to_u2 == '2':
                unit2.heals(unit2)
            elif to_u2 == '1':
                unit2.heals(unit1)
                print('подлечил соперника ;)\n---------')
    if action == '3':
        print("Выбран особый навык!\n" 
              "Рыцарь - натиск = 10 ед гарантированного урона\n"
              'Сорка - огненный шар = 5-15 ед урона буйством огня\n')
        u3 = input('Выберите действующего юнита: 1 - Рыцарь, 2 - Сорка, ')
        if u3 == '1':
            to_u3 = input('Выберите цель: 1 - Рыцарь, 2 - Сорка, ')
            if to_u3 == '1':
                unit1.special(unit1)
                print('сам себя покалечил суператакой ;)\n---------')
            elif to_u3 == '2':
                unit1.special(unit2)

        elif u3 == '2':
            to_u3 = input('Выберите цель: 1 - Рыцарь, 2 - Сорка, ')
            if to_u3 == '1':
                unit2.special(unit1)
            elif to_u3 == '2':
                unit2.special(unit2)
                print('сам себя подпалил! Магия - не твоё ;)\n---------')