from random import randint, choice, choices
from os import replace

class Card:
    def __init__(self):
        self.num1 = []
        self.num2 = []
        self.__user_card = []
        self.__comp_card = []
        self.get_card()
        self.usercart()
        self.compcart()
        self.n = 'н'.lower() or 'n'.lower() or 'т'.lower()
        self.y = 'д'.lower() or 'y'.lower()
        self.l = []

    def __add__(self, other):
        self.__user_card.append(self.num1)
        self.__comp_card.append(self.num2)
        return self

    def keg(self):
        self.keg = randint(1, 90)
        return self.keg

    def __str__(self):
        return f'{self.num1} {self.num2}'

    def cart(self):
        if len(self.num1) <= 16:
            while len(self.num1) != 16:
                i = randint(1, 90)
                if i not in self.num1:
                    self.num1.append(i)
        if len(self.num2) <= 16:
            while len(self.num2) != 16:
                i = randint(1, 90)
                if i not in self.num2:
                    self.num2.append(i)
        return self.num1, self.num2

    def usercart(self):
        self.__user_card = '\n', sorted(self.num1[0:5]), '\n', sorted(self.num1[5:10]), '\n', sorted(self.num1[11:16])

        return f'{self.__user_card}'

    def compcart(self):
        self.__comp_card = '\n', sorted(self.num2[0:5]), '\n', sorted(self.num2[5:10]), '\n', sorted(self.num2[11:16])
        return f'{self.__comp_card}'

    def razbivka_user(self):
        n = 0
        while n != 4:
            self.__user_card[1].insert(randint(0, 5), ' '),
            self.__user_card[3].insert(randint(0, 5), ' ')
            self.__user_card[5].insert(randint(0, 5), ' ')
            n += 1
            continue
        return self.__user_card

    def razbivka_comp(self):
        n = 0
        while n != 4:
            self.__comp_card[1].insert(randint(0, 5), ' '),
            self.__comp_card[3].insert(randint(0, 5), ' ')
            self.__comp_card[5].insert(randint(0, 5), ' ')
            n += 1
            continue
        return self.__comp_card

    def cart_geimer(self):
        self.__user_card = ' '.join([' '.join([str(elem) for elem in line]) for line in self.__user_card])
        return self.__user_card

    def cart_geimer2(self):
        self.__comp_card = ' '.join([' '.join([str(elem) for elem in line]) for line in self.__comp_card])
        return self.__comp_card

    def get_card(self):
        return f'{"-" * 7} Ваша карточка {"-" * 7}  {self.__user_card} \n {"-" * 28} \n {"-" * 3} Карточка компьютера {"-" * 4} {self.__comp_card}\n {"-" * 28}'

class Keg(Card):
    def keg_random(self):
        self.keg_rand = randint(1, 90)
        return self.keg_rand

    def __add__(self, other):
        self.l.append(self.keg_rand)
        return self, self.l

    def list_keg(self):
        return f'выпали: {i in self.l}'

    def find_boch(self):
        print(self.l.append(self.keg_random()))
        # print(self.get_card())
        print(f'{self.cart()}{self.usercart()}{self.compcart()} {self.razbivka_user()}{self.razbivka_comp()} {self.cart_geimer2()}{self.cart_geimer()} \n {self.get_card()}')
        print(f'Выпал бочонок: {self.keg_random()}')
        self.__qwestion = input('Хотите зачеркнуть? (д / н): ')
        if self.__qwestion == 'д'.lower() or 'y'.lower():
            for i in self.usercart():
                el = '-'
                self.usercart().replace(i, el)
                continue
        for i in self.compcart():
            el = '-'
            self.new_comcart = self.compcart().replace(i, el)
            return self.new_comcart
        print(f'{self.game()}{self.find_boch()} {self.game()}')
        print(self.find_boch())

    def game(self):
        if self.keg_random() in self.num1 or self.num2:
            for i in self.num1:
                it = '-'
                list(self.num1).insert(i, it)
                i = it
                if i != 0:
                    continue
                else:
                    print('Компьютер выйграл!')
                    break
            for elem in self.num2:
                el = '-'
                list(self.num1).insert(elem, el)
                if elem != 0:
                    continue
                else:
                    print('Вы выйграли!')
                    break
            else:
                print('Вы проиграли!')
                return 2

        return f'{self.razbivka_user()} {self.razbivka_comp()}'

if __name__ == '__main__':
    game = Keg()
    cart = Card()
    while True:
        s = game.find_boch()
        print(game.game())
        if game.keg_random() in cart.num1 or cart.num2:
            for item in Card.cart():
                '-'.join(item)
                if item != 0:
                    continue
                else:
                    print('Компьютер выйграл!')

            for elem in cart.num2:
                if __qwestion == 'д'.lower() or 'y'.lower():
                    '-'.join(elem)
                    if elem != 0:
                        continue
                    else:
                        print('Вы выйграли!')
                else:
                    print('Вы проиграли!')
                    break
            continue