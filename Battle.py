import random



spec = random.randrange(10,21)
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
        if self.stamina < 20:
            print("Недостаточно стамины. Рыцарь выдохся")
        else:
            print("--------")
            print("Натиск!")
            print(f' Собравшись {self.name} наносит повышенный урон ! {target.name}')
            target.health -= 15
            self.stamina -= 20
            print(f'Здоровье у {target.name} понижено до {target.health}\n',
                f'У {self.name} осталось {self.stamina} единиц сил')
            print("--------")
    def bercerk(self, target):
        if self.health < 20:
            print("Рыцарь не переживёт впадание в боевое безумие")
        else:
            print("--------")
            print("Ненависть закипает в нутри рыцаря! \n"
                  "Он бросается на врага забыв о защите")
            print(f'{self.name} наносит рану за раной {target.name}')
            target.health -= spec * 2.5
            self.health -= 19
            print(f'Здоровье у {target.name} понижено до {target.health}\n',
                f' {self.name} замечает, что его тоже задели в пылу битвы, \n'
                f' его здоровье снизилось до {self.health} единиц ')
            print("--------")
class Mage:
    def __init__(self, name='mage', health=80, mana=120):
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
        if self.mana < 20:
            print("Недостаточно маны для заклинания лечения")
        else:
            print("--------")
            print("Фаербол!")
            print(f'{self.name} наносит урон магией ОГНЯ! {target.name}')
            target.health -= spec
            self.mana -= 20
            print(f'Здоровье у {target.name} понижено до {target.health}\n',
                f'У {self.name} осталось {self.mana} единиц маны')
            print("--------")
    def blood_magic(self, target):
        if self.health < 20:
            print("Маг не переживёт каст магии крови")
        else:
            print("--------")
            print("Взывая к запретному искуству, маг режет себе кисть...")
            print(f'{self.name} наносит урон магией Крови! {target.name}')
            target.health -= spec * 2.5
            self.health -= 19
            print(f'Здоровье у {target.name} понижено до {target.health}\n',
                f'У {self.name} осталось {self.health} единиц здоровья')
            print("--------")

unit1 = Warrior('Рыцарь')
unit2 = Mage('Сорка')

while unit1.health > 0 and unit2.health > 0:
    action = input('Выберите действие: 1 - атака, 2 - лечение '
                   '3 - специальный навык, 4 - запретный навык')
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
              "Рыцарь - натиск = 15 ед гарантированного урона\n"
              'Сорка - огненный шар = 10-20 ед урона буйством огня\n')
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
    elif action == '4':
        print("Запретное искуство! Расплатой будет твоя жизненная сила!\n" 
              "Рыцарь - Берсерк = 25-50 ед урона от серии жестоких ударов\n"
              'Сорка - Магия крови = 25-50 ед урона кипящей кровью\n')

        u4 = input('Выберите действующего юнита: 1 - Рыцарь, 2 - Сорка, ')
        if u4 == '1':
            to_u4 = input('Выберите цель: 1 - Рыцарь, 2 - Сорка, ')
            if to_u4 == '1':
                unit1.bercerk(unit1)
                print('В безумии, рыцарь изрезал СЕБЯ ;)\n---------')
            elif to_u4 == '2':
                unit1.bercerk(unit2)

        elif u4 == '2':
            to_u4 = input('Выберите цель: 1 - Рыцарь, 2 - Сорка, ')
            if to_u4 == '1':
                unit2.blood_magic(unit1)
            elif to_u4 == '2':
                unit2.blood_magic(unit2)
                print('Не совладав с магией крови, маг вскипятил СЕБЯ;)\n---------')

else:
    print(f'Здоровье Рыцаря = {unit1.health}, Мага = {unit2.health}')
    if unit1.health > unit2.health:
        print(f'Рыцарь заколол Мага')
    else:
        print(f'Маг сжег Рыцаря')